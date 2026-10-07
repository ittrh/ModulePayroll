from PySide6.QtWidgets import QWidget
from src.ui.master.tabs.SiteDesignation import Ui_SiteDesignation

class SiteDesignationController(QWidget):
    def __init__(self):
        super(SiteDesignationController, self).__init__()
        self.ui = Ui_SiteDesignation()
        self.ui.setupUi(self)