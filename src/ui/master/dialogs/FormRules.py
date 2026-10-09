# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormRules.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_FormRules(object):
    def setupUi(self, FormRules):
        if not FormRules.objectName():
            FormRules.setObjectName(u"FormRules")
        FormRules.resize(746, 530)
        self.verticalLayout = QVBoxLayout(FormRules)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(FormRules)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(FormRules)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.editIdRules = QLineEdit(FormRules)
        self.editIdRules.setObjectName(u"editIdRules")

        self.horizontalLayout_2.addWidget(self.editIdRules)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(FormRules)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.editNameofRules = QLineEdit(FormRules)
        self.editNameofRules.setObjectName(u"editNameofRules")

        self.horizontalLayout_3.addWidget(self.editNameofRules)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(FormRules)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.editKey = QLineEdit(FormRules)
        self.editKey.setObjectName(u"editKey")

        self.horizontalLayout.addWidget(self.editKey)

        self.editValue = QLineEdit(FormRules)
        self.editValue.setObjectName(u"editValue")

        self.horizontalLayout.addWidget(self.editValue)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushInsertRules = QPushButton(FormRules)
        self.pushInsertRules.setObjectName(u"pushInsertRules")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/adobe_fill_and_sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushInsertRules.setIcon(icon)
        self.pushInsertRules.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushInsertRules)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(FormRules)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushCancel = QPushButton(FormRules)
        self.pushCancel.setObjectName(u"pushCancel")
        self.pushCancel.setMaximumSize(QSize(95, 30))
        self.pushCancel.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushCancel)

        self.pushSave = QPushButton(FormRules)
        self.pushSave.setObjectName(u"pushSave")
        icon1 = QIcon()
        icon1.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/everdo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSave.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushSave)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(FormRules)

        QMetaObject.connectSlotsByName(FormRules)
    # setupUi

    def retranslateUi(self, FormRules):
        FormRules.setWindowTitle(QCoreApplication.translate("FormRules", u"Form Rules", None))
        self.label_4.setText(QCoreApplication.translate("FormRules", u"Form Rules", None))
        self.label.setText(QCoreApplication.translate("FormRules", u"ID Rules :", None))
        self.editIdRules.setPlaceholderText(QCoreApplication.translate("FormRules", u"Example : BPJS_TK ...", None))
        self.label_2.setText(QCoreApplication.translate("FormRules", u"Name of Rules :", None))
        self.editNameofRules.setPlaceholderText(QCoreApplication.translate("FormRules", u"Example : BPJS Tenaga Kerja ...", None))
        self.label_3.setText(QCoreApplication.translate("FormRules", u"Config Rules :", None))
        self.editKey.setPlaceholderText(QCoreApplication.translate("FormRules", u"Key ...", None))
        self.editValue.setPlaceholderText(QCoreApplication.translate("FormRules", u"Value ...", None))
        self.pushInsertRules.setText(QCoreApplication.translate("FormRules", u"Insert Rules", None))
        self.pushCancel.setText(QCoreApplication.translate("FormRules", u"Cancel", None))
        self.pushSave.setText(QCoreApplication.translate("FormRules", u"Save", None))
    # retranslateUi

