### Tahap 1: Pengelolaan Master Independen (Standar CRUD)

Mulai dari fitur CRUD untuk tabel-tabel master yang tidak membutuhkan Foreign Key (FK) dari tabel lain.

1. **CRUD Site & Positions:**
* Modul input master lokasi kerja (`site`) dan jabatan (`positions`).




2. **CRUD Rules:**
* Fitur penyusunan/pengaturan JSON aturan regulasi (BPJS, PPh21 TER, Uang Makan).




3. **CRUD Salary Components:**
* Fitur input nama komponen gaji (misal: *Gaji Pokok*, *Lembur*, *BPJS*) dan menghubungkannya dengan `rules_id` jika ada.





---

### Tahap 2: Pengelolaan Data Karyawan & Setting Standar

Setelah tabel dasar siap, lanjut ke entitas karyawan dan pemetaan komponen gajinya.

1. **CRUD Employee:**
* Fitur pendataan karyawan dengan dropdown pilihan `site_id` dan `position_id`.


* Menyimpan atribut seperti `composition`, `bpjs_tk_active`, `bpjs_kes_active`, dan `tax_active`.




2. **Setup Default Salary Component per Karyawan (`default_employee_salary_component`):**
* Fitur untuk menetapkan besaran nominal komponen tetap (seperti *Gaji Pokok*) untuk masing-masing karyawan.





---

### Tahap 3: Modul Penggalan Periode & Engine Payroll (Core Engine)

Ini adalah inti dari aplikasi penggajian.

1. **Manajemen Periode Penggajian (`payroll_period`):**
* Fitur untuk membuat periode penggajian baru (misal: *Oktober 2026*) serta mengubah status buka/tutup buku (`is_closed`).




2. **Engine / Service Kalkulasi Gaji (Paling Krusial):**
* Fungsi Python yang bertugas membaca `context` inputan (seperti *jumlah lembur*, *kehadiran*).


* Menghitung nilai tiap `salary_components` berdasarkan `formula` atau aturan dari `rules` (JSON).


* Menghitung total `total_income`, `total_deduction`, dan `thp`.





---

### Tahap 4: Eksekusi & Detail Transaksi Payroll

1. **Proses Hitung & Simpan Slip Gaji (`payroll_header` & `payroll_details`):**
* Menyimpan hasil kalkulasi ke `payroll_header`.


* Menyimpan rincian tiap komponen ke `payroll_details` secara kolektif.




2. **Fitur Cetak & Preview Slip Gaji:**
* Menampilkan UI slip gaji / rekap penggajian berbasis gabungan data `payroll_header` dan `payroll_details`.





---

### Ringkasan Urutan Coding

```text
1. Master Dasar (Site, Position, Rules, SalaryComponents)
   ↓
2. Master Karyawan (Employee)
   ↓
3. Mapping Gaji Bawaan (DefaultEmployeeSalaryComponent)
   ↓
4. Periode Penggajian (PayrollPeriod)
   ↓
5. Logic Engine Calculations & Transaksi (PayrollHeader & PayrollDetails)
   ↓
6. UI Slip Gaji / Reporting

```