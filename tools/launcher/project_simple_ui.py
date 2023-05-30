# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_simple.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(228, 84)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QWidget#Form{\n"
"	margin: 3px;\n"
"}\n"
"QWidget{\n"
"	background: solid rgb(30,30,30);\n"
"	color: rgb(133,133,133);\n"
"	border-radius: 10px;\n"
"	selection-color:  rgb(105, 179, 71);\n"
"}\n"
"QPushButton{\n"
"	border-style: outset; \n"
"	border-width: 0px; \n"
"	color: rgb(133,133,133);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid rgb(55,55,55);\n"
"	padding-bottom: 3px;\n"
"}\n"
"QComboBox {\n"
"    border: 2px solid rgb(133,133,133);\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"	color: solid rgb(30,30,30);\n"
"}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: solid rgb(133,133,133)\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: solid rgb(133,133,133)\n"
"}\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"	background-color: rgb(133,133,133);\n"
"    "
                        "border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/resources/drop_arrow.png);\n"
"	width: 15px;\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main = QGridLayout()
        self.main.setObjectName(u"main")
        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy1)
        self.image.setMinimumSize(QSize(64, 64))
        self.image.setMaximumSize(QSize(64, 64))
        self.image.setScaledContents(True)

        self.main.addWidget(self.image, 0, 0, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open = QPushButton(Form)
        self.open.setObjectName(u"open")
        self.open.setMinimumSize(QSize(28, 28))
        self.open.setMaximumSize(QSize(28, 28))
        self.open.setStyleSheet(u"")
        self.open.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.open)

        self.info = QPushButton(Form)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(28, 28))
        self.info.setMaximumSize(QSize(28, 28))
        self.info.setStyleSheet(u"")
        self.info.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.info)

        self.output = QPushButton(Form)
        self.output.setObjectName(u"output")
        self.output.setMinimumSize(QSize(28, 28))
        self.output.setMaximumSize(QSize(28, 28))
        self.output.setStyleSheet(u"")
        self.output.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.output)

        self.status = QLabel(Form)
        self.status.setObjectName(u"status")

        self.horizontalLayout.addWidget(self.status)


        self.main.addLayout(self.horizontalLayout, 0, 1, 1, 3)

        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"color: rgb(212,212,212)")

        self.main.addWidget(self.name, 1, 1, 1, 3)


        self.gridLayout_2.addLayout(self.main, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText(QCoreApplication.translate("Form", u"Image", None))
#if QT_CONFIG(tooltip)
        self.open.setToolTip(QCoreApplication.translate("Form", u"open root directory", None))
#endif // QT_CONFIG(tooltip)
        self.open.setText("")
#if QT_CONFIG(tooltip)
        self.info.setToolTip(QCoreApplication.translate("Form", u"open info website", None))
#endif // QT_CONFIG(tooltip)
        self.info.setText("")
#if QT_CONFIG(tooltip)
        self.output.setToolTip(QCoreApplication.translate("Form", u"open output website", None))
#endif // QT_CONFIG(tooltip)
        self.output.setText("")
#if QT_CONFIG(tooltip)
        self.status.setToolTip(QCoreApplication.translate("Form", u"project status", None))
#endif // QT_CONFIG(tooltip)
        self.status.setText(QCoreApplication.translate("Form", u"default", None))
#if QT_CONFIG(tooltip)
        self.name.setToolTip(QCoreApplication.translate("Form", u"project name", None))
#endif // QT_CONFIG(tooltip)
        self.name.setText(QCoreApplication.translate("Form", u"S444_246_Persil_Proclean", None))
    # retranslateUi

