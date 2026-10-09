from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt
from src.ui.master.dialogs.FormSite import Ui_FormSite
from src.fun.master.SiteDesignationCrud import SiteCrud

class AddSiteController(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormSite()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.ui.label_4.setText("Add Site")
        self.setWindowTitle("Add Site")
        
        self.ui.pushCancel.clicked.connect(self.reject)
        self.ui.pushSave.clicked.connect(self.save_site_handler)
    
    def save_site_handler(self):
        crud = SiteCrud()
        id_site = self.ui.editIdSite.text().strip().upper()
        name_site = self.ui.editSiteName.text().strip().title()
        
        if not id_site or not name_site:
            QMessageBox.warning(self, "Peringatan", "ID Site dan Site wajib diisi!")
            return
        
        data = {
            "id": id_site,
            "name": name_site
        }
        
        try:
            crud.create_site(data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {str(e)}")