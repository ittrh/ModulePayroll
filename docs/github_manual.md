…or create a new repository on the command line
echo "# ModulePayroll" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ittrh/ModulePayroll.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/ittrh/ModulePayroll.git
git branch -M main
git push -u origin main

# Panduan Lengkap Penggunaan GitHub: Dari Konsep Dasar hingga Push & Pull

Buku manual ini dirancang untuk memandu Anda memahami dan menguasai alur kerja Git dan GitHub. Seluruh materi disusun secara mendasar, jelas, dan dapat langsung dipraktikkan.

---

## 1. Konsep Dasar Git & GitHub

Sebelum masuk ke perintah, penting untuk memahami perbedaan dasar antara Git dan GitHub:

* **Git**: Sistem pengontrol versi (*Version Control System* - VCS) lokal yang berjalan di komputer Anda. Git mencatat setiap perubahan kode yang Anda buat.
* **GitHub**: Layanan *cloud host* untuk menyimpan *repository* Git secara online. GitHub memudahkan kolaborasi antar pengembang.

### Alur Kerja 3 Area Git

Di lokal komputer Anda, Git membagi berkas ke dalam 3 area utama:

1. **Working Directory**: Area tempat Anda membuat, mengedit, atau menghapus berkas.
2. **Staging Area (Index)**: Area penampungan sementara untuk memilih perubahan mana yang siap disimpan.
3. **Local Repository (.git)**: Tempat penyimpanan permanen dari histori perubahan di komputer Anda setelah di-*commit*.

---

## 2. Persiapan & Konfigurasi Awal

### Langkah 1: Pengaturan Identitas Git

Setelah menginstal Git, jalankan perintah berikut di Terminal atau Command Prompt untuk mendaftarkan nama dan email Anda. Identitas ini akan dicatat pada setiap *commit*.

```bash
git config --global user.name "Nama Anda"
git config --global user.email "emailanda@example.com"

```

### Langkah 2: Menghubungkan ke GitHub (Autentikasi SSH / PAT)

Karena GitHub tidak lagi mendukung autentikasi kata sandi biasa via CLI, gunakan **Personal Access Token (PAT)** atau **SSH Key**.

* **Menggunakan Personal Access Token (PAT)**:
1. Buka GitHub $\rightarrow$ **Settings** $\rightarrow$ **Developer Settings** $\rightarrow$ **Personal Access Tokens** $\rightarrow$ **Tokens (classic)**.
2. Klik **Generate new token**, beri izin akses repo (centang `repo`), lalu salin token tersebut.
3. Token ini berfungsi sebagai kata sandi saat diminta autentikasi di CLI.



---

## 3. Menghubungkan Projek Lokal ke GitHub

Ada dua skenario umum dalam memulai proyek:

### Skenario A: Memulai dari Lokal (Project Baru)

1. **Inisialisasi Repository Lokal:**
Masuk ke folder projek Anda melalui terminal, lalu jalankan perintah inisialisasi Git:

```bash
cd /path/ke/folder/projek
git init

```


2. **Buat Repository di GitHub:**
1. Buka [GitHub](https://github.com) dan buat repository baru (klik ikon **+** di pojok kanan atas $\rightarrow$ **New repository**).
2. Isi nama repository (misal: `projek-utama`). Jangan centang *Initialize with README* jika ingin menghubungkan projek yang sudah ada.


3. **Hubungkan Remote Repository:**
Tambahkan URL repository GitHub sebagai tujuan remote dengan nama `origin`:

```bash
git remote add origin https://github.com/username/projek-utama.git

```


4. **Ubah Nama Branch Utama:**
Pastikan nama branch utama adalah `main`:

```bash
git branch -M main

```


### Skenario B: Mengunduh Repository yang Sudah Ada di GitHub (Clone)

Jika projek sudah ada di GitHub dan Anda ingin menyalinnya ke lokal:

```bash
git clone https://github.com/username/projek-utama.git
cd projek-utama

```

---

## 4. Alur Kerja Utama: Mengubah, Saving, dan Push

Bagian ini menjelaskan alur kerja sehari-hari dari penulisan kode hingga mengunggahnya ke GitHub.

### Step 1: Memeriksa Status Berkas (`git status`)

Gunakan perintah ini setiap kali Anda ingin melihat berkas apa saja yang telah diubah, ditambahkan, atau dihapus:

```bash
git status

```

### Step 2: Memindahkan ke Staging Area (`git add`)

Menandai berkas yang akan dimasukkan ke dalam *snapshot* berikutnya.

* Menambahkan satu berkas spesifik:
```bash
git add nama_berkas.py

```


* Menambahkan seluruh perubahan dalam folder:
```bash
git add .

```



### Step 3: Menyimpan Perubahan Lokal (`git commit`)

*Commit* menyimpan perubahan dari Staging Area ke Local Repository beserta pesan penjelas.

```bash
git commit -m "Deskripsi perubahan yang singkat dan jelas"

```

> **Tips Pesan Commit**: Gunakan kalimat imperatif, contoh: `"Tambah fitur login"` atau `"Perbaiki bug validasi formulir"`.

### Step 4: Mengunggah ke GitHub (`git push`)

*Push* mengirimkan seluruh *commit* dari Local Repository ke Remote Repository (GitHub).

* **Push Pertama Kali** (mensejajarkan branch lokal dan remote):
```bash
git push -u origin main

```


* **Push Selanjutnya**:
```bash
git push

```



---

## 5. Alur Kerja Mengambil Perubahan: Fetch & Pull

Ketika bekerja dalam tim atau pada komputer berbeda, kode di GitHub mungkin lebih baru daripada kode di komputer lokal Anda.

```
+-------------------------------------------------------------+
|                      REMOTE (GitHub)                        |
+-------------------------------------------------------------+
               |                               |
        (git fetch)                        (git pull)
               |                               |
               v                               v
+-----------------------------+  merge  +---------------------+
| Local Remote-Tracking Branch| ------->|   Working Directory |
|      (origin/main)          |         |       (Lokal)       |
+-----------------------------+         +---------------------+

```

### Penjelasan `git fetch`

`git fetch` hanya mengunduh data dan riwayat komit terbaru dari GitHub ke repository lokal Anda, **tanpa menggabungkan (merge)** perubahan tersebut ke berkas yang sedang Anda kerjakan. Perintah ini aman digunakan untuk memeriksa pembaruan tanpa merusak kode lokal.

```bash
git fetch origin

```

### Penjelasan `git pull`

`git pull` mengunduh data sekaligus **secara otomatis menggabungkan (merge)** perubahan dari GitHub langsung ke Working Directory lokal Anda.

```bash
git pull origin main

```

> **Rumus Dasar**: `git pull` = `git fetch` + `git merge`

---

## 6. Penanganan Konflik (Merge Conflict)

Konflik terjadi ketika Anda dan rekan tim mengubah baris kode yang sama pada berkas yang sama, lalu mencoba menggabungkannya.

### Alur Penyelesaian Konflik:

1. Jalankan `git pull`. Jika terjadi konflik, Git akan memberikan peringatan di terminal.
2. Buka berkas yang mengalami konflik. Anda akan melihat penanda khusus dari Git:
```text
<<<<<<< HEAD
Kode milik Anda di komputer lokal
=======
Kode baru yang diunduh dari GitHub
>>>>>>> main

```


3. **Lakukan Edit**: Hapus penanda `<<<<<<<`, `=======`, dan `>>>>>>>`. Pilih baris kode mana yang benar atau gabungkan keduanya secara manual.
4. Simpan berkas tersebut.
5. Selesaikan proses merge melalui terminal:

```bash
git add berkas_terkait.py
git commit -m "Penyelesaian merge conflict"
git push

```

---

## 7. Rangkuman Perintah Sering Digunakan (Cheatsheet)

| Perintah | Fungsi / Kegunaan |
| --- | --- |
| `git init` | Membuat repository Git baru di folder lokal |
| `git clone <url>` | Menduplikasi repository dari GitHub ke lokal |
| `git status` | Memeriksa kondisi berkas di Working Directory & Staging Area |
| `git add .` | Memindahkan seluruh perubahan ke Staging Area |
| `git commit -m "pesan"` | Menyimpan permanen snapshot perubahan di repository lokal |
| `git push origin main` | Mengirimkan *commit* dari lokal ke branch main di GitHub |
| `git fetch` | Memeriksa dan mengambil update dari GitHub tanpa merge |
| `git pull` | Mengambil update dari GitHub dan langsung melakukan merge |
| `git log --oneline` | Melihat riwayat *commit* secara ringkas |