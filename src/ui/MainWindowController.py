from PySide6.QtWidgets import QMainWindow
from src.ui.MainWindow import Ui_MainWindow
from src.ui.dashboard.DashboardController import DashboardController
from src.ui.master.MasterController import MasterController

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
        
        self.show_dashboard()
        
        self.master_page = MasterController()
        self.master_stack_index = self.ui.stackedWidget.addWidget(self.master_page)
        self.ui.pushSideMasters.clicked.connect(self.show_master)
        
    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(self.dashboard_stack_index)
        self.ui.labelTittle.setText(self.default_title)

    def show_master(self):
        self.ui.stackedWidget.setCurrentIndex(self.master_stack_index)
        self.ui.labelTittle.setText("Settings Master")