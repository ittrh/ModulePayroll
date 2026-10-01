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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 728)
        icon = QIcon()
        icon.addFile(u":/ico/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 2, 4, 0)
        self.sideBar = QWidget(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMaximumSize(QSize(134, 16777215))
        self.sideBar.setStyleSheet(u"QPushButton{\n"
"	font-weight:bold;\n"
"	text-align:left;\n"
"}")
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

        self.pushSidePayroll = QPushButton(self.sideBar)
        self.pushSidePayroll.setObjectName(u"pushSidePayroll")
        self.pushSidePayroll.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/picpay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSidePayroll.setIcon(icon2)
        self.pushSidePayroll.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSidePayroll)

        self.verticalSpacer = QSpacerItem(20, 476, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushSideLogout = QPushButton(self.sideBar)
        self.pushSideLogout.setObjectName(u"pushSideLogout")
        icon3 = QIcon()
        icon3.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/aptoide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushSideLogout.setIcon(icon3)
        self.pushSideLogout.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushSideLogout)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelTittle = QLabel(self.widget_2)
        self.labelTittle.setObjectName(u"labelTittle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelTittle.setFont(font)

        self.verticalLayout_3.addWidget(self.labelTittle)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(870, 550))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuReports = QMenu(self.menubar)
        self.menuReports.setObjectName(u"menuReports")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionMasters)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionBasic_Salary)
        self.menuSettings.addAction(self.actionDeduction)
        self.menuSettings.addAction(self.actionBenefits)
        self.menuSettings.addAction(self.actionIncome_Tax)
        self.menuHelp.addAction(self.actionDonate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Payroll - Module", None))
        self.actionMasters.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionDonate.setText(QCoreApplication.translate("MainWindow", u"Donate", None))
        self.actionAbout_Me.setText(QCoreApplication.translate("MainWindow", u"About Me", None))
        self.actionBasic_Salary.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.actionDeduction.setText(QCoreApplication.translate("MainWindow", u"Deductions", None))
        self.actionBenefits.setText(QCoreApplication.translate("MainWindow", u"Benefits", None))
        self.actionIncome_Tax.setText(QCoreApplication.translate("MainWindow", u"Tax", None))
        self.label.setText("")
        self.pushSideDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushSidePayroll.setText(QCoreApplication.translate("MainWindow", u"Payroll", None))
        self.pushSideLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.labelTittle.setText(QCoreApplication.translate("MainWindow", u"Modul Payroll PT. Tanjung Redeb Hutani", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Created by IT PT. Tanjung Redeb Hutani - Code by Restu Ardananto \u00a9 2026", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuReports.setTitle(QCoreApplication.translate("MainWindow", u"Reports", None))
    # retranslateUi

