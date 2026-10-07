from PySide6.QtWidgets import QWidget
from src.ui.master.Master import Ui_Master

from src.ui.master.tabs.RulesController import RulesController
from src.ui.master.tabs.SiteDesignationController import SiteDesignationController
from src.ui.master.tabs.SalaryComponentController import SalaryComponentController

class MasterController(QWidget):
    def __init__(self):
        super(MasterController, self).__init__()
        self.ui = Ui_Master()
        self.ui.setupUi(self)
        self.ui.tabWidget.clear()
        
        # Tab segment
        self.tab_rules = RulesController()
        self.tab_sitedesignation = SiteDesignationController()
        self.tab_salarycomponent = SalaryComponentController()
        
        self.ui.tabWidget.addTab(self.tab_rules, "Rules")
        self.ui.tabWidget.addTab(self.tab_sitedesignation, "Sites / Designations")
        self.ui.tabWidget.addTab(self.tab_salarycomponent, "Salary Components")