# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Rules.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_Rules(object):
    def setupUi(self, Rules):
        if not Rules.objectName():
            Rules.setObjectName(u"Rules")
        Rules.resize(893, 604)
        self.verticalLayout = QVBoxLayout(Rules)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Rules)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboRules = QComboBox(Rules)
        self.comboRules.setObjectName(u"comboRules")

        self.horizontalLayout.addWidget(self.comboRules)

        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(Rules)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setPixmap(QPixmap(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_device_search.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.editCari = QLineEdit(Rules)
        self.editCari.setObjectName(u"editCari")

        self.horizontalLayout.addWidget(self.editCari)

        self.pushAddRules = QPushButton(Rules)
        self.pushAddRules.setObjectName(u"pushAddRules")
        font = QFont()
        font.setBold(True)
        self.pushAddRules.setFont(font)
        self.pushAddRules.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/game_space.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushAddRules.setIcon(icon)
        self.pushAddRules.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushAddRules)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(Rules)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushHapusBatal = QPushButton(Rules)
        self.pushHapusBatal.setObjectName(u"pushHapusBatal")
        self.pushHapusBatal.setMaximumSize(QSize(95, 30))
        self.pushHapusBatal.setStyleSheet(u"border:none;")

        self.horizontalLayout_2.addWidget(self.pushHapusBatal)

        self.pushEditSimpan = QPushButton(Rules)
        self.pushEditSimpan.setObjectName(u"pushEditSimpan")
        self.pushEditSimpan.setMaximumSize(QSize(95, 30))
        self.pushEditSimpan.setFont(font)
        self.pushEditSimpan.setStyleSheet(u"text-align:left;")
        self.pushEditSimpan.setIcon(icon)
        self.pushEditSimpan.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushEditSimpan)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Rules)

        QMetaObject.connectSlotsByName(Rules)
    # setupUi

    def retranslateUi(self, Rules):
        Rules.setWindowTitle(QCoreApplication.translate("Rules", u"Form", None))
        self.label.setText(QCoreApplication.translate("Rules", u"Rules :", None))
        self.label_2.setText("")
        self.editCari.setPlaceholderText(QCoreApplication.translate("Rules", u"Cari ...", None))
        self.pushAddRules.setText(QCoreApplication.translate("Rules", u"Add Rules", None))
        self.pushHapusBatal.setText(QCoreApplication.translate("Rules", u"Hapus", None))
        self.pushEditSimpan.setText(QCoreApplication.translate("Rules", u"Edit", None))
    # retranslateUi

