from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt
from src.ui.master.dialogs.FormRules import Ui_FormRules
from src.fun.JsonTableModel import JsonTableModel
from src.fun.master.RulesCrud import RulesCrud

class AddRulesController(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormRules()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        
        self.config_rules_json: dict = {}
        
        self.rules_table_model = JsonTableModel()
        self.ui.tableView.setModel(self.rules_table_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        # Biarkan selection memilih seluruh baris agar UX lebih konsisten
        self.ui.tableView.setSelectionBehavior(self.ui.tableView.SelectionBehavior.SelectRows)
        
        self.ui.pushInsertRules.clicked.connect(self.insert_rules_handler)
        self.ui.pushSave.clicked.connect(self.save_rules_handler)
        
        if hasattr(self.ui, 'pushCancel'):
            self.ui.pushCancel.clicked.connect(self.reject)
        
    def insert_rules_handler(self):
        key = self.ui.editKey.text().strip()
        value = self.ui.editValue.text().strip()
        
        if not key or not value:
            return 
            
        self.config_rules_json[key] = value
        self.rules_table_model.set_json_data(self.config_rules_json)
        
        self.ui.editKey.clear()
        self.ui.editValue.clear()
        self.ui.editKey.setFocus()
        
    def save_rules_handler(self):
        id_rules = self.ui.editIdRules.text().strip().upper()
        name_rules = self.ui.editNameofRules.text().strip()
        
        if not id_rules or not name_rules:
            QMessageBox.warning(self, "Peringatan", "ID Rules dan Name of Rules wajib diisi!")
            return

        data = {
            "id": id_rules,
            "name": name_rules,
            "config": self.config_rules_json
        }
        
        try:
            crud = RulesCrud()
            crud.create_rules(data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {str(e)}")
            
    def delete_rules_handler(self):
        """Handler untuk menghapus item dari dict & memperbarui tampilan tabel."""
        # Ambil semua sel yang terpilih jika selectedRows() kosong
        indexes = self.ui.tableView.selectionModel().selectedIndexes()
        
        if not indexes:
            return

        # Ambil index baris pertama yang aktif
        selected_row = indexes[0].row()
        
        keys_list = list(self.config_rules_json.keys())
        if 0 <= selected_row < len(keys_list):
            key_to_delete = keys_list[selected_row]
            
            # Hapus dari dictionary internal
            del self.config_rules_json[key_to_delete]
            
            # Update data di model
            self.rules_table_model.set_json_data(self.config_rules_json)
            
            # Paksa tampilan QTableView melakukan render ulang
            self.ui.tableView.viewport().update()

    def keyPressEvent(self, event):
        """Menangani penekanan tombol Delete pada keyboard saat tabel aktif."""
        if event.key() == Qt.Key.Key_Delete and self.ui.tableView.hasFocus():
            self.delete_rules_handler()
        else:
            super().keyPressEvent(event)