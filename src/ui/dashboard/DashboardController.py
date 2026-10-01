from PySide6.QtWidgets import QWidget
from src.ui.dashboard.Dashboard import Ui_Dashboard

class DashboardController(QWidget):
    def __init__(self):
        super(DashboardController, self).__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)