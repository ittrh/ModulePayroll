Sangat tepat secara konsep, namun tempatnya kurang tepat jika diletakkan langsung di dalam tabel `payroll_details`

.

Sesuai dengan prinsip **normalisasi database** dan pemisahan antara data transaksi per karyawan (`payroll_header`) dengan data rincian per komponen gaji (`payroll_details`), letak variabel *context* sebaiknya dibagi sebagai berikut:

---

### 1. Di Mana Seharusnya *Context* Disimpan?

Variabel *context* terbagi menjadi 2 jenis:

#### A. Input Variabel Bulanan per Karyawan $\rightarrow$ Simpan di `payroll_header`

Variabel seperti `overtime_days`, `rate_per_day`, `overtime_hours`, atau `tax_rate` berlaku untuk satu karyawan dalam satu periode payroll tertentu.

* Maka, buatlah satu kolom berjenis **JSON / TEXT** bernama **`payroll_context`** atau **`formula_variables`** di tabel **`payroll_header`**.



#### B. Rincian Angka Hasil Komponen $\rightarrow$ Simpan di `payroll_details`

Tabel `payroll_details` bertugas mencatat hasil eksekusi nominal per baris komponen gaji (`FI001`, `VI001`, dst).

* Di sini, Anda cukup menyimpan **`amount`** hasil kalkulasi, dan jika perlu tambahkan kolom **`formula_snapshot`** (menyimpan rumus yang dipakai saat itu sebagai bukti audit log).

---

### 2. Gambaran Struktur Tabel & Contoh Isinya

#### **Tabel `payroll_header**`

*(Menyimpan rekap gaji karyawan + seluruh nilai variabel input bulanan)*

| id (PK) | period_id (FK) | employee_id (FK) | total_income | total_deduction | thp | **payroll_context** (JSON/TEXT) |
| --- | --- | --- | --- | --- | --- | --- |
| `hdr-001` | `period-oct-26` | `emp-uuid-001` | 5600000.00 | 140000.00 | 5460000.00 | `{"base_salary": 5000000, "overtime_days": 4, "rate_per_day": 150000, "tax_rate": 0.015, "gross_income": 5600000}` |

---

#### **Tabel `payroll_details**`

*(Menyimpan rincian hasil perhitungan per komponen gaji)*

| id (PK) | payroll_header_id (FK) | component_id (FK) | amount | **formula_used** | remarks |
| --- | --- | --- | --- | --- | --- |
| `dtl-001` | `hdr-001` | `FI001` | 5000000.00 | `base_salary` | Gaji Pokok |
| `dtl-002` | `hdr-001` | `VI001` | 600000.00 | `overtime_days * rate_per_day` | Lembur 4 hari |
| `dtl-003` | `hdr-001` | `FD001` | 56000.00 | `gross_income * 0.01` | Potongan BPJS |
| `dtl-004` | `hdr-001` | `FD002` | 84000.00 | `gross_income * tax_rate` | Potongan PPh 21 TER |

---

### 3. Mengapa Menyimpan Context JSON di `payroll_header`

 Sangat Menguntungkan?

1. **Jejak Audit & Histori (*Audit Trail*)**:
Jika 6 bulan lagi ada perubahan rumus atau perubahan gaji pokok, Anda tetap bisa melacak dengan pasti angka/variabel apa saja yang dipakai saat memproses gaji di bulan Oktober 2026.
2. **Kemudahan *Re-calculation* / Print Slip Gaji**:
Jika slip gaji dicetak ulang, sistem tidak perlu mencari data histori ke mana-mana karena seluruh data masukan (*input context*) tersimpan utuh di `payroll_header.payroll_context`.


3. **Mencegah Duplikasi Data**:
Jika ditaruh di `payroll_details`, nilai `overtime_days: 4` akan terulang di setiap baris detail komponen gaji, yang membuat query menjadi boros dan kurang terstruktur.

Berikut adalah implementasi kode model SQLAlchemy (menggunakan SQLite) yang mengakomodasi skema `payroll_header` dengan kolom `payroll_context` berformat JSON, serta tabel `salary_components` dengan kolom `formula`.

```python
import uuid
import enum
from datetime import datetime
from sqlalchemy import (
    create_engine, Column, String, Float, Boolean, 
    DateTime, ForeignKey, Enum as SQLEnum, Text, JSON
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Helper function untuk UUID primary key
def generate_uuid():
    return str(uuid.uuid4())


# ==========================================
# 1. ENUMERATIONS
# ==========================================
class ComponentType(str, enum.Enum):
    INCOME = "INCOME"
    DEDUCTION = "DEDUCTION"


# ==========================================
# 2. MASTER MODELS
# ==========================================
class Site(Base):
    __tablename__ = "site"
    
    id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)


class Position(Base):
    __tablename__ = "positions"
    
    id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)


class Composition(Base):
    __tablename__ = "compositions"
    
    id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)


class SalaryComponent(Base):
    __tablename__ = "salary_components"
    
    id = Column(String(20), primary_key=True)  # Contoh: FI001, VI001, FD001
    name = Column(String(100), nullable=False)
    type = Column(SQLEnum(ComponentType), nullable=False)
    description = Column(Text, nullable=True)
    
    # Kolom utama untuk menampung rumus matematika (misal: "overtime_days * rate_per_day")
    formula = Column(Text, nullable=True)


class Employee(Base):
    __tablename__ = "employee"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    nik = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    
    site_id = Column(String(10), ForeignKey("site.id"), nullable=True)
    position_id = Column(String(10), ForeignKey("positions.id"), nullable=True)
    composition_id = Column(String(10), ForeignKey("compositions.id"), nullable=True)
    
    # Relationships
    site = relationship("Site")
    position = relationship("Position")
    composition = relationship("Composition")


# ==========================================
# 3. TRANSACTION MODELS
# ==========================================
class PayrollPeriod(Base):
    __tablename__ = "payroll_period"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    period_name = Column(String(50), nullable=False)
    start_date = Column(String(10), nullable=False)  # YYYY-MM-DD
    end_date = Column(String(10), nullable=False)    # YYYY-MM-DD
    is_closed = Column(Boolean, default=False)


class PayrollHeader(Base):
    __tablename__ = "payroll_header"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    period_id = Column(String(36), ForeignKey("payroll_period.id"), nullable=False)
    employee_id = Column(String(36), ForeignKey("employee.id"), nullable=False)
    
    total_income = Column(Float, default=0.0)
    total_deduction = Column(Float, default=0.0)
    thp = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Menyimpan dictionary context variabel yang digunakan saat kalkulasi (misal: overtime_days, rate_per_day, dll)
    # SQLAlchemy secara otomatis mengonversi dict Python ke bentuk JSON di SQLite
    payroll_context = Column(JSON, nullable=True)
    
    # Relationships
    period = relationship("PayrollPeriod")
    employee = relationship("Employee")
    details = relationship("PayrollDetail", back_populates="header", cascade="all, delete-orphan")


class PayrollDetail(Base):
    __tablename__ = "payroll_details"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    payroll_header_id = Column(String(36), ForeignKey("payroll_header.id"), nullable=False)
    component_id = Column(String(20), ForeignKey("salary_components.id"), nullable=False)
    
    amount = Column(Float, nullable=False, default=0.0)
    formula_used = Column(Text, nullable=True)  # Snapshot rumus yang dieksekusi
    remarks = Column(Text, nullable=True)
    
    # Relationships
    header = relationship("PayrollHeader", back_populates="details")
    component = relationship("SalaryComponent")


# ==========================================
# 4. TESTING & DATABASE SETUP (SQLite)
# ==========================================
if __name__ == "__main__":
    # Setup Database SQLite Lokal
    engine = create_engine("sqlite:///payroll.db", echo=True)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n[SUCCESS] Tabel berhasil dibuat di SQLite!")

    # --- SIMULASI INSERT DATA MASTER ---
    comp_gaji = SalaryComponent(
        id="FI001",
        name="Gaji Pokok",
        type=ComponentType.INCOME,
        formula="base_salary"
    )
    
    comp_lembur = SalaryComponent(
        id="VI001",
        name="Uang Lembur",
        type=ComponentType.INCOME,
        formula="overtime_days * rate_per_day"
    )
    
    comp_pajak = SalaryComponent(
        id="FD002",
        name="Potongan PPh 21 TER",
        type=ComponentType.DEDUCTION,
        formula="gross_income * tax_rate"
    )

    session.add_all([comp_gaji, comp_lembur, comp_pajak])
    session.commit()

    # --- SIMULASI INSERT PAYROLL HEADER BERIKUT CONTEXT JSON ---
    sample_context = {
        "base_salary": 5000000,
        "overtime_days": 4,
        "rate_per_day": 150000,
        "tax_rate": 0.015,
        "gross_income": 5600000
    }

    # Asumsi ID karyawan & periode sudah ada
    header = PayrollHeader(
        period_id="period-uuid-sample",
        employee_id="emp-uuid-sample",
        total_income=5600000.0,
        total_deduction=84000.0,
        thp=5516000.0,
        payroll_context=sample_context  # Disimpan langsung dalam format Dict Python
    )

    detail_lembur = PayrollDetail(
        header=header,
        component_id="VI001",
        amount=600000.0,
        formula_used="overtime_days * rate_per_day",
        remarks="Lembur 4 hari"
    )

    session.add(header)
    session.commit()
    print("[SUCCESS] Data transaksi dan JSON context berhasil disimpan!")

```

### Penjelasan Poin Penting:

1. **Tipe Data `JSON` di SQLite**: SQLAlchemy mendukung `Column(JSON)` natively pada SQLite. SQLAlchemy secara otomatis melakukan *serialization* (mengubah dict ke JSON string saat simpan) dan *deserialization* (mengubah JSON string kembali ke dict saat dibaca).
2. **`PayrollDetail.formula_used`**: Menyimpan snapshot string rumus dari `SalaryComponent.formula` saat transaksi dibuat. Ini berguna jika di masa mendatang rumus di tabel master berubah, riwayat rumus pada slip gaji lama tidak akan terpengaruh.
3. **`PayrollHeader.payroll_context`**: Menampung seluruh variabel inputan/acuan dalam satu objek JSON utuh untuk mempermudah audit data.