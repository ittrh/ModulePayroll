# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalaryComponent.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_SalaryComponent(object):
    def setupUi(self, SalaryComponent):
        if not SalaryComponent.objectName():
            SalaryComponent.setObjectName(u"SalaryComponent")
        SalaryComponent.resize(893, 604)
        self.verticalLayout = QVBoxLayout(SalaryComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(SalaryComponent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setPixmap(QPixmap(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_device_search.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.editCari = QLineEdit(SalaryComponent)
        self.editCari.setObjectName(u"editCari")

        self.horizontalLayout.addWidget(self.editCari)

        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushAddComponent = QPushButton(SalaryComponent)
        self.pushAddComponent.setObjectName(u"pushAddComponent")
        font = QFont()
        font.setBold(True)
        self.pushAddComponent.setFont(font)
        self.pushAddComponent.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/game_space.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushAddComponent.setIcon(icon)
        self.pushAddComponent.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushAddComponent)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(SalaryComponent)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(SalaryComponent)

        QMetaObject.connectSlotsByName(SalaryComponent)
    # setupUi

    def retranslateUi(self, SalaryComponent):
        SalaryComponent.setWindowTitle(QCoreApplication.translate("SalaryComponent", u"Form", None))
        self.label_2.setText("")
        self.editCari.setPlaceholderText(QCoreApplication.translate("SalaryComponent", u"Search ...", None))
        self.pushAddComponent.setText(QCoreApplication.translate("SalaryComponent", u"Add Comp...", None))
    # retranslateUi

