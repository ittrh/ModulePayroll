

### 1. Struktur Layout Utama (Main Window)

Aplikasi menggunakan layout **Sidebar Navigation** di sebelah kiri dan **Workspace Area** di sebelah kanan.

```text
+-----------------------------------------------------------------------------------------------+
|  APP HEADER: LOGO TRH  |  Payroll Management System v1.0                     [ User: Julian ] |
+------------------------+----------------------------------------------------------------------+
|  SIDEBAR MENU          |  MAIN WORKSPACE AREA                                                 |
|                        |                                                                      |
|  [D] Dashboard         |  +----------------------------------------------------------------+  |
|                        |  | BREADCRUMB: Master > Karyawan                                  |  |
|  MASTER DATA           |  +----------------------------------------------------------------+  |
|  - Site & Designation  |  | ACTION BAR:                                                    |  |
|  - Rules / Regulasi    |  | [ + Tambah Karyawan ]  [ Export Excel ]     Search: [________] |  |
|  - Komponen Gaji       |  +----------------------------------------------------------------+  |
|  - Data Karyawan       |  | TABLE VIEW:                                                    |  |
|                        |  | +--------+-----------------+------+-----------+--------------+ |  |
|  TRANSAKSI             |  | | NIK    | Nama            | Site | Komposisi | Action       | |  |
|  - Gaji Standar        |  | +--------+-----------------+------+-----------+--------------+ |  |
|  - Periode Penggajian  |  | | 242002 | Julian Oriztia  | S001 | SKR       | [Edit] [Del] | |  |
|  - Hitung Gaji (Run)   |  | | K252050| Restu Ardananto | S001 | SKR       | [Edit] [Del] | |  |
|                        |  | +--------+-----------------+------+-----------+--------------+ |  |
|  LAPORAN               |  +----------------------------------------------------------------+  |
|  - Rekap & Slip Gaji   |  | PAGINATION: < 1 2 3 >                          Total: 2 Karyawan  |  |
+------------------------+----------------------------------------------------------------------+

```

---

### 2. Tampilan Form Modul Utama

#### **A. Modul Master Rules (`Rules` / `JSON`)**

Modul ini menyajikan form dinamis untuk mengubah parameter JSON regulasi.

```text
+-----------------------------------------------------------------------------------------------+
|  MASTER ATURAN / REGULASI (RULES)                                                             |
+-----------------------------------------------------------------------------------------------+
|  Pilih Aturan: [ R_MEAL - Rules Uang Makan            v ]                                     |
|                                                                                               |
|  Nama Aturan  : [ Rules Uang Makan                         ]                                  |
|  ID Aturan    : R_MEAL                                                                        |
|                                                                                               |
|  Konfigurasi JSON (Dinamis):                                                                  |
|  +-----------------------------------------------------------------------------------------+  |
|  | {                                                                                       |  |
|  |   "rate_per_day": 50000,                                                                |  |
|  |   "composition_rates": { "SKR": 50000, "OPR": 65000 },                                  |  |
|  |   "extra_overtime_rate": 20000                                                          |  |
|  | }                                                                                       |  |
|  +-----------------------------------------------------------------------------------------+  |
|                                                                                               |
|  [ Simpan Konfigurasi ]  [ Batal ]                                                            |
+-----------------------------------------------------------------------------------------------+

```

---

#### **B. Modul Transaksi Hitung Gaji (`Payroll Processing`)**

Layar eksekusi kalkulasi gaji per periode berbasis tabel `PayrollHeader` & `PayrollDetails`.

```text
+-----------------------------------------------------------------------------------------------+
|  PROSES PENGGAJIAN (PAYROLL RUN)                                                              |
+-----------------------------------------------------------------------------------------------+
|  Periode Penggajian: [ Oktober 2026 (01/10/2026 - 31/10/2026) v ]   Status: OPEN               |
|                                                                                               |
|  +-----------------------------------------------------------------------------------------+  |
|  | FILTER & HITUNG MASSAL                                                                  |  |
|  | Unit/Site: [ Semua Site v ]   Komposisi: [ Semua v ]   [ > PROSES KALKULASI GAJI ]      |  |
|  +-----------------------------------------------------------------------------------------+  |
|                                                                                               |
|  HASIL PRATINJAU HITUNGAN:                                                                    |
|  +--------+-----------------+--------------+-----------------+-----------------+------------+ |
|  | NIK    | Nama Karyawan   | Total Income | Total Deduction | Take Home Pay   | Status     | |
|  +--------+-----------------+--------------+-----------------+-----------------+------------+ |
|  | 242002 | Julian Oriztia  | Rp 5.500.000 | Rp   162.500    | Rp 5.337.500    | [ Detil ]  | |
|  | K252050| Restu Ardananto | Rp 4.800.000 | Rp   120.000    | Rp 4.680.000    | [ Detil ]  | |
|  +--------+-----------------+--------------+-----------------+-----------------+------------+ |
|                                                                                               |
|  [ SIMPAN TRANSAKSI & KUNCI PERIODE ]                                                        |
+-----------------------------------------------------------------------------------------------+

```

---

#### **C. Modal Pratinjau Slip Gaji (`PayrollDetails` Viewer)**

Pop-up/Modal dialog saat tombol `[ Detil ]` diklik.

```text
+-----------------------------------------------------------------------------------------------+
|  DETAIL SLIP GAJI - JULIAN ORIZTIA (NIK: 242002)                                          [X] |
+-----------------------------------------------------------------------------------------------+
|  Periode: Oktober 2026 | Site: HQ Gunung Tabur | Jabatan: Koordinator IT                       |
+-----------------------------------------------------------------------------------------------+
|  PENDAPATAN (INCOME)                        | POTONGAN (DEDUCTION)                            |
|  +----------------------------+-----------+ | +----------------------------+-----------+    |
|  | Komponen                   | Jumlah    | | | Komponen                   | Jumlah    |    |
|  +----------------------------+-----------+ | +----------------------------+-----------+    |
|  | Gaji Pokok                 | 5.000.000 | | | BPJS Kesehatan (1%)        |    50.000 |    |
|  | Lembur (10 Jam)            |   500.000 | | | PPh 21 TER (0.25%)        |   112.500 |    |
|  +----------------------------+-----------+ | +----------------------------+-----------+    |
|  | TOTAL PENDAPATAN           | 5.500.000 | | | TOTAL POTONGAN             |   162.500 |    |
|  +----------------------------+-----------+ | +----------------------------+-----------+    |
+-----------------------------------------------------------------------------------------------+
|  TAKE HOME PAY (THP) : Rp 5.337.500                                                        |
|  Context JSON Snapshot: {"TER_Category": "A", "Gaji Pokok": 5000000, "Lembur Jam": 10}        |
+-----------------------------------------------------------------------------------------------+
|  [ Cetak PDF ]  [ Tutup ]                                                                     |
+-----------------------------------------------------------------------------------------------+

```

---

### 3. Palet Warna & Styling QSS Recommended

Untuk aplikasi PySide6 bertema profesional/industrial:

* **Primary Color (Header/Active):** Deep Navy (`#1E293B`)
* **Accent Color (Button Primary):** Ocean Blue (`#0284C7`)
* **Background Area:** Slate Light (`#F8FAFC`)
* **Card/Table Background:** Pure White (`#FFFFFF`)
* **Text Main:** Dark Gray (`#0F172A`)
* **Status Active/Open:** Emerald Green (`#10B981`)

Rancangan UI ini sangat sesuai dengan arsitektur **Model/View PySide6 (`QTableView` & `QStandardItemModel`)** serta memfasilitasi penggunaan `QStyledItemDelegate` untuk editing data secara langsung.