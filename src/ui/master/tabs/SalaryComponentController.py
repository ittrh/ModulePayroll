from PySide6.QtWidgets import QWidget
from src.ui.master.tabs.SalaryComponent import Ui_SalaryComponent

class SalaryComponentController(QWidget):
    def __init__(self):
        super(SalaryComponentController, self).__init__()
        self.ui = Ui_SalaryComponent()
        self.ui.setupUi(self)