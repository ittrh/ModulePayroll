Buku manual ini dirancang sebagai panduan praktis dan referensi lengkap dalam merancang serta menerapkan **Qt Style Sheets (QSS)** pada aplikasi berbasis PySide6.

---

# Manual Penggunaan & Kamus QSS PySide6

## 1. Konsep Dasar & Sintaks QSS

Sintaks QSS terinspirasi langsung dari CSS web. Format dasarnya terdiri dari **Selector**, **Property**, dan **Value**.

```css
Selector {
    property-name: value;
}

```

### Metode Penerapan

1. **Aplikasi Global (`QApplication`):** Mempengaruhi seluruh komponen visual dalam aplikasi.
```python
app = QApplication(sys.argv)
app.setStyleSheet("QPushButton { color: red; }")

```


2. **Spesifik Widget (`QWidget`):** Hanya mempengaruhi widget tertentu dan anak-anaknya (*child widgets*).
```python
button.setStyleSheet("background-color: #2b2b2b; color: white;")

```


3. **Menggunakan File Eksternal `.qss` (Sangat Direkomendasikan):**
```python
def load_stylesheet(filename):
    with open(filename, "r") as f:
        return f.read()

app.setStyleSheet(load_stylesheet("style.qss"))

```



---

## 2. Hirarki & Tipe Selector

| Jenis Selector | Sintaks | Keterangan & Contoh |
| --- | --- | --- |
| **Universal** | `*` | Berlaku untuk seluruh widget. <br>

<br>`* { font-family: 'Segoe UI'; }` |
| **Type Selector** | `QWidgetClass` | Berlaku untuk instance kelas tersebut dan sub-kelasnya. <br>

<br>`QPushButton { background: blue; }` |
| **Class Selector** | `.QWidgetClass` | Hanya berlaku untuk instance kelas tepat, **tanpa** sub-kelasnya. <br>

<br>`.QPushButton { border: none; }` |
| **ID / Object Name** | `#objectName` | Menargetkan widget berdasarkan `setObjectName()`. <br>

<br>`#btnSubmit { background: green; }` |
| **Property Selector** | `[property="value"]` | Menargetkan widget berdasarkan atribut kustom/bawaan. <br>

<br>`QPushButton[active="true"] { color: yellow; }` |
| **Descendant** | `QFrame QPushButton` | Menargetkan `QPushButton` di dalam `QFrame` (level mana saja). |
| **Direct Child** | `QFrame > QPushButton` | Menargetkan `QPushButton` yang merupakan anak langsung dari `QFrame`. |

---

## 3. Pseudo-States (Kondisi Interaktif Widget)

Pseudo-states digunakan untuk merespons interaksi pengguna seperti *hover*, klik, atau kondisi status widget (*checked*, *disabled*).

* **`:hover`** – Cursor berada di atas widget.
* **`:pressed`** – Widget sedang diklik/ditekan.
* **`:checked`** – Widget (tombol, checkbox, radio) dalam kondisi aktif/terpilih.
* **`:unchecked`** – Widget dalam kondisi tidak terpilih.
* **`:disabled`** – Widget dalam keadaan tidak aktif (`setEnabled(False)`).
* **`:focus`** – Widget sedang menerima fokus input (misal: cursor aktif di LineEdit).
* **`:on` / `:off**` – Digunakan pada status spesifik (misal: menu item atau indicator).
* **`:open` / `:closed**` – Kondisi menu, combobox, atau tree view item.

```css
QPushButton {
    background-color: #007acc;
    color: white;
}
QPushButton:hover {
    background-color: #0098ff;
}
QPushButton:pressed {
    background-color: #005999;
}
QPushButton:disabled {
    background-color: #444444;
    color: #888888;
}

```

---

## 4. Sub-Controls (Komponen Internal Widget)

Banyak widget kompleks PySide6 terdiri dari beberapa bagian internal yang dapat di-style secara terpisah menggunakan predikat `::`.

| Sub-Control | Widget Terkait | Keterangan |
| --- | --- | --- |
| `::indicator` | `QCheckBox`, `QRadioButton`, `QGroupBox` | Kotak centang atau bulatan radio. |
| `::drop-down` | `QComboBox` | Tombol panah di sebelah kanan combobox. |
| `::down-arrow` / `::up-arrow` | `QComboBox`, `QSpinBox` | Ikon panah ke bawah/atas. |
| `::handle` | `QScrollBar`, `QSlider`, `QSplitter` | Batang pegangan yang bisa digeser. |
| `::groove` | `QSlider` | Jalur/lintasan tempat slider bergeser. |
| `::add-line` / `::sub-line` | `QScrollBar` | Tombol panah di ujung scrollbar. |
| `::item` | `QListWidget`, `QTreeWidget`, `QMenu` | Item individual di dalam list, tree, atau menu. |
| `::section` | `QHeaderView` (QTableWidget, QTreeView) | Judul kolom/baris pada tabel. |
| `::title` | `QGroupBox` | Teks judul pada GroupBox. |

```css
/* Contoh Kustomisasi Scrollbar Handle */
QScrollBar::handle:vertical {
    background: #555555;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background: #777777;
}

```

---

## 5. Kamus Lengkap Perintah (Properties) QSS

### A. Teks & Font

* **`color`**: Warna teks (`#HEX`, `rgb()`, `rgba()`, atau nama warna).
* **`font-family`**: Nama font (misal: `'Segoe UI'`, `'Roboto'`, `'Arial'`).
* **`font-size`**: Ukuran font (`12px`, `10pt`).
* **`font-weight`**: Ketebalan font (`normal`, `bold`, `100`–`900`).
* **`font-style`**: Gaya font (`normal`, `italic`, `oblique`).
* **`text-align`**: Penataan teks (`left`, `right`, `center`, `justify`).
* **`selection-color`**: Warna teks saat diblok/disorot.
* **`selection-background-color`**: Warna latar belakang blok teks.

### B. Latar Belakang & Tata Letak (Background & Box Model)

* **`background-color`**: Warna latar belakang widget.
* **`background-image`**: Gambar latar (`url(:/icon/bg.png)`).
* **`background-repeat`**: Perulangan gambar (`repeat`, `repeat-x`, `repeat-y`, `no-repeat`).
* **`background-position`**: Posisi gambar (`top left`, `center`, `bottom right`).
* **`background-attachment`**: Perilaku gambar (`fixed`, `scroll`).
* **`margin`**: Jarak luar widget (`margin-top`, `margin-right`, `margin-bottom`, `margin-left`).
* **`padding`**: Jarak dalam antara konten dan border (`padding-top`, `padding-left`, dll).
* **`width` / `height**`: Lebar dan tinggi eksplisit widget/sub-control.
* **`min-width` / `min-height**`: Batas ukuran minimum.
* **`max-width` / `max-height**`: Batas ukuran maksimum.

### C. Bingkai (Border)

* **`border`**: Format ringkas `width style color` (contoh: `1px solid #cccccc`).
* **`border-style`**: `none`, `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`.
* **`border-width`**: Ketebalan garis bingkai.
* **`border-color`**: Warna garis bingkai.
* **`border-radius`**: Sudut tumpul bingkai (`border-top-left-radius`, dll).
* **`outline`**: Garis fokus di luar border (`outline-color`, `outline-style`).

### D. Gradasi Warna (Gradients)

Qt menyediakan fungsi gradasi khusus untuk QSS:

* **Linear Gradient:** `qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e1e1e, stop:1 #2d2d2d)`
* **Radial Gradient:** `qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #fff, stop:1 #000)`
* **Conical Gradient:** `qconicalgradient(cx:0.5, cy:0.5, angle:30, stop:0 #fff, stop:1 #000)`

---

## 6. Contoh Template Dark Theme Siap Pakai

Berikut adalah implementasi stylesheet tema gelap (*dark theme*) modern yang mencakup widget-widget utama:

```css
/* --- Global Style --- */
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: "Segoe UI", sans-serif;
    font-size: 13px;
}

/* --- LineEdit & TextEdit --- */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #181825;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px 10px;
    color: #cdd6f4;
    selection-background-color: #f5e0dc;
    selection-color: #11111b;
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid #89b4fa;
}

/* --- PushButton --- */
QPushButton {
    background-color: #89b4fa;
    color: #11111b;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #b4befe;
}

QPushButton:pressed {
    background-color: #74c7ec;
}

QPushButton:disabled {
    background-color: #313244;
    color: #6c7086;
}

/* --- ComboBox --- */
QComboBox {
    background-color: #181825;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px 10px;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #181825;
    border: 1px solid #45475a;
    selection-background-color: #313244;
    selection-color: #cdd6f4;
}

/* --- TableView / TableWidget --- */
QTableWidget, QTableView {
    background-color: #181825;
    gridline-color: #313244;
    border: 1px solid #45475a;
    border-radius: 6px;
}

QHeaderView::section {
    background-color: #313244;
    color: #cdd6f4;
    padding: 6px;
    border: none;
    font-weight: bold;
}

/* --- ScrollBar --- */
QScrollBar:vertical {
    background: #181825;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #45475a;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #585b70;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

```