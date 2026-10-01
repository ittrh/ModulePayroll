import os
import sys
import threading
import portalocker
from contextlib import contextmanager
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

def get_db_path():
    """
    Menentukan lokasi folder dtabase, biasanya di AppData/Local
    """
    if getattr(sys, 'frozen', False):
        # Lokasinya di C:\Users\<User>\AppData\Local
        base_dir = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "DB_MonitoringBBM")
    else:
        # Lokasi: Folder root project
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir

DB_DIR = get_db_path()
DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'monitoring_bbm.db')}"
LOCK_FILE = os.path.join(DB_DIR, "monitoring_bbm.db.lock")

engine = create_engine(DATABASE_URL, echo=False)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

db_lock = threading.Lock()

# Memastikan table hanya dideklarasi sekali per sesi aplikasi
_db_init = False
def init_db_schema():
    global _db_init
    if not _db_init:
        # Import model di dalam fungsi untuk menghindari circular import
        # data initialisasi ini ada dalam file __init__.py
        # import databases.models
        Base.metadata.create_all(bind=engine)
        _db_init = True
        
@contextmanager
def get_db_session():
    """
    Session manager dengan Thread Lock (threading) dan Process Lock (portalocker).
    """
    # 1. Kunci level Thread
    with db_lock:
        # Pastikan tabel sudah dibuat sebelum membuka session
        init_db_schema()

        # 2. Kunci level Proses menggunakan context manager portalocker.Lock
        # Ini adalah cara yang benar untuk menggunakan parameter 'timeout'
        lock = portalocker.Lock(LOCK_FILE, timeout=10, mode='w')
        
        try:
            with lock:
                session = SessionLocal()
                try:
                    yield session
                    session.commit() # Disarankan commit di sini atau di fungsi pemanggil
                except Exception as e:
                    session.rollback()
                    print(f"❌ Database error: {e}")
                    raise
                finally:
                    session.close()
        except portalocker.exceptions.LockException:
            print("❌ Gagal mendapatkan akses database: Timeout (digunakan aplikasi lain).")
            raise