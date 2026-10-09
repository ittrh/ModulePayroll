from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class QueryTableModel(QAbstractTableModel):
    def __init__(self, data=None, header: list = None, parent=None):
        super().__init__(parent)
        self._data = data or []
        self._header = header or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # Jika header diisi manual, gunakan panjang header.
        if self._header:
            return len(self._header)
        
        # Jika header kosong dan ada data, tentukan jumlah kolom dari baris pertama.
        if self._data:
            first_row = self._data[0]
            if isinstance(first_row, (list, tuple)):
                return len(first_row)
            elif isinstance(first_row, dict):
                return len(first_row)
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        row = self._data[index.row()]
        col = index.column()

        # Handle jika row berupa tuple/list (Hasil raw query DB / cursor.fetchall())
        if isinstance(row, (tuple, list)):
            if col < len(row):
                val = row[col]
                return str(val) if val is not None else ""

        # Handle jika row berupa dictionary (e.g. {'id': 'S01', 'name': 'Site A'})
        elif isinstance(row, dict):
            keys = list(row.keys())
            if col < len(keys):
                val = row[keys[col]]
                return str(val) if val is not None else ""

        # Handle jika row berupa Objek Model (e.g. Objek SQLAlchemy)
        elif hasattr(row, "__dict__"):
            attrs = [a for a in dir(row) if not a.startswith('_') and not callable(getattr(row, a))]
            if col < len(attrs):
                val = getattr(row, attrs[col])
                return str(val) if val is not None else ""

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            if self._header and section < len(self._header):
                return self._header[section]
        return None

    def set_data(self, data, header: list = None):
        """Memperbarui isi tabel secara dinamis."""
        self.beginResetModel()
        self._data = data or []
        if header is not None:
            self._header = header
        self.endResetModel()

    def get_row_data(self, row_index: int):
        """Helper untuk mengambil data mentah pada baris terpilih."""
        if 0 <= row_index < len(self._data):
            return self._data[row_index]
        return None