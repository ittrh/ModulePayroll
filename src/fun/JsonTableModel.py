from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
import json

class JsonTableModel(QAbstractTableModel):
    def __init__(self, json_data=None, parent=None):
        super(JsonTableModel, self).__init__(parent)
        self.headers = ["Item / Key", "Value"]
        self._data_list = []
        
        if json_data:
            self.set_json_data(json_data)

    def set_json_data(self, data):
        """Menerima input berupa dict atau string JSON."""
        self.beginResetModel()
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                data = {}

        if isinstance(data, dict):
            # Ubah dictionary key-value menjadi list tuple [(key, value), ...]
            self._data_list = list(data.items())
        elif isinstance(data, list):
            # Jika JSON berbentuk list of dict, tampilkan berdasarkan index
            self._data_list = [(f"Index {i}", item) for i, item in enumerate(data)]
        else:
            self._data_list = []

        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return len(self._data_list)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        row = index.row()
        col = index.column()
        key, value = self._data_list[row]

        if col == 0:
            return str(key)
        elif col == 1:
            # Jika value berupa dict/list (nested JSON), ubah ke string JSON agar rapi
            if isinstance(value, (dict, list)):
                return json.dumps(value, ensure_ascii=False)
            return str(value) if value is not None else ""

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None