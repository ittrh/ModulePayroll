# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 728)
        icon = QIcon()
        icon.addFile(u":/ico/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionMasters = QAction(MainWindow)
        self.actionMasters.setObjectName(u"actionMasters")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDonate = QAction(MainWindow)
        self.actionDonate.setObjectName(u"actionDonate")
        self.actionAbout_Me = QAction(MainWindow)
        self.actionAbout_Me.setObjectName(u"actionAbout_Me")
        self.actionBasic_Salary = QAction(MainWindow)
        self.actionBasic_Salary.setObjectName(u"actionBasic_Salary")
        self.actionDeduction = QAction(MainWindow)
        self.actionDeduction.setObjectName(u"actionDeduction")
        self.actionBenefits = QAction(MainWindow)
        self.actionBenefits.setObjectName(u"actionBenefits")
        self.actionIncome_Tax = QAction(MainWindow)
        self.actionIncome_Tax.setObjectName(u"actionIncome_Tax")
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionSite = QAction(MainWindow)
        self.actionSite.setObjectName(u"actionSite")
        self.actionPosition = QAction(MainWindow)
        self.actionPosition.setObjectName(u"actionPosition")
        self.actionReports = QAction(MainWindow)
        self.actionReports.setObjectName(u"actionReports")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QWidget(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMaximumSize(QSize(160, 16777215))
        self.sideBar.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.sideBar)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.sideBar)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/ico/images/logo.ico"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.sideBar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pushSideDashboard = QPushButton(self.sideBar)
        self.pushSideDashboard.setObjectName(u"pushSideDashboard")
        self.pushSideDashboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/google_home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideDashboard.setIcon(icon1)
        self.pushSideDashboard.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideDashboard)

        self.pushSideMasters = QPushButton(self.sideBar)
        self.pushSideMasters.setObjectName(u"pushSideMasters")
        self.pushSideMasters.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/walmart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideMasters.setIcon(icon2)
        self.pushSideMasters.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideMasters)

        self.pushSideTransactions = QPushButton(self.sideBar)
        self.pushSideTransactions.setObjectName(u"pushSideTransactions")
        self.pushSideTransactions.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/picpay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideTransactions.setIcon(icon3)
        self.pushSideTransactions.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideTransactions)

        self.pushSideReports = QPushButton(self.sideBar)
        self.pushSideReports.setObjectName(u"pushSideReports")
        self.pushSideReports.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/google_files.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideReports.setIcon(icon4)
        self.pushSideReports.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideReports)

        self.verticalSpacer = QSpacerItem(20, 476, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushSideAbout = QPushButton(self.sideBar)
        self.pushSideAbout.setObjectName(u"pushSideAbout")
        icon5 = QIcon()
        icon5.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/xfinity_my_account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideAbout.setIcon(icon5)
        self.pushSideAbout.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideAbout)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.mainWidget = QWidget(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelTittle = QLabel(self.mainWidget)
        self.labelTittle.setObjectName(u"labelTittle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelTittle.setFont(font)
        self.labelTittle.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.labelTittle)

        self.stackedWidget = QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(870, 550))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.mainWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Payroll - Module", None))
        self.actionMasters.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionDonate.setText(QCoreApplication.translate("MainWindow", u"About Me", None))
        self.actionAbout_Me.setText(QCoreApplication.translate("MainWindow", u"About Me", None))
        self.actionBasic_Salary.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.actionDeduction.setText(QCoreApplication.translate("MainWindow", u"Deductions", None))
        self.actionBenefits.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.actionIncome_Tax.setText(QCoreApplication.translate("MainWindow", u"Tax", None))
        self.actionSetting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSite.setText(QCoreApplication.translate("MainWindow", u"Site", None))
        self.actionPosition.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.actionReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label.setText("")
        self.pushSideDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushSideMasters.setText(QCoreApplication.translate("MainWindow", u"Master", None))
        self.pushSideTransactions.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.pushSideReports.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.pushSideAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.labelTittle.setText(QCoreApplication.translate("MainWindow", u"Payroll Management Module - PT. Tanjung Redeb Hutani", None))
    # retranslateUi

