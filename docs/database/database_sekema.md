### Grafis Diagram Relasi Tabel (ERD)

```text
       +-------------------+               +-------------------+
       |       site        |               |     positions     |
       +-------------------+               +-------------------+
       | PK  id (String10) |               | PK  id (String10) |
       |     name          |               |     name          |
       +---------+---------+               +---------+---------+
                 |                                   |
                 | 1                                 | 1
                 |                                   |
                 +-------------------+---------------+
                                     |
                                     | N
                           +---------v---------+
                           |     employee      |
                           +-------------------+
                           | PK  id (UUID36)   |
                           |     nik           |
                           |     name          |
                           |     composition   |
                           |     bpjs_tk_active|
                           |     bpjs_kes_active
                           |     tax_active    |
                           |     ...           |
                           | FK  site_id       |
                           | FK  position_id   |
                           +----+----------+---+
                                |          |
                      +---------+          +-------------------------+
                      | 1                                            | 1
                      |                                              |
                      | N                                            | N
  +-------------------v------------+            +--------------------v------------+
  | default_employee_salary_comp   |            |         payroll_header          |
  +--------------------------------+            +---------------------------------+
  | PK  id (UUID36)                |            | PK  id (UUID36)                 |
  | FK  employee_id (UUID36)       |            | FK  period_id (UUID36) -----------+--+
  | FK  component_id (VARCHAR20) --+-----+      | FK  employee_id (UUID36)        |  |
  |     amount                     |     |      |     total_income / deduction    |  |
  +--------------------------------+     |      |     thp / created_at / context  |  |
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
                              |     formula         |                      |     is_closed     |
                              |     description     |                      +-------------------+
                              | FK  rules_id        |
                              +----------+----------+
                                         | N
                                         |
                                         | 1 (Opsional / Dynamic Lookup)
                              +----------v----------+
                              |        rules        |
                              +---------------------+
                              | PK  id (String25)   |
                              |     name            |
                              |     config (JSON)   |
                              +---------------------+

```

---

### Contoh Tabel beserta Isinya

#### **A. Tabel Master (`master.py`)**

##### **`rules`** *(Satu Tabel Master untuk Semua Regulasi)*

| id (PK) | name | config (JSON) |
| --- | --- | --- |
| `R_BPJS_KES` | BPJS Kesehatan | `{"batas_max": 12000000, "batas_min": 3383928, "pemberi_kerja": 0.04, "pekerja": 0.01}` |
| `R_BPJS_TK` | BPJS Ketenagakerjaan | `{"batas_max": 10042300, "jkk": 0.0024, "jkm": 0.0030, "jht_pemberi": 0.037, "jht_pekerja": 0.02}` |
| `R_TAX_TER` | PPh 21 TER | `{"category": "A", "min": 0, "max": 5400000, "rate": 0.0, "min": 5400001, "max": 5650000, "rate": 0.0025}` |
| `R_MEAL` | Rules Uang Makan | `{"rate_per_day": 50000, "extra_overtime_rate": 20000}` |

##### **`site`** & **`positions`**

| id (PK) | name |
| --- | --- |
| `S001` | HQ Gunung Tabur |
| `S002` | Camp Semurut |

| id (PK) | name |
| --- | --- |
| `P001` | Staff IT & Komputer |
| `P002` | Koordinator IT |

##### **`employee`**

| id (PK) | nik | name | composition | bpjs_tk_active | bpjs_kes_active | tax_active | site_id (FK) | position_id (FK) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `emp-uuid-001` | `242002` | Julian Oriztia | `SKR` | `1` | `1` | `1` | `S001` | `P002` |
| `emp-uuid-002` | `K252050` | Restu Ardananto | `SKR` | `1` | `1` | `1` | `S001` | `P001` |

##### **`salary_components`**

| id (PK) | name | type | formula | rules_id (FK) | description |
| --- | --- | --- | --- | --- | --- |
| `FI001` | Gaji Pokok | `INCOME` | `None` | `None` | Gaji pokok bulanan |
| `VI001` | Lembur | `INCOME` | `(gaji_pokok / 173) * jam` | `None` | Lembur harian/jam |
| `FD001` | BPJS Kes | `DEDUCTION` | `CALC_BPJS_KES` | `R_BPJS_KES` | Potongan BPJS Kesehatan |
| `FD002` | PPh 21 TER | `DEDUCTION` | `CALC_TAX_TER` | `R_TAX_TER` | Potongan PPh21 TER |

---

#### **B. Tabel Transaksi (`transaction.py`)**

##### **`default_employee_salary_component`**

| id (PK) | employee_id (FK) | component_id (FK) | amount |
| --- | --- | --- | --- |
| `def-001` | `emp-uuid-001` | `FI001` | 5000000.00 |

##### **`payroll_period`**

| id (PK) | period_name | start_date | end_date | is_closed |
| --- | --- | --- | --- | --- |
| `prd-oct-2026` | Oktober 2026 | 2026-10-01 | 2026-10-31 | 0 |

##### **`payroll_header`**

| id (PK) | period_id (FK) | employee_id (FK) | total_income | total_deduction | thp | created_at | context (JSON) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay-hdr-001` | `prd-oct-2026` | `emp-uuid-001` | 5500000.00 | 162500.00 | 5337500.00 | 2026-10-06 09:00:00 | `{"Gaji Pokok": 5000000, "Lembur Jam": 10, "Tarif Pajak": 0.0025, "TER_Category": "A"}` |

##### **`payroll_details`**

| id (PK) | payroll_header_id (FK) | component_id (FK) | amount | remarks |
| --- | --- | --- | --- | --- |
| `dtl-001` | `pay-hdr-001` | `FI001` | 5000000.00 | Gaji Pokok Oktober |
| `dtl-002` | `pay-hdr-001` | `VI001` | 500000.00 | Uang Lembur (10 Jam) |
| `dtl-003` | `pay-hdr-001` | `FD001` | 50000.00 | Potongan BPJS Kes (1%) |
| `dtl-004` | `pay-hdr-001` | `FD002` | 112500.00 | PPh21 TER (0.25%) |

---

### Penjelasan Relasi Antartabel

1. **Master Karyawan:**
* `Site` & `Positions` ke `Employee` (`1 : N`). Karyawan terikat pada 1 site dan 1 jabatan.


2. **Master Komponen & Rules:**
* `Rules` ke `SalaryComponents` (`1 : N`). Komponen gaji (seperti BPJS atau PPh21) dapat mengacu pada aturan tertentu yang disimpan di dalam tabel `Rules`.


3. **Standar Gaji & Transaksi:**
* `Employee` & `SalaryComponents` dihubungkan oleh `DefaultEmployeeSalaryComponent` untuk menentukan nominal default tiap karyawan.
* `PayrollPeriod` & `Employee` menjadi rujukan utama untuk `PayrollHeader` (`1 : N`).
* `PayrollHeader` memiliki banyak rincian di `PayrollDetails` (`1 : N`), di mana setiap baris rincian merujuk pada `SalaryComponents`.