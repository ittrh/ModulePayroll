Berikut adalah gambaran grafis diagram ERD, contoh isi sampel data, serta penjelasan relasi antartabel berdasarkan struktur terbaru dari model `masters.py` dan `transactions.py` Anda.

---

### 1. Visualisasi Diagram Relasi Tabel (ERD)

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
                              +---------------------+

   [ TABEL MASTER ATURAN / REGULASI (STANDALONE / LOOKUP SERVICE) ]
   +------------------------+  +---------------------------+  +-------------------+
   |  bpjs_kesehatan_rules  |  | bpjs_tenaga_kerja_rules   |  |   tax_tar_rules   |
   +------------------------+  +---------------------------+  +-------------------+
   | PK id (VARCHAR20)      |  | PK id (VARCHAR20)         |  | PK id (VARCHAR20) |
   |    batas_max_upah      |  |    batas_max_upah         |  |    kategori       |
   |    batas_min_upah      |  |    jkk (DECIMAL 5,4)      |  |    bruto_min      |
   |    ditanggung_pemberi  |  |    jkm (DECIMAL 5,4)      |  |    bruto_max      |
   |    ditanggung_pekerja  |  |    jht_pemberi / pekerja  |  |    tarif (DECIMAL)|
   +------------------------+  |    jp_pemberi / pekerja   |  |    composition_acc|
                               +---------------------------+  +-------------------+

```

---

### 2. Gambaran Tabel & Contoh Isinya

#### **A. Tabel Master (`masters.py`)**

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

##### **`employee`**

| id (PK) | nik | name | composition | bpjs_tk_active | bpjs_kes_active | tax_active | site_id (FK) | position_id (FK) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `emp-uuid-001` | `242002` | Julian Oriztia | `SKR` | `1` | `1` | `1` | `S001` | `P002` |
| `emp-uuid-002` | `K252050` | Restu Ardananto | `SKR` | `1` | `1` | `1` | `S001` | `P001` |

##### **`salary_components`**

| id (PK) | name | type | formula | description |
| --- | --- | --- | --- | --- |
| `FI001` | Gaji Pokok | `INCOME` | `None` | Gaji pokok bulanan |
| `VI001` | Lembur 1.5x | `INCOME` | `(gaji_pokok / 173) * 1.5` | Uang lembur jam pertama |
| `FD001` | BPJS Kes | `DEDUCTION` | `CALC_BPJS_KES` | Potongan BPJS Kesehatan 1% |
| `FD002` | PPh 21 TER | `DEDUCTION` | `CALC_TER` | Potongan Pajak PPh21 TER |

##### **`bpjs_kesehatan_rules`** *(Desimal 5,4 untuk Persentase)*

| id (PK) | batas_max_upah | batas_min_upah | ditanggung_pemberi_kerja | ditanggung_tenaga_kerja |
| --- | --- | --- | --- | --- |
| `KES2026` | 12000000.00 | 3383928.00 | `0.0400` *(4%)* | `0.0100` *(1%)* |

##### **`bpjs_tenaga_kerja_rules`** *(Desimal 5,4 untuk Persentase)*

| id (PK) | batas_max_upah | jaminan_kecelakaan_kerja | jaminan_kematian | jht_ditanggung_pemberi_kerja | jht_ditanggung_tenaga_kerja | jp_ditanggung_pemberi_kerja | jp_ditanggung_tenaga_kerja |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TK2026` | 10042300.00 | `0.0024` *(0.24%)* | `0.0030` *(0.30%)* | `0.0370` *(3.7%)* | `0.0200` *(2.0%)* | `0.0200` *(2.0%)* | `0.0100` *(1.0%)* |

##### **`tax_tar_rules`** *(Lengkap dengan JSON `composition_accept`)*

| id (PK) | kategori | bruto_min | bruto_max | tarif | composition_accept (JSON) |
| --- | --- | --- | --- | --- | --- |
| `TER_A_01` | `A` | 0.00 | 5400000.00 | `0.0000` *(0%)* | `["SKR", "OPR", "DIR"]` |
| `TER_A_02` | `A` | 5400001.00 | 5650000.00 | `0.0025` *(0.25%)* | `["SKR", "OPR"]` |

---

#### **B. Tabel Transaksi (`transactions.py`)**

##### **`default_employee_salary_component`** *(Gaji Standar per Karyawan)*

| id (PK) | employee_id (FK) | component_id (FK) | amount |
| --- | --- | --- | --- |
| `def-001` | `emp-uuid-001` | `FI001` | 5000000.00 |

##### **`payroll_period`** *(Periode Penggajian)*

| id (PK) | period_name | start_date | end_date | is_closed |
| --- | --- | --- | --- | --- |
| `prd-oct-2026` | Oktober 2026 | 2026-10-01 | 2026-10-31 | 0 |

##### **`payroll_header`** *(Slip Gaji Header)*

| id (PK) | period_id (FK) | employee_id (FK) | total_income | total_deduction | thp | created_at | context (JSON) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay-hdr-001` | `prd-oct-2026` | `emp-uuid-001` | 5500000.00 | 200000.00 | 5300000.00 | 2026-10-05 15:08:00 | `{"ter_category": "A", "marital_status": "K/0", "tax_rate": 0.0025}` |

##### **`payroll_details`** *(Rincian Komponen Slip Gaji)*

| id (PK) | payroll_header_id (FK) | component_id (FK) | amount | remarks |
| --- | --- | --- | --- | --- |
| `dtl-001` | `pay-hdr-001` | `FI001` | 5000000.00 | Gaji Pokok Oktober |
| `dtl-002` | `pay-hdr-001` | `VI001` | 500000.00 | Lembur 10 jam |
| `dtl-003` | `pay-hdr-001` | `FD001` | 50000.00 | BPJS Kesehatan (1%) |
| `dtl-004` | `pay-hdr-001` | `FD002` | 150000.00 | PPh21 TER (0.25%) |

---

### 3. Penjelasan Relasi & Perubahan Penting

1. **Struktur `DECIMAL(5, 4)` pada Rules Regulasi:**
* Penggunaan tipe data `DECIMAL(5, 4)` sangat tepat untuk menyimpan rate persentase akurat (misal: `0.0025` untuk `0.25%`, `0.0400` untuk `4%`) sehingga menghindari rounding error saat pemrosesan gaji di Python.


2. **Kesesuaian `composition_accept` (JSON) pada `TaxTarRules`:**
* Fitur kolom `JSON` ini memungkinkan pencocokan kategori TER PPh 21 tidak hanya berdasarkan penghasilan bruto, tetapi juga memvalidasi apakah kode komposisi karyawan (`Employee.composition`) berhak atau cocok dengan aturan tarif pajak tersebut.


3. **Penyimpanan Snapshot via `PayrollHeader.context` (JSON):**
* Saat transaksi diproses, detail historis (seperti status PTKP, rate pajak yang digunakan, atau parameter kalkulasi) disimpan ke dalam kolom `context` berbentuk JSON. Hal ini membuat data historis slip gaji tetap aman dan dapat diverifikasi kapan pun meskipun aturan regulasi berubah di kemudian hari.