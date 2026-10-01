from PySide6.QtWidgets import QMainWindow
from src.ui.MainWindow import Ui_MainWindow
from src.ui.dashboard.DashboardController import DashboardController
from src.ui.payroll.PayrollController import PayrollController

class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.opened_window = []
        self.default_title = self.ui.labelTittle.text()
        
        self.dashboard_page = DashboardController()
        self.dashboard_stack_index = self.ui.stackedWidget.addWidget(self.dashboard_page)
        self.ui.pushSideDashboard.clicked.connect(self.show_dashboard)
        
        self.payroll_page = PayrollController()
        self.payroll_stack_index = self.ui.stackedWidget.addWidget(self.payroll_page)
        self.ui.pushSidePayroll.clicked.connect(self.show_payroll)
        
        self.show_dashboard()
        
    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(self.dashboard_stack_index)
        self.ui.labelTittle.setText(self.default_title)
        
    def show_payroll(self):
        self.ui.stackedWidget.setCurrentIndex(self.payroll_stack_index)
        self.ui.labelTittle.setText("Payroll")
