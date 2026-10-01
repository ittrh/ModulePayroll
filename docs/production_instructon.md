Membuat installer untuk aplikasi Python melibatkan dua langkah utama: membungkus (bundling) kode Python menjadi file eksekutabel (`.exe`) dengan **PyInstaller**, lalu mengemasnya ke dalam installer profesional (seperti setup wizard) dengan **Inno Setup**.

Berikut adalah panduan langkah demi langkahnya.

---

### Langkah 1: Mengubah Skrip Python Menjadi `.exe` dengan PyInstaller

PyInstaller akan mengumpulkan kode Anda beserta dependensinya ke dalam satu folder atau satu file.

1.  **Instal PyInstaller:**
    Buka terminal/CMD dan jalankan:
    ```bash
    pip install pyinstaller
    ```

2.  **Buat File Executable:**
    Masuk ke folder proyek Anda di terminal, lalu jalankan perintah berikut:
    ```bash
    pyinstaller --noconsole --collect-all selenium --onefile --icon=docs/images/logo.ico bot.py
    ```
    * `--noconsole`: Tidak akan memunculkan jendela hitam (terminal) saat aplikasi dijalankan.
    * `--onefile`: Menggabungkan semua dependensi ke dalam satu file `.exe` saja.

3.  **Hasil:**
    Setelah proses selesai, cari file `.exe` Anda di folder `dist/`.

---

### Langkah 2: Membuat Installer dengan Inno Setup

Setelah memiliki file `.exe`, Anda memerlukan **Inno Setup** untuk membuat installer yang bisa diinstal pengguna dengan mudah.

1.  **Unduh & Instal:** Unduh [Inno Setup](https://jrsoftware.org/isdl.php) dan instal di komputer Anda.
2.  **Buka Inno Setup Compiler:** Pilih "Create a new script file using the Script Wizard".
3.  **Ikuti Wizard:**
    * **Application Information:** Masukkan nama aplikasi, versi, dan nama perusahaan Anda.
    * **Application Files:** * **Application main executable file:** Pilih file `.exe` yang Anda buat di folder `dist/` tadi.
        * **Other application files:** Jika aplikasi Anda membutuhkan file pendukung (seperti gambar, file konfigurasi, atau database), tambahkan di sini.
    * **Application Icons:** Anda bisa menambahkan shortcut di desktop atau menu Start.
    * **Setup Languages:** Pilih bahasa (misal: English).
    * **Compiler Settings:** Tentukan di mana folder installer akan disimpan (`Custom compiler output folder`) dan berikan nama file installer-nya (misal: `SetupAplikasi.exe`).
4.  **Selesaikan:** Klik "Finish". Jika ditanya untuk membuat *script*, pilih "Yes".

---

### Langkah 3: Menjalankan Kompilasi

Setelah wizard selesai, Inno Setup akan menampilkan kode *script* `.iss`. 

* Klik menu **Build** > **Compile**.
* Inno Setup akan membuat installer di folder output yang telah Anda tentukan.

Sekarang, Anda memiliki file `SetupAplikasi.exe` yang bisa Anda bagikan kepada pengguna untuk menginstal aplikasi Anda di Windows.


### Lokasi database setelah kompilasi ada di "C:\Users\IT\AppData\Local\DB_Automation_OrderSipuh"
---

**Tips Tambahan:**
* **Ukuran File:** Jika menggunakan `--onefile`, waktu buka aplikasi mungkin sedikit lebih lama karena file harus diekstrak ke folder temp terlebih dahulu.
* **Icon:** Anda bisa menambahkan opsi `--icon=logo.ico` pada perintah PyInstaller agar aplikasi memiliki ikon khusus.
* **Dependensi:** Pastikan Anda telah menginstal semua pustaka yang digunakan (seperti `pandas`, `requests`, dsb) di environment tempat Anda menjalankan PyInstaller agar terbaca oleh compiler.
