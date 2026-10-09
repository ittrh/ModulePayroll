from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt
from src.ui.master.dialogs.FormRules import Ui_FormRules
from src.fun.JsonTableModel import JsonTableModel
from src.fun.master.RulesCrud import RulesCrud

class EditRulesController(QDialog):
    def __init__(self, data_rule=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormRules()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        
        # 1. Inisialisasi atribut dictionary penyimpan config
        self.rule_data = data_rule or {}
        self.config_rules_json = dict(self.rule_data.get("config", {}))

        # 2. Inisialisasi Model & Tabel DAHULU
        self.config_rules_model = JsonTableModel()
        self.ui.tableView.setModel(self.config_rules_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tableView.setSelectionBehavior(self.ui.tableView.SelectionBehavior.SelectRows)
        
        # 3. Panggil load_rule_to_form SETELAH model siap
        if self.rule_data:
            self.load_rule_to_form()
        
        if hasattr(self.ui, "pushCancel"):
            self.ui.pushCancel.clicked.connect(self.reject)
        if hasattr(self.ui, "pushSave"):
            self.ui.pushSave.clicked.connect(self.save_rules_handler)
        if hasattr(self.ui, "pushInsertRules"):
            self.ui.pushInsertRules.clicked.connect(self.insert_rules_handler)
            
    def load_rule_to_form(self):
        rule_id = self.rule_data.get("id", "")
        rule_name = self.rule_data.get("name", "")
        
        self.ui.editIdRules.setText(str(rule_id))
        self.ui.editNameofRules.setText(str(rule_name))
        
        self.ui.editIdRules.setEnabled(False) 
        
        self.config_rules_model.set_json_data(self.config_rules_json)
    
    def insert_rules_handler(self):
        key = self.ui.editKey.text().strip()
        value = self.ui.editValue.text().strip()
            
        if not key or not value:
            return 
                
        self.config_rules_json[key] = value
        self.config_rules_model.set_json_data(self.config_rules_json)
            
        self.ui.editKey.clear()
        self.ui.editValue.clear()
        self.ui.editKey.setFocus()
            
    def save_rules_handler(self):
        # id_rules = self.ui.editIdRules.text().strip().upper()
        name_rules = self.ui.editNameofRules.text().strip()
            
        if not not name_rules:
            name_rules = self.rule_data.get("name")
    
        data = {
            "id": self.rule_data.get("id"),
            "name": name_rules,
            "config": self.config_rules_json
        }
            
        try:
            crud = RulesCrud()
            crud.update_rules(data) # if hasattr(crud, 'update_rules') else crud.create_rules(data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {str(e)}")
                
    def delete_rules_handler(self):
        """Handler untuk menghapus item dari dict & memperbarui tampilan tabel."""
        indexes = self.ui.tableView.selectionModel().selectedIndexes()
            
        if not indexes:
            return
    
        selected_row = indexes[0].row()
            
        keys_list = list(self.config_rules_json.keys())
        if 0 <= selected_row < len(keys_list):
            key_to_delete = keys_list[selected_row]
                
            del self.config_rules_json[key_to_delete]
            
            # Perbaikan nama variabel model
            self.config_rules_model.set_json_data(self.config_rules_json)
            self.ui.tableView.viewport().update()
    
    def keyPressEvent(self, event):
        """Menangani penekanan tombol Delete pada keyboard saat tabel aktif."""
        if event.key() == Qt.Key.Key_Delete and self.ui.tableView.hasFocus():
            self.delete_rules_handler()
        else:
            super().keyPressEvent(event)