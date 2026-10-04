# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PayrollTabSalary.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import src.ui.PayrollResource

class Ui_PayrollTabSalary(object):
    def setupUi(self, PayrollTabSalary):
        if not PayrollTabSalary.objectName():
            PayrollTabSalary.setObjectName(u"PayrollTabSalary")
        PayrollTabSalary.resize(1077, 788)
        self.horizontalLayout_11 = QHBoxLayout(PayrollTabSalary)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, -1)
        self.widget = QWidget(PayrollTabSalary)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(280, 0))
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setPixmap(QPixmap(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_device_search.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.editCari = QLineEdit(self.widget)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.editCari)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableEmployee = QTableView(self.widget)
        self.tableEmployee.setObjectName(u"tableEmployee")
        self.tableEmployee.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.tableEmployee)


        self.horizontalLayout_11.addWidget(self.widget)

        self.widget_2 = QWidget(PayrollTabSalary)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalIdentitas = QVBoxLayout()
        self.verticalIdentitas.setObjectName(u"verticalIdentitas")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setUnderline(True)
        self.label_6.setFont(font1)

        self.verticalIdentitas.addWidget(self.label_6)

        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalIdentitas.addWidget(self.line_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.labelNama = QLabel(self.widget_2)
        self.labelNama.setObjectName(u"labelNama")
        self.labelNama.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelNama)


        self.verticalIdentitas.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.labelNik = QLabel(self.widget_2)
        self.labelNik.setObjectName(u"labelNik")
        self.labelNik.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.labelNik)


        self.verticalIdentitas.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.labelBidang = QLabel(self.widget_2)
        self.labelBidang.setObjectName(u"labelBidang")
        self.labelBidang.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.labelBidang)


        self.verticalIdentitas.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.labelStatus = QLabel(self.widget_2)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.labelStatus)


        self.verticalIdentitas.addLayout(self.horizontalLayout_10)

        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalIdentitas.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.labelPenghasilan = QLabel(self.widget_2)
        self.labelPenghasilan.setObjectName(u"labelPenghasilan")
        self.labelPenghasilan.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.labelPenghasilan)


        self.verticalIdentitas.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.labelPotongan = QLabel(self.widget_2)
        self.labelPotongan.setObjectName(u"labelPotongan")
        self.labelPotongan.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.labelPotongan)


        self.verticalIdentitas.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setBold(True)
        self.label_8.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.labelDiterima = QLabel(self.widget_2)
        self.labelDiterima.setObjectName(u"labelDiterima")
        self.labelDiterima.setFont(font2)
        self.labelDiterima.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.labelDiterima)


        self.verticalIdentitas.addLayout(self.horizontalLayout_5)

        self.line_4 = QFrame(self.widget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalIdentitas.addWidget(self.line_4)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/icons-dark/images/Appstract-master/icons/appstract-dark/blackberry_hub_notes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.verticalIdentitas.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalIdentitas.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalIdentitas)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_9)

        self.tablePenghasilan = QTableView(self.widget_2)
        self.tablePenghasilan.setObjectName(u"tablePenghasilan")
        self.tablePenghasilan.setMinimumSize(QSize(0, 250))

        self.verticalLayout_4.addWidget(self.tablePenghasilan)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_12)

        self.tablePotongan = QTableView(self.widget_2)
        self.tablePotongan.setObjectName(u"tablePotongan")
        self.tablePotongan.setMinimumSize(QSize(0, 250))

        self.verticalLayout_5.addWidget(self.tablePotongan)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_11.addWidget(self.widget_2)


        self.retranslateUi(PayrollTabSalary)

        QMetaObject.connectSlotsByName(PayrollTabSalary)
    # setupUi

    def retranslateUi(self, PayrollTabSalary):
        PayrollTabSalary.setWindowTitle(QCoreApplication.translate("PayrollTabSalary", u"Payroll - Salary", None))
        self.label_2.setText("")
        self.editCari.setPlaceholderText(QCoreApplication.translate("PayrollTabSalary", u"Cari ...", None))
        self.label_3.setText(QCoreApplication.translate("PayrollTabSalary", u"Review Salary", None))
        self.label_6.setText(QCoreApplication.translate("PayrollTabSalary", u"Data Karyawan", None))
        self.label_13.setText(QCoreApplication.translate("PayrollTabSalary", u"Nama :", None))
        self.labelNama.setText(QCoreApplication.translate("PayrollTabSalary", u"None", None))
        self.label_14.setText(QCoreApplication.translate("PayrollTabSalary", u"No. Pegawai :", None))
        self.labelNik.setText(QCoreApplication.translate("PayrollTabSalary", u"None", None))
        self.label_15.setText(QCoreApplication.translate("PayrollTabSalary", u"Bidang :", None))
        self.labelBidang.setText(QCoreApplication.translate("PayrollTabSalary", u"None", None))
        self.label_16.setText(QCoreApplication.translate("PayrollTabSalary", u"Status :", None))
        self.labelStatus.setText(QCoreApplication.translate("PayrollTabSalary", u"None", None))
        self.label.setText(QCoreApplication.translate("PayrollTabSalary", u"Penghasilan :", None))
        self.label_5.setText(QCoreApplication.translate("PayrollTabSalary", u"Rp.", None))
        self.labelPenghasilan.setText(QCoreApplication.translate("PayrollTabSalary", u"0", None))
        self.label_7.setText(QCoreApplication.translate("PayrollTabSalary", u"Potongan :", None))
        self.label_10.setText(QCoreApplication.translate("PayrollTabSalary", u"Rp.", None))
        self.labelPotongan.setText(QCoreApplication.translate("PayrollTabSalary", u"0", None))
        self.label_8.setText(QCoreApplication.translate("PayrollTabSalary", u"Diterima :", None))
        self.label_11.setText(QCoreApplication.translate("PayrollTabSalary", u"Rp.", None))
        self.labelDiterima.setText(QCoreApplication.translate("PayrollTabSalary", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("PayrollTabSalary", u"Edit", None))
        self.label_9.setText(QCoreApplication.translate("PayrollTabSalary", u"Penghasilan", None))
        self.label_12.setText(QCoreApplication.translate("PayrollTabSalary", u"Potongan", None))
    # retranslateUi

