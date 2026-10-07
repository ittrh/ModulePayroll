# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SiteDesignation.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_SiteDesignation(object):
    def setupUi(self, SiteDesignation):
        if not SiteDesignation.objectName():
            SiteDesignation.setObjectName(u"SiteDesignation")
        SiteDesignation.resize(908, 603)
        self.horizontalLayout_3 = QHBoxLayout(SiteDesignation)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(SiteDesignation)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(SiteDesignation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setMaximumSize(QSize(20, 20))
        self.label_3.setPixmap(QPixmap(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_device_search.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.editCariSites = QLineEdit(SiteDesignation)
        self.editCariSites.setObjectName(u"editCariSites")

        self.horizontalLayout_2.addWidget(self.editCariSites)

        self.pushAddSite = QPushButton(SiteDesignation)
        self.pushAddSite.setObjectName(u"pushAddSite")
        font = QFont()
        font.setBold(True)
        self.pushAddSite.setFont(font)
        self.pushAddSite.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/game_space.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushAddSite.setIcon(icon)
        self.pushAddSite.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushAddSite)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableSites = QTableView(SiteDesignation)
        self.tableSites.setObjectName(u"tableSites")

        self.verticalLayout_2.addWidget(self.tableSites)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(SiteDesignation)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(SiteDesignation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))
        self.label_4.setPixmap(QPixmap(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_device_search.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.editCariDesignations = QLineEdit(SiteDesignation)
        self.editCariDesignations.setObjectName(u"editCariDesignations")

        self.horizontalLayout.addWidget(self.editCariDesignations)

        self.pushAddDesignation = QPushButton(SiteDesignation)
        self.pushAddDesignation.setObjectName(u"pushAddDesignation")
        self.pushAddDesignation.setFont(font)
        self.pushAddDesignation.setStyleSheet(u"text-align:left;")
        self.pushAddDesignation.setIcon(icon)
        self.pushAddDesignation.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushAddDesignation)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableDesignation = QTableView(SiteDesignation)
        self.tableDesignation.setObjectName(u"tableDesignation")

        self.verticalLayout.addWidget(self.tableDesignation)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(SiteDesignation)

        QMetaObject.connectSlotsByName(SiteDesignation)
    # setupUi

    def retranslateUi(self, SiteDesignation):
        SiteDesignation.setWindowTitle(QCoreApplication.translate("SiteDesignation", u"Form", None))
        self.label.setText(QCoreApplication.translate("SiteDesignation", u"Sites :", None))
        self.label_3.setText("")
        self.editCariSites.setPlaceholderText(QCoreApplication.translate("SiteDesignation", u"Cari ...", None))
        self.pushAddSite.setText(QCoreApplication.translate("SiteDesignation", u"Add Site", None))
        self.label_2.setText(QCoreApplication.translate("SiteDesignation", u"Designations :", None))
        self.label_4.setText("")
        self.editCariDesignations.setPlaceholderText(QCoreApplication.translate("SiteDesignation", u"Cari ...", None))
        self.pushAddDesignation.setText(QCoreApplication.translate("SiteDesignation", u"Add Desig...", None))
    # retranslateUi

