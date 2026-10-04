from PySide6.QtWidgets import QWidget
from src.ui.payroll.Payroll import Ui_Payroll

from src.ui.payroll.tab_salary.PayrollTabSalaryController import PayrollTabSalaryController

class PayrollController(QWidget):
    def __init__(self):
        super(PayrollController, self).__init__()
        self.ui = Ui_Payroll()
        self.ui.setupUi(self)
        self.ui.tabWidget.clear()
        
        self.tab_salary = PayrollTabSalaryController()
        
        self.ui.tabWidget.addTab(self.tab_salary, "Salary")
        