from PySide6.QtWidgets import QWidget, QMessageBox, QHeaderView, QDialog
from src.ui.master.tabs.SiteDesignation import Ui_SiteDesignation
from src.ui.master.dialogs.AddSiteController import AddSiteController
from src.ui.master.dialogs.EditSiteController import EditSiteController
from src.fun.QueryTableModel import QueryTableModel
from src.fun.master.SiteDesignationCrud import SiteCrud

class SiteDesignationController(QWidget):
    HEADER = ["ID Site", "Site"]

    def __init__(self, parent=None):
        super(SiteDesignationController, self).__init__(parent)
        self.ui = Ui_SiteDesignation()
        self.ui.setupUi(self)

        self.site_crud = SiteCrud()
        self.site_table_model = QueryTableModel()

        self.ui.tableSites.setModel(self.site_table_model)
        self.ui.tableSites.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.tableSites.setSelectionBehavior(
            self.ui.tableSites.SelectionBehavior.SelectRows
        )

        self.load_sites_data()

        # Signal Connections
        self.ui.tableSites.doubleClicked.connect(self.on_table_site_clicked)
        self.ui.pushAddSite.clicked.connect(self.add_site_handler)
        self.ui.editCariSites.textChanged.connect(self.search_handler)

    def load_sites_data(self, data_sites=None):
        if data_sites is not None:
            self.site_table_model.set_data(data=data_sites, header=self.HEADER)
        else:
            try:
                sites_data = self.site_crud.get_all_site()
                self.site_table_model.set_data(data=sites_data, header=self.HEADER)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal memuat data site: {str(e)}")

    def add_site_handler(self):
        dialog = AddSiteController(parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # Re-evaluate filter saat ini dari database setelah penambahan
            self.search_handler()

    def on_table_site_clicked(self, index):
        selected_data: dict = self.site_table_model.get_row_data(index.row())
        if selected_data:
            dialog = EditSiteController(data_site=selected_data, parent=self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                # Re-evaluate filter saat ini dari database setelah pembaruan/penghapusan
                self.search_handler()

    def search_handler(self):
        keyword = self.ui.editCariSites.text().strip()
        try:
            if keyword:
                search_data = self.site_crud.search_site(keyword)
                self.load_sites_data(data_sites=search_data)
            else:
                self.load_sites_data()
        except Exception as e:
            QMessageBox.warning(self, "Peringatan", f"Gagal mencari data: {str(e)}")