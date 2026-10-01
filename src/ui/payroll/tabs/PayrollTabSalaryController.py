from PySide6.QtWidgets import QWidget
from src.ui.payroll.tabs.PayrollTabSalary import Ui_PayrollTabSalary

class PayrollTabSalaryController(QWidget):
    def __init__(self):
        super(PayrollTabSalaryController, self).__init__()
        self.ui = Ui_PayrollTabSalary()
        self.ui.setupUi(self)
        
        self.ui.labelNama.setText("Pradya Tiara Frahastiwie")
        
        self.ui.labelPenghasilan.setText("10.000.000")
        self.ui.labelPotongan.setText("1.000.000")
        self.ui.labelDiterima.setText("9.000.000")