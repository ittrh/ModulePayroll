Karena kamu sudah memiliki file `db.py`, langkahnya menjadi sangat spesifik. Kamu tidak perlu membuat koneksi baru, cukup "mengarahkan" Alembic agar membaca variabel `Base` dan `DATABASE_URL` yang sudah ada di sana.

Berikut adalah panduan langkah demi langkah untuk mengimplementasikannya:

---

### 1. Inisialisasi Alembic

Buka terminal di folder proyekmu, lalu jalankan:

```bash
alembic init migrations

```

### 2. Hubungkan `alembic.ini` dengan Database kamu

Buka file `alembic.ini`. Cari baris `sqlalchemy.url` dan sesuaikan dengan nama database yang ada di `db.py` kamu:

```ini
sqlalchemy.url = sqlite:///db_payroll.db

```

### 3. Konfigurasi `migrations/env.py` (Langkah Paling Penting)

Agar Alembic bisa mendeteksi model-model yang nanti kamu tulis di `db.py`, kamu harus mengedit file `migrations/env.py`.

**A. Tambahkan Folder Proyek ke Path**
Di bagian paling atas (setelah import standar), tambahkan kode ini agar Alembic bisa menemukan file `db.py`:

```python
import sys
import os
sys.path.append(os.getcwd())

```

**B. Import Base dan Metadata**
Cari baris `target_metadata = None` (biasanya di sekitar baris 20) dan ubah menjadi:

```python
tambahkan juga class model disini
from db import Base
target_metadata = Base.metadata

```

**C. Aktifkan Batch Mode untuk SQLite**
Cari fungsi `run_migrations_online()`. Tambahkan `render_as_batch=True` di dalam `context.configure`:

```python
def run_migrations_online() -> None:
    # ... kode lainnya ...
    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            render_as_batch=True  # TAMBAHKAN INI
        )
        # ... kode lainnya ...

```

---

### 4. Membuat File Migrasi Pertama

Sekarang, mari kita tes. Anggaplah kamu sudah menambahkan sebuah Class Model di `db.py`, misalnya:

```python
from sqlalchemy import Column, Integer, String

class Karyawan(Base):
    __tablename__ = 'karyawan'
    id = Column(Integer, primary_key=True)
    nama = Column(String)

```

Jalankan perintah ini di terminal:

```bash
alembic revision --autogenerate -m "membuat tabel karyawan"

```

### 5. Terapkan ke Database

Terakhir, buat tabel tersebut di dalam `db_payroll.db` dengan perintah:

```bash
alembic upgrade head

```

---

### Tips untuk `db.py` kamu:

Karena sekarang kamu menggunakan Alembic, kamu **tidak perlu lagi** menjalankan perintah `Base.metadata.create_all(engine)` di dalam kode Python kamu. Alembic yang akan bertanggung jawab sepenuhnya atas pembuatan dan perubahan tabel.