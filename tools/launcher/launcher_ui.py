# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_launcher(object):
    def setupUi(self, launcher):
        if not launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.resize(536, 422)
        launcher.setStyleSheet(u"")
        self.gridLayout = QGridLayout(launcher)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search = QLineEdit(launcher)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(256, 0))
        self.search.setMaximumSize(QSize(16777215, 16777215))
        self.search.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.search, 0, 0, 1, 1)

        self.prj_list = QListWidget(launcher)
        self.prj_list.setObjectName(u"prj_list")
        self.prj_list.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.prj_list, 1, 0, 1, 1)

        self.prj_grp = QGroupBox(launcher)
        self.prj_grp.setObjectName(u"prj_grp")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prj_grp.sizePolicy().hasHeightForWidth())
        self.prj_grp.setSizePolicy(sizePolicy)
        self.prj_grp.setMinimumSize(QSize(256, 0))
        self.gridLayout_3 = QGridLayout(self.prj_grp)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gl_prj_grp = QGridLayout()
        self.gl_prj_grp.setObjectName(u"gl_prj_grp")

        self.gridLayout_3.addLayout(self.gl_prj_grp, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.prj_grp, 0, 1, 2, 1)


        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)
    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"Launcher", None))
        self.search.setPlaceholderText(QCoreApplication.translate("launcher", u"Search", None))
        self.prj_grp.setTitle("")
    # retranslateUi

