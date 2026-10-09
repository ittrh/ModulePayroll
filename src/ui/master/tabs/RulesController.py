from PySide6.QtWidgets import QWidget, QHeaderView, QDialog, QMessageBox
from src.ui.master.tabs.Rules import Ui_Rules
from src.fun.ComboBtnSetup import ComboBtnSetup
from src.fun.JsonTableModel import JsonTableModel

from src.ui.master.dialogs.AddRulesController import AddRulesController
from src.ui.master.dialogs.EditRulesController import EditRulesController
from src.fun.master.RulesCrud import RulesCrud

class RulesController(QWidget):
    def __init__(self):
        super(RulesController, self).__init__()
        self.ui = Ui_Rules()
        self.ui.setupUi(self)
        
        self.rules_data_by_id: dict = {}
        self.combo_btn = ComboBtnSetup()
        
        self.rules_table_model = JsonTableModel()
        self.ui.tableView.setModel(self.rules_table_model)
        
        self.load_combo_box()
        
        self.ui.comboRules.currentIndexChanged.connect(self.combo_box_selector)
        self.ui.pushAddRules.clicked.connect(self.add_rules_handler)
        
        self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        self.crud = RulesCrud()
        
        self.ui.pushHapusBatal.clicked.connect(self.delete_rules_handler)
        self.ui.pushEditSimpan.clicked.connect(self.edit_rules_handler)
        
    def load_combo_box(self):
        rules_list = self.combo_btn.rules_list()
        self.combo_btn.combo_btn_setup(
            self.ui.comboRules, 
            rules_list, 
            display_key="name", 
            placeholder="Choose Rules"
        )
        
    def combo_box_selector(self):
        # Mengambil dictionary item yang disimpan di currentData()
        selected_data = self.ui.comboRules.currentData()
        
        if isinstance(selected_data, dict):
            self.rules_data_by_id = selected_data
            self.rules_table_model.set_json_data(self.rules_data_by_id.get("config", {}))
        else:
            self.rules_data_by_id = {}
            
    def add_rules_handler(self):
        dialog = AddRulesController()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_combo_box()  # Refresh isi QComboBox
            
            # Opsional: Otomatis pilih item terbaru di QComboBox jika ada
            if self.ui.comboRules.count() > 1:
                self.ui.comboRules.setCurrentIndex(self.ui.comboRules.count() - 1)
                
    def edit_rules_handler(self):
        if not self.rules_data_by_id or not self.rules_data_by_id.get("id"):
            QMessageBox.warning(self, "Peringatan", "Plih rule yang ingin dirubah")
            return
        
        current_index = self.ui.comboRules.currentIndex()
        dialog = EditRulesController(data_rule=self.rules_data_by_id, parent=self)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_combo_box()
            
            if 0 <= current_index < self.ui.comboRules.count():
                self.ui.comboRules.setCurrentIndex(current_index)
            else:
                self.combo_box_selector()
    
    def delete_rules_handler(self):
        rule_id = self.rules_data_by_id.get("id")
        rule_name = self.rules_data_by_id.get("name")
        if rule_id:
            reply = QMessageBox.question(self, "Konfirmasi Hapus!",
                                 f"Yakin ingin menghapus {rule_name}?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    self.crud.delete_rules(rule_id)
                    self.load_combo_box()
                    if self.rules_data_by_id:   
                        self.ui.comboRules.setCurrentIndex(self.ui.comboRules.count() - 1)
                    else:
                        self.rules_table_model.set_json_data({})
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")