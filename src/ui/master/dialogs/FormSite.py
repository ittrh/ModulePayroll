# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormSite.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_FormSite(object):
    def setupUi(self, FormSite):
        if not FormSite.objectName():
            FormSite.setObjectName(u"FormSite")
        FormSite.resize(494, 176)
        self.verticalLayout = QVBoxLayout(FormSite)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(FormSite)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FormSite)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editIdSite = QLineEdit(FormSite)
        self.editIdSite.setObjectName(u"editIdSite")

        self.horizontalLayout.addWidget(self.editIdSite)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FormSite)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editSiteName = QLineEdit(FormSite)
        self.editSiteName.setObjectName(u"editSiteName")

        self.horizontalLayout_2.addWidget(self.editSiteName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushCancel = QPushButton(FormSite)
        self.pushCancel.setObjectName(u"pushCancel")
        self.pushCancel.setMaximumSize(QSize(95, 30))
        self.pushCancel.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushCancel)

        self.pushSave = QPushButton(FormSite)
        self.pushSave.setObjectName(u"pushSave")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/everdo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSave.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushSave)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(FormSite)

        QMetaObject.connectSlotsByName(FormSite)
    # setupUi

    def retranslateUi(self, FormSite):
        FormSite.setWindowTitle(QCoreApplication.translate("FormSite", u"Form Site", None))
        self.label_4.setText(QCoreApplication.translate("FormSite", u"Form Site", None))
        self.label.setText(QCoreApplication.translate("FormSite", u"ID Site :", None))
        self.editIdSite.setText("")
        self.editIdSite.setPlaceholderText(QCoreApplication.translate("FormSite", u"Example : HO0001", None))
        self.label_2.setText(QCoreApplication.translate("FormSite", u"Site :", None))
        self.editSiteName.setText("")
        self.editSiteName.setPlaceholderText(QCoreApplication.translate("FormSite", u"Example : Head Office - Gunung Tabur", None))
        self.pushCancel.setText(QCoreApplication.translate("FormSite", u"Cancel", None))
        self.pushSave.setText(QCoreApplication.translate("FormSite", u"Save", None))
    # retranslateUi

