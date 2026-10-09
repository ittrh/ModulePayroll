from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt
from src.ui.master.dialogs.FormSite import Ui_FormSite
from src.fun.master.SiteDesignationCrud import SiteCrud

class EditSiteController(QDialog):
    def __init__(self, data_site: dict = None, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormSite()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.ui.label_4.setText("Edit Site")
        self.setWindowTitle("Edit Site")
        
        self.crud = SiteCrud()
        
        self.site_data = data_site or {}
        
        self.ui.pushCancel.setText("Delete")
        self.ui.editIdSite.setEnabled(False)
        self.ui.editIdSite.setText(self.site_data.get("id"))
        self.ui.editSiteName.setText(self.site_data.get("name"))
        
        self.ui.pushSave.clicked.connect(self.save_site_handler)
        self.ui.pushCancel.clicked.connect(self.delete_site_handler)
        
    def save_site_handler(self):
        name_site = self.ui.editSiteName.text().strip().title()
        
        if not name_site:
            name_site = self.site_data['name']
            
        data = {
            "id": self.site_data['id'],
            "name": name_site
        }
        
        try: 
            self.crud.update_site(data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {str(e)}")
            
    def delete_site_handler(self):
        reply = QMessageBox.question(self, "Konfirmasi Hapus!",
                                     f"Yakin ingin menghapus {self.site_data['name']}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.crud.delete_site(self.site_data['id'])
                self.accept()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")
                
        
        