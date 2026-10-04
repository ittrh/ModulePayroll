Berikut adalah gambaran grafis struktur tabel (ERD / Entity Relationship Diagram), isi sampel data, serta penjelasan relasi antartabel berdasarkan perbaikan kode `master.py` dan `transactions.py`.

---

### 1. Visualisasi Diagram Relasi Tabel (ERD)

```text
  +-------------------+          +-------------------+          +-------------------+
  |       site        |          |    positions      |          |   compositions    |
  +-------------------+          +-------------------+          +-------------------+
  | PK  id (String10) |          | PK  id (String10) |          | PK  id (String10) |
  |     name          |          |     name          |          |                   |
  +---------+---------+          +---------+---------+          |     name          |
            |                              |                    +---------+---------+
            | 1                            | 1                            | 1
            |                              |                              |
            +---------------+--------------+------------------------------+
                            |
                            | N
                  +---------v---------+
                  |     employee      |
                  +-------------------+
                  | PK  id (UUID36)   |
                  |     nik           |
                  |     name          |
                  |     ...           |
                  | FK  site_id       |
                  | FK  position_id   |
                  | FK  composition_id|
                  +----+----------+---+
                       |          |
             +---------+          +-------------------------+
             | 1                                            | 1
             |                                              |
             | N                                            | N
+------------v-------------------+            +-------------v-------------------+
| default_employee_salary_comp   |            |         payroll_header          |
+--------------------------------+            +---------------------------------+
| PK  id (UUID36)                |            | PK  id (UUID36)                 |
| FK  employee_id (UUID36)       |            | FK  period_id (UUID36) -----------+--+
| FK  component_id (VARCHAR20) --+-----+      | FK  employee_id (UUID36)        |  |
|     amount                     |     |      |     total_income / deduction    |  |
+--------------------------------+     |      |     thp / created_at            |  |
                                       |      +---------------------+-----------+  |
                                       |                            | 1            |
                                       |                            |              |
                                       |                            | N            |
                                       |              +-------------v---+          |
                                       |              | payroll_details |          |
                                       |              +-----------------+          |
                                       |              | PK  id (UUID36) |          |
                                       |              | FK  header_id   |          |
                                       +------------->| FK  comp_id     |          |
                                       |              |     amount      |          |
                                       |              |     remarks     |          |
                                       |              +-----------------+          |
                                       |                                           |
                            +----------v----------+                      +---------v---------+
                            |  salary_components  |                      |  payroll_period   |
                            +---------------------+                      +-------------------+
                            | PK  id (VARCHAR20)  |                      | PK  id (UUID36)   |
                            |     name            |                      |     period_name   |
                            |     type            |                      |     start/end_date|
                            |     description     |                      |     is_closed     |
                            +---------------------+                      +-------------------+

```

---

### 2. Gambaran Tabel & Contoh Isinya

#### **Tabel Master (`master.py`)**

##### **`site`**

| id (PK) | name |
| --- | --- |
| `S001` | HQ Gunung Tabur |
| `S002` | Camp Semurut |

##### **`positions`**

| id (PK) | name |
| --- | --- |
| `P001` | Staff IT & Komputer |
| `P002` | Koordinator IT |

##### **`compositions`**

| id (PK) | name |
| --- | --- | --- |
| `TK/0` | Tidak Kawin, 0 Tanggungan |
| `TK/1` | Tidak Kawin, 1 Tanggungan |

##### **`salary_components`**

| id (PK) | name | type | description |
| --- | --- | --- | --- |
| `FI001` | Gaji Pokok | INCOME | Gaji pokok bulanan |
| `VI001` | Lembur | INCOME | Uang lembur harian/jam |
| `FD001` | Potongan BPJS | DEDUCTION | Potongan BPJS Kesehatan |

##### **`employee`**

| id (PK) | nik | name | site_id (FK) | position_id (FK) | composition_id (FK) |
| --- | --- | --- | --- | --- | --- |
| `emp-uuid-001` | `242002` | Julian Oriztia | `S001` | `P002` | `C001` |
| `emp-uuid-002` | `K252050` | Restu Ardananto | `S001` | `P001` | `C001` |

---

#### **Tabel Transaksi (`transactions.py`)**

##### **`default_employee_salary_component`** *(Gaji Standar per Karyawan)*

| id (PK) | employee_id (FK) | component_id (FK) | amount |
| --- | --- | --- | --- |
| `def-001` | `emp-uuid-001` | `FI001` | 5000000.00 |
| `def-002` | `emp-uuid-001` | `FD001` | 150000.00 |

##### **`payroll_period`** *(Periode Buku Gaji)*

| id (PK) | period_name | start_date | end_date | is_closed |
| --- | --- | --- | --- | --- |
| `period-oct-26` | Oktober 2026 | 2026-10-01 | 2026-10-31 | 0 |

##### **`payroll_header`** *(Slip Gaji / Rekap Gaji per Karyawan)*

| id (PK) | period_id (FK) | employee_id (FK) | total_income | total_deduction | thp | created_at |
| --- | --- | --- | --- | --- | --- | --- |
| `pay-hdr-001` | `period-oct-26` | `emp-uuid-001` | 5500000.00 | 150000.00 | 5350000.00 | 2026-10-04 15:42:00 |

##### **`payroll_details`** *(Rincian Item Komponen Slip Gaji)*

| id (PK) | payroll_header_id (FK) | component_id (FK) | amount | remarks |
| --- | --- | --- | --- | --- |
| `dtl-001` | `pay-hdr-001` | `FI001` | 5000000.00 | Gaji Pokok Oktober |
| `dtl-002` | `pay-hdr-001` | `VI001` | 500000.00 | Lembur 10 jam |
| `dtl-003` | `pay-hdr-001` | `FD001` | 150000.00 | BPJS Kesehatan |

---

### 3. Penjelasan Kardinalitas & Relasi Tabel

1. **One-to-Many (`1 : N`) Master ke Karyawan:**
* **`Site` $\rightarrow$ `Employee**`: 1 Lokasi/Site bisa ditempati banyak karyawan.
* **`Positions` $\rightarrow$ `Employee**`: 1 Jabatan bisa dimiliki banyak karyawan.
* **`Compositions` $\rightarrow$ `Employee**`: 1 Komposisi/Departemen memiliki banyak karyawan.


2. **Gaji Bawaan Karyawan:**
* **`Employee` $\leftrightarrow$ `DefaultEmployeeSalaryComponent` $\leftrightarrow$ `SalaryComponents**`: Menghubungkan karyawan dengan komponen gaji dasarnya (seperti Gaji Pokok / Potongan Rutin) beserta nominal standarnya.


3. **Proses Penggajian (Payroll Transaction):**
* **`PayrollPeriod` $\rightarrow$ `PayrollHeader` (`1 : N`)**: Dalam 1 periode penggajian (misal: *Oktober 2026*), dibuat banyak slip/header gaji untuk seluruh karyawan.
* **`Employee` $\rightarrow$ `PayrollHeader` (`1 : N`)**: 1 Karyawan memiliki rekap penggajian di setiap periodenya.
* **`PayrollHeader` $\rightarrow$ `PayrollDetails` (`1 : N`)**: 1 Header slip gaji memiliki banyak baris rincian pendapatan/potongan.
* **`SalaryComponents` $\rightarrow$ `PayrollDetails` (`1 : N`)**: Setiap baris rincian gaji menginduk pada master komponen gaji terkait.