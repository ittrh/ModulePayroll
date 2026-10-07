from PySide6.QtWidgets import QWidget, QHeaderView
from src.ui.master.tabs.Rules import Ui_Rules
from src.fun.ComboBtnSetup import ComboBtnSetup
from src.fun.master.RulesTableModel import RulesTableModel

class RulesController(QWidget):
    def __init__(self):
        super(RulesController, self).__init__()
        self.ui = Ui_Rules()
        self.ui.setupUi(self)
        
        self.rules_data_by_id: dict = {}
        self.combo_btn = ComboBtnSetup()
        
        self.rules_table_model = RulesTableModel()
        self.ui.tableView.setModel(self.rules_table_model)
        
        self.load_combo_box()
        
        self.ui.comboRules.currentIndexChanged.connect(self.combo_box_selector)
        
        self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
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