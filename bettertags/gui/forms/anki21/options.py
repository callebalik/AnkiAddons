# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'build/dist/designer/options.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 589)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutBanner = QtWidgets.QHBoxLayout()
        self.layoutBanner.setObjectName("layoutBanner")
        self.labHeading = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labHeading.setFont(font)
        self.labHeading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labHeading.setIndent(2)
        self.labHeading.setObjectName("labHeading")
        self.layoutBanner.addWidget(self.labHeading)
        self.btnRate = QtWidgets.QToolButton(Dialog)
        self.btnRate.setMinimumSize(QtCore.QSize(24, 24))
        self.btnRate.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bettertags/icons/rate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRate.setIcon(icon)
        self.btnRate.setObjectName("btnRate")
        self.layoutBanner.addWidget(self.btnRate)
        self.btnTwitter = QtWidgets.QToolButton(Dialog)
        self.btnTwitter.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bettertags/icons/twitter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTwitter.setIcon(icon1)
        self.btnTwitter.setObjectName("btnTwitter")
        self.layoutBanner.addWidget(self.btnTwitter)
        self.btnYoutube = QtWidgets.QToolButton(Dialog)
        self.btnYoutube.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/bettertags/icons/youtube.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnYoutube.setIcon(icon2)
        self.btnYoutube.setIconSize(QtCore.QSize(18, 16))
        self.btnYoutube.setObjectName("btnYoutube")
        self.layoutBanner.addWidget(self.btnYoutube)
        self.btnHelp = QtWidgets.QToolButton(Dialog)
        self.btnHelp.setMinimumSize(QtCore.QSize(24, 24))
        self.btnHelp.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/bettertags/icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHelp.setIcon(icon3)
        self.btnHelp.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnHelp.setArrowType(QtCore.Qt.NoArrow)
        self.btnHelp.setObjectName("btnHelp")
        self.layoutBanner.addWidget(self.btnHelp)
        self.verticalLayout.addLayout(self.layoutBanner)
        self.layoutSocialBtns = QtWidgets.QHBoxLayout()
        self.layoutSocialBtns.setObjectName("layoutSocialBtns")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutSocialBtns.addItem(spacerItem)
        self.fmtLabInfo = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.fmtLabInfo.setFont(font)
        self.fmtLabInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fmtLabInfo.setObjectName("fmtLabInfo")
        self.layoutSocialBtns.addWidget(self.fmtLabInfo)
        self.verticalLayout.addLayout(self.layoutSocialBtns)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contribLayout = QtWidgets.QVBoxLayout()
        self.contribLayout.setContentsMargins(-1, 10, -1, 5)
        self.contribLayout.setObjectName("contribLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.labHeart = QtWidgets.QLabel(self.tab)
        self.labHeart.setText("")
        self.labHeart.setPixmap(QtGui.QPixmap(":/bettertags/icons/heart.svg"))
        self.labHeart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labHeart.setObjectName("labHeart")
        self.horizontalLayout_3.addWidget(self.labHeart)
        self.fmtLabContrib = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fmtLabContrib.setFont(font)
        self.fmtLabContrib.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fmtLabContrib.setObjectName("fmtLabContrib")
        self.horizontalLayout_3.addWidget(self.fmtLabContrib)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.contribLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnCoffee = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCoffee.setFont(font)
        self.btnCoffee.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/bettertags/icons/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCoffee.setIcon(icon4)
        self.btnCoffee.setIconSize(QtCore.QSize(32, 32))
        self.btnCoffee.setObjectName("btnCoffee")
        self.gridLayout_3.addWidget(self.btnCoffee, 0, 2, 1, 1)
        self.btnPatreon = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnPatreon.setFont(font)
        self.btnPatreon.setFocusPolicy(QtCore.Qt.NoFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/bettertags/icons/patreon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPatreon.setIcon(icon5)
        self.btnPatreon.setIconSize(QtCore.QSize(32, 32))
        self.btnPatreon.setObjectName("btnPatreon")
        self.gridLayout_3.addWidget(self.btnPatreon, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.contribLayout.addLayout(self.gridLayout_3)
        self.verticalLayout_5.addLayout(self.contribLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.layoutHotkey = QtWidgets.QGridLayout()
        self.layoutHotkey.setObjectName("layoutHotkey")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.layoutHotkey.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.layoutHotkey.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.layoutHotkey.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.layoutHotkey.addWidget(self.label_10, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.layoutHotkey.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.layoutHotkey.addWidget(self.label_11, 4, 0, 1, 2)
        self.hotkey_replace = QKeyGrabButton(self.groupBox_4)
        self.hotkey_replace.setFocusPolicy(QtCore.Qt.TabFocus)
        self.hotkey_replace.setText("")
        self.hotkey_replace.setObjectName("hotkey_replace")
        self.layoutHotkey.addWidget(self.hotkey_replace, 2, 1, 1, 1)
        self.hotkey_refresh = QKeyGrabButton(self.groupBox_4)
        self.hotkey_refresh.setFocusPolicy(QtCore.Qt.TabFocus)
        self.hotkey_refresh.setText("")
        self.hotkey_refresh.setObjectName("hotkey_refresh")
        self.layoutHotkey.addWidget(self.hotkey_refresh, 3, 1, 1, 1)
        self.hotkey_delete = QKeyGrabButton(self.groupBox_4)
        self.hotkey_delete.setFocusPolicy(QtCore.Qt.TabFocus)
        self.hotkey_delete.setText("")
        self.hotkey_delete.setObjectName("hotkey_delete")
        self.layoutHotkey.addWidget(self.hotkey_delete, 5, 1, 1, 1)
        self.hotkey_rename = QKeyGrabButton(self.groupBox_4)
        self.hotkey_rename.setFocusPolicy(QtCore.Qt.TabFocus)
        self.hotkey_rename.setText("")
        self.hotkey_rename.setObjectName("hotkey_rename")
        self.layoutHotkey.addWidget(self.hotkey_rename, 6, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.layoutHotkey)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cb_enable_sidebar = QtWidgets.QGroupBox(self.tab_5)
        self.cb_enable_sidebar.setCheckable(True)
        self.cb_enable_sidebar.setObjectName("cb_enable_sidebar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.cb_enable_sidebar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.cb_enable_sidebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.cb_enable_sidebar)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.sel_tag_expansion = QtWidgets.QComboBox(self.cb_enable_sidebar)
        self.sel_tag_expansion.setObjectName("sel_tag_expansion")
        self.sel_tag_expansion.addItem("")
        self.sel_tag_expansion.addItem("")
        self.sel_tag_expansion.addItem("")
        self.horizontalLayout.addWidget(self.sel_tag_expansion)
        self.horizontalLayout.setStretch(2, 6)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.cb_confirm_deletion = QtWidgets.QCheckBox(self.cb_enable_sidebar)
        self.cb_confirm_deletion.setObjectName("cb_confirm_deletion")
        self.verticalLayout_9.addWidget(self.cb_confirm_deletion)
        self.verticalLayout_8.addWidget(self.cb_enable_sidebar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cb_enable_completer = QtWidgets.QGroupBox(self.tab_4)
        self.cb_enable_completer.setCheckable(True)
        self.cb_enable_completer.setObjectName("cb_enable_completer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.cb_enable_completer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cb_completer_substrings = QtWidgets.QCheckBox(self.cb_enable_completer)
        self.cb_completer_substrings.setObjectName("cb_completer_substrings")
        self.verticalLayout_6.addWidget(self.cb_completer_substrings)
        self.cb_completer_workaround = QtWidgets.QCheckBox(self.cb_enable_completer)
        self.cb_completer_workaround.setObjectName("cb_completer_workaround")
        self.verticalLayout_6.addWidget(self.cb_completer_workaround)
        self.verticalLayout_7.addWidget(self.cb_enable_completer)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem9)
        self.line = QtWidgets.QFrame(self.tab_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem10)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.le_separator = QtWidgets.QLineEdit(self.groupBox)
        self.le_separator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_separator.setObjectName("le_separator")
        self.gridLayout_2.addWidget(self.le_separator, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_7.addWidget(self.groupBox)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.htmlAbout = QtWidgets.QTextBrowser(self.tab_3)
        self.htmlAbout.setOpenExternalLinks(True)
        self.htmlAbout.setObjectName("htmlAbout")
        self.verticalLayout_3.addWidget(self.htmlAbout)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.cb_enable_sidebar)
        Dialog.setTabOrder(self.cb_enable_sidebar, self.cb_enable_completer)
        Dialog.setTabOrder(self.cb_enable_completer, self.cb_completer_substrings)
        Dialog.setTabOrder(self.cb_completer_substrings, self.cb_completer_workaround)
        Dialog.setTabOrder(self.cb_completer_workaround, self.le_separator)
        Dialog.setTabOrder(self.le_separator, self.htmlAbout)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BetterTags Settings"))
        self.labHeading.setText(_translate("Dialog", "BetterTags Settings"))
        self.btnRate.setToolTip(_translate("Dialog", "<html>Please leave a thumbs-up if you\'ve enjoyed this add-on</html>"))
        self.btnRate.setText(_translate("Dialog", "Rate"))
        self.btnTwitter.setToolTip(_translate("Dialog", "<html>Follow me on Twitter for <br>updates on add-on releases and news on Anki in general!</html>"))
        self.btnTwitter.setText(_translate("Dialog", "Twitter"))
        self.btnYoutube.setToolTip(_translate("Dialog", "<html>Check out my YouTube channel for<br>helpful tutorials on this add-on and more</html>"))
        self.btnYoutube.setText(_translate("Dialog", "YouTube"))
        self.btnHelp.setToolTip(_translate("Dialog", "<html>Invoke the wiki page, add-on description, or manual</html>"))
        self.btnHelp.setText(_translate("Dialog", "?"))
        self.btnHelp.setShortcut(_translate("Dialog", "Ctrl+H"))
        self.fmtLabInfo.setText(_translate("Dialog", "BetterTags v{ADDON_VERSION} by Glutanimate "))
        self.fmtLabContrib.setText(_translate("Dialog", "{ADDON_NAME}?"))
        self.btnCoffee.setToolTip(_translate("Dialog", "Each coffee helps. Thank you!"))
        self.btnCoffee.setText(_translate("Dialog", "Fuel my work\n"
"with a coffee"))
        self.btnPatreon.setToolTip(_translate("Dialog", "Perks include access to Patron-only add-ons, <br>exclusive blog posts, mentions in the credits, and more!"))
        self.btnPatreon.setText(_translate("Dialog", "Become a Patron\n"
"&& receive cool perks!"))
        self.groupBox_4.setTitle(_translate("Dialog", "Hotkeys"))
        self.label_9.setText(_translate("Dialog", "Changes will take effect after reopening the resp. window"))
        self.label_6.setText(_translate("Dialog", "Rename tag"))
        self.label_4.setText(_translate("Dialog", "Delete tag"))
        self.label_3.setText(_translate("Dialog", "Refresh tags"))
        self.label_10.setText(_translate("Dialog", "Browser general"))
        self.label_5.setText(_translate("Dialog", "Find and replace tags"))
        self.label_11.setText(_translate("Dialog", "Browser sidebar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "&General"))
        self.cb_enable_sidebar.setToolTip(_translate("Dialog", "<html><head/><body><p>To completely disable/enable sidebar modifications you will have to restart Anki</p></body></html>"))
        self.cb_enable_sidebar.setTitle(_translate("Dialog", "Enable sidebar modifications (requires Anki restart)"))
        self.label.setText(_translate("Dialog", "Tags"))
        self.label_2.setText(_translate("Dialog", "Default tag expansion behavior:"))
        self.sel_tag_expansion.setToolTip(_translate("Dialog", "<html><head/><body><p>&quot;Restore state&quot; remembers the previous expansion state, whereas &quot;Collapse all&quot; and &quot;Expand all&quot; ignore it</p></body></html>"))
        self.sel_tag_expansion.setItemText(0, _translate("Dialog", "Restore state"))
        self.sel_tag_expansion.setItemText(1, _translate("Dialog", "Collapse all"))
        self.sel_tag_expansion.setItemText(2, _translate("Dialog", "Expand all"))
        self.cb_confirm_deletion.setText(_translate("Dialog", "Ask for confirmation before deleting tags"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "&Sidebar"))
        self.cb_enable_completer.setToolTip(_translate("Dialog", "<html><head/><body><p>To completely disable/enable tag completer modifications you will have to restart Anki</p></body></html>"))
        self.cb_enable_completer.setTitle(_translate("Dialog", "Enable tag completer modifications (requires Anki restart)"))
        self.cb_completer_substrings.setToolTip(_translate("Dialog", "<html><head/><body><p>Rather than going by tag hierarchies, match any substring within your tags</p></body></html>"))
        self.cb_completer_substrings.setText(_translate("Dialog", "Match arbitrary &substrings"))
        self.cb_completer_workaround.setToolTip(_translate("Dialog", "<html><head/><body><p>Fixes the appearance of tag completions on some platforms, but might not look as pretty</p></body></html>"))
        self.cb_completer_workaround.setText(_translate("Dialog", "Enable match highlighting &workaround"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Warning</span>: The settings below are advanced and you should only adjust them if you know what you\'re doing.</p></body></html>"))
        self.groupBox.setToolTip(_translate("Dialog", "<html><head/><body><p>Tread carefully!</p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "I understand and want to proceed"))
        self.label_8.setText(_translate("Dialog", "Hierarchical Tags Separator\n"
"(requires Anki restart)"))
        self.le_separator.setToolTip(_translate("Dialog", "<html><head/><body><p>The sequence of characters used to separate individual tag components in a hierarchy</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "&Other"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "A&bout"))


from ....libaddon.gui.basic.widgets.qkeygrabber import QKeyGrabButton