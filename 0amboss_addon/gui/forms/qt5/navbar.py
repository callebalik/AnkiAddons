# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'build/dist/designer/navbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NavBar(object):
    def setupUi(self, NavBar):
        NavBar.setObjectName("NavBar")
        self.gridLayout_2 = QtWidgets.QGridLayout(NavBar)
        self.gridLayout_2.setContentsMargins(8, 0, 8, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_back = QtWidgets.QPushButton(NavBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMinimumSize(QtCore.QSize(24, 24))
        self.button_back.setMaximumSize(QtCore.QSize(24, 24))
        self.button_back.setText("")
        self.button_back.setIconSize(QtCore.QSize(24, 24))
        self.button_back.setObjectName("button_back")
        self.gridLayout_2.addWidget(self.button_back, 0, 0, 1, 1)
        self.button_forward = QtWidgets.QPushButton(NavBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_forward.sizePolicy().hasHeightForWidth())
        self.button_forward.setSizePolicy(sizePolicy)
        self.button_forward.setMinimumSize(QtCore.QSize(24, 24))
        self.button_forward.setMaximumSize(QtCore.QSize(24, 24))
        self.button_forward.setText("")
        self.button_forward.setIconSize(QtCore.QSize(24, 24))
        self.button_forward.setObjectName("button_forward")
        self.gridLayout_2.addWidget(self.button_forward, 0, 1, 1, 1)
        self.label_title = QtWidgets.QLabel(NavBar)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 3, 1, 1)
        self.button_home = QtWidgets.QPushButton(NavBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_home.sizePolicy().hasHeightForWidth())
        self.button_home.setSizePolicy(sizePolicy)
        self.button_home.setMinimumSize(QtCore.QSize(24, 24))
        self.button_home.setMaximumSize(QtCore.QSize(24, 24))
        self.button_home.setText("")
        self.button_home.setIconSize(QtCore.QSize(24, 24))
        self.button_home.setObjectName("button_home")
        self.gridLayout_2.addWidget(self.button_home, 0, 2, 1, 1)
        self.button_external = QtWidgets.QPushButton(NavBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_external.sizePolicy().hasHeightForWidth())
        self.button_external.setSizePolicy(sizePolicy)
        self.button_external.setMinimumSize(QtCore.QSize(24, 24))
        self.button_external.setMaximumSize(QtCore.QSize(24, 24))
        self.button_external.setText("")
        self.button_external.setIconSize(QtCore.QSize(24, 24))
        self.button_external.setObjectName("button_external")
        self.gridLayout_2.addWidget(self.button_external, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(48, 24, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)

        self.retranslateUi(NavBar)
        QtCore.QMetaObject.connectSlotsByName(NavBar)

    def retranslateUi(self, NavBar):
        _translate = QtCore.QCoreApplication.translate
        NavBar.setWindowTitle(_translate("NavBar", "SidePanel"))
        self.button_back.setToolTip(_translate("NavBar", "One page back"))
        self.button_forward.setToolTip(_translate("NavBar", "One page forward"))
        self.label_title.setText(_translate("NavBar", "AMBOSS viewer"))
        self.button_home.setToolTip(_translate("NavBar", "Go to your dashboard"))
        self.button_external.setToolTip(_translate("NavBar", "Open current page in external browser"))
