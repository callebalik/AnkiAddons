# Form implementation generated from reading ui file 'build/dist/designer/anki_simulator_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_simulator_dialog(object):
    def setupUi(self, simulator_dialog):
        simulator_dialog.setObjectName("simulator_dialog")
        simulator_dialog.resize(1168, 790)
        self.verticalLayout = QtWidgets.QVBoxLayout(simulator_dialog)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolbar = QtWidgets.QWidget(parent=simulator_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setObjectName("toolbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbar)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deckChooser = QtWidgets.QWidget(parent=self.toolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckChooser.sizePolicy().hasHeightForWidth())
        self.deckChooser.setSizePolicy(sizePolicy)
        self.deckChooser.setObjectName("deckChooser")
        self.horizontalLayout.addWidget(self.deckChooser)
        self.loadDeckConfigurationsButton = QtWidgets.QPushButton(parent=self.toolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadDeckConfigurationsButton.sizePolicy().hasHeightForWidth())
        self.loadDeckConfigurationsButton.setSizePolicy(sizePolicy)
        self.loadDeckConfigurationsButton.setObjectName("loadDeckConfigurationsButton")
        self.horizontalLayout.addWidget(self.loadDeckConfigurationsButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.manualButton = QtWidgets.QPushButton(parent=self.toolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualButton.sizePolicy().hasHeightForWidth())
        self.manualButton.setSizePolicy(sizePolicy)
        self.manualButton.setObjectName("manualButton")
        self.horizontalLayout.addWidget(self.manualButton)
        self.aboutButton = QtWidgets.QPushButton(parent=self.toolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout.addWidget(self.aboutButton)
        self.supportButton = QtWidgets.QPushButton(parent=self.toolbar)
        self.supportButton.setObjectName("supportButton")
        self.horizontalLayout.addWidget(self.supportButton)
        self.verticalLayout.addWidget(self.toolbar)
        self.form = QtWidgets.QWidget(parent=simulator_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form.sizePolicy().hasHeightForWidth())
        self.form.setSizePolicy(sizePolicy)
        self.form.setObjectName("form")
        self.gridLayout = QtWidgets.QGridLayout(self.form)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.learningStepsTextfield = QtWidgets.QLineEdit(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.learningStepsTextfield.sizePolicy().hasHeightForWidth())
        self.learningStepsTextfield.setSizePolicy(sizePolicy)
        self.learningStepsTextfield.setMinimumSize(QtCore.QSize(100, 0))
        self.learningStepsTextfield.setMaximumSize(QtCore.QSize(160, 16777215))
        self.learningStepsTextfield.setObjectName("learningStepsTextfield")
        self.gridLayout.addWidget(self.learningStepsTextfield, 3, 3, 1, 1)
        self.newLapseIntervalSpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLapseIntervalSpinbox.sizePolicy().hasHeightForWidth())
        self.newLapseIntervalSpinbox.setSizePolicy(sizePolicy)
        self.newLapseIntervalSpinbox.setPrefix("")
        self.newLapseIntervalSpinbox.setMaximum(100)
        self.newLapseIntervalSpinbox.setSingleStep(10)
        self.newLapseIntervalSpinbox.setProperty("value", 60)
        self.newLapseIntervalSpinbox.setObjectName("newLapseIntervalSpinbox")
        self.gridLayout.addWidget(self.newLapseIntervalSpinbox, 3, 6, 1, 1)
        self.maximumReviewsPerDaySpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximumReviewsPerDaySpinbox.sizePolicy().hasHeightForWidth())
        self.maximumReviewsPerDaySpinbox.setSizePolicy(sizePolicy)
        self.maximumReviewsPerDaySpinbox.setSuffix("")
        self.maximumReviewsPerDaySpinbox.setPrefix("")
        self.maximumReviewsPerDaySpinbox.setMinimum(0)
        self.maximumReviewsPerDaySpinbox.setMaximum(9999)
        self.maximumReviewsPerDaySpinbox.setSingleStep(1)
        self.maximumReviewsPerDaySpinbox.setProperty("value", 9999)
        self.maximumReviewsPerDaySpinbox.setObjectName("maximumReviewsPerDaySpinbox")
        self.gridLayout.addWidget(self.maximumReviewsPerDaySpinbox, 2, 3, 1, 1)
        self.graduatingIntervalSpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graduatingIntervalSpinbox.sizePolicy().hasHeightForWidth())
        self.graduatingIntervalSpinbox.setSizePolicy(sizePolicy)
        self.graduatingIntervalSpinbox.setSuffix("")
        self.graduatingIntervalSpinbox.setPrefix("")
        self.graduatingIntervalSpinbox.setMinimum(1)
        self.graduatingIntervalSpinbox.setMaximum(9999)
        self.graduatingIntervalSpinbox.setSingleStep(1)
        self.graduatingIntervalSpinbox.setProperty("value", 20)
        self.graduatingIntervalSpinbox.setObjectName("graduatingIntervalSpinbox")
        self.gridLayout.addWidget(self.graduatingIntervalSpinbox, 2, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.maximumIntervalLabel = QtWidgets.QLabel(parent=self.form)
        self.maximumIntervalLabel.setObjectName("maximumIntervalLabel")
        self.gridLayout.addWidget(self.maximumIntervalLabel, 5, 5, 1, 1)
        self.intervalModifierLabel = QtWidgets.QLabel(parent=self.form)
        self.intervalModifierLabel.setObjectName("intervalModifierLabel")
        self.gridLayout.addWidget(self.intervalModifierLabel, 5, 0, 1, 1)
        self.startingEaseSpinBox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startingEaseSpinBox.sizePolicy().hasHeightForWidth())
        self.startingEaseSpinBox.setSizePolicy(sizePolicy)
        self.startingEaseSpinBox.setPrefix("")
        self.startingEaseSpinBox.setMinimum(130)
        self.startingEaseSpinBox.setMaximum(999)
        self.startingEaseSpinBox.setSingleStep(10)
        self.startingEaseSpinBox.setProperty("value", 250)
        self.startingEaseSpinBox.setObjectName("startingEaseSpinBox")
        self.gridLayout.addWidget(self.startingEaseSpinBox, 3, 1, 1, 1)
        self.maximumReviewsPerDayLabel = QtWidgets.QLabel(parent=self.form)
        self.maximumReviewsPerDayLabel.setObjectName("maximumReviewsPerDayLabel")
        self.gridLayout.addWidget(self.maximumReviewsPerDayLabel, 2, 2, 1, 1)
        self.lapseStepsTextfield = QtWidgets.QLineEdit(parent=self.form)
        self.lapseStepsTextfield.setMinimumSize(QtCore.QSize(100, 0))
        self.lapseStepsTextfield.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lapseStepsTextfield.setObjectName("lapseStepsTextfield")
        self.gridLayout.addWidget(self.lapseStepsTextfield, 5, 3, 1, 1)
        self.newLapseIntervalLabel = QtWidgets.QLabel(parent=self.form)
        self.newLapseIntervalLabel.setObjectName("newLapseIntervalLabel")
        self.gridLayout.addWidget(self.newLapseIntervalLabel, 3, 5, 1, 1)
        self.newCardsPerDayLabel = QtWidgets.QLabel(parent=self.form)
        self.newCardsPerDayLabel.setObjectName("newCardsPerDayLabel")
        self.gridLayout.addWidget(self.newCardsPerDayLabel, 2, 0, 1, 1)
        self.intervalModifierSpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalModifierSpinbox.sizePolicy().hasHeightForWidth())
        self.intervalModifierSpinbox.setSizePolicy(sizePolicy)
        self.intervalModifierSpinbox.setPrefix("")
        self.intervalModifierSpinbox.setMaximum(999)
        self.intervalModifierSpinbox.setSingleStep(10)
        self.intervalModifierSpinbox.setProperty("value", 100)
        self.intervalModifierSpinbox.setObjectName("intervalModifierSpinbox")
        self.gridLayout.addWidget(self.intervalModifierSpinbox, 5, 1, 1, 1)
        self.graduatingIntervalLabel = QtWidgets.QLabel(parent=self.form)
        self.graduatingIntervalLabel.setObjectName("graduatingIntervalLabel")
        self.gridLayout.addWidget(self.graduatingIntervalLabel, 2, 5, 1, 1)
        self.startingEaseLabel = QtWidgets.QLabel(parent=self.form)
        self.startingEaseLabel.setObjectName("startingEaseLabel")
        self.gridLayout.addWidget(self.startingEaseLabel, 3, 0, 1, 1)
        self.learningStepsLabel = QtWidgets.QLabel(parent=self.form)
        self.learningStepsLabel.setObjectName("learningStepsLabel")
        self.gridLayout.addWidget(self.learningStepsLabel, 3, 2, 1, 1)
        self.newCardsPerDaySpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newCardsPerDaySpinbox.sizePolicy().hasHeightForWidth())
        self.newCardsPerDaySpinbox.setSizePolicy(sizePolicy)
        self.newCardsPerDaySpinbox.setSuffix("")
        self.newCardsPerDaySpinbox.setPrefix("")
        self.newCardsPerDaySpinbox.setMinimum(0)
        self.newCardsPerDaySpinbox.setMaximum(9999)
        self.newCardsPerDaySpinbox.setSingleStep(1)
        self.newCardsPerDaySpinbox.setProperty("value", 60)
        self.newCardsPerDaySpinbox.setObjectName("newCardsPerDaySpinbox")
        self.gridLayout.addWidget(self.newCardsPerDaySpinbox, 2, 1, 1, 1)
        self.lapseStepsLabel = QtWidgets.QLabel(parent=self.form)
        self.lapseStepsLabel.setObjectName("lapseStepsLabel")
        self.gridLayout.addWidget(self.lapseStepsLabel, 5, 2, 1, 1)
        self.maximumIntervalSpinbox = QtWidgets.QSpinBox(parent=self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximumIntervalSpinbox.sizePolicy().hasHeightForWidth())
        self.maximumIntervalSpinbox.setSizePolicy(sizePolicy)
        self.maximumIntervalSpinbox.setSuffix("")
        self.maximumIntervalSpinbox.setPrefix("")
        self.maximumIntervalSpinbox.setMinimum(1)
        self.maximumIntervalSpinbox.setMaximum(9999)
        self.maximumIntervalSpinbox.setSingleStep(1)
        self.maximumIntervalSpinbox.setProperty("value", 365)
        self.maximumIntervalSpinbox.setObjectName("maximumIntervalSpinbox")
        self.gridLayout.addWidget(self.maximumIntervalSpinbox, 5, 6, 1, 1)
        self.verticalLayout.addWidget(self.form)
        self.widget = QtWidgets.QWidget(parent=simulator_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.percentCorrectLearningTextfield = QtWidgets.QLineEdit(parent=self.widget)
        self.percentCorrectLearningTextfield.setMinimumSize(QtCore.QSize(70, 0))
        self.percentCorrectLearningTextfield.setObjectName("percentCorrectLearningTextfield")
        self.gridLayout_4.addWidget(self.percentCorrectLearningTextfield, 2, 6, 1, 1)
        self.percentCorrectLapseTextfield = QtWidgets.QLineEdit(parent=self.widget)
        self.percentCorrectLapseTextfield.setMinimumSize(QtCore.QSize(70, 0))
        self.percentCorrectLapseTextfield.setObjectName("percentCorrectLapseTextfield")
        self.gridLayout_4.addWidget(self.percentCorrectLapseTextfield, 3, 6, 1, 1)
        self.percentCorrectYoungLabel = QtWidgets.QLabel(parent=self.widget)
        self.percentCorrectYoungLabel.setObjectName("percentCorrectYoungLabel")
        self.gridLayout_4.addWidget(self.percentCorrectYoungLabel, 2, 9, 1, 1)
        self.percentCorrectLearningLabel = QtWidgets.QLabel(parent=self.widget)
        self.percentCorrectLearningLabel.setObjectName("percentCorrectLearningLabel")
        self.gridLayout_4.addWidget(self.percentCorrectLearningLabel, 2, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 7, 1, 1)
        self.includeSuspendedNewCardsCheckbox = QtWidgets.QCheckBox(parent=self.widget)
        self.includeSuspendedNewCardsCheckbox.setChecked(True)
        self.includeSuspendedNewCardsCheckbox.setObjectName("includeSuspendedNewCardsCheckbox")
        self.gridLayout_4.addWidget(self.includeSuspendedNewCardsCheckbox, 2, 2, 1, 1)
        self.includeOverdueCardsCheckbox = QtWidgets.QCheckBox(parent=self.widget)
        self.includeOverdueCardsCheckbox.setObjectName("includeOverdueCardsCheckbox")
        self.gridLayout_4.addWidget(self.includeOverdueCardsCheckbox, 3, 2, 1, 1)
        self.simulateAdditionalNewCardsCheckbox = QtWidgets.QCheckBox(parent=self.widget)
        self.simulateAdditionalNewCardsCheckbox.setObjectName("simulateAdditionalNewCardsCheckbox")
        self.gridLayout_4.addWidget(self.simulateAdditionalNewCardsCheckbox, 5, 1, 1, 1)
        self.useActualCardsCheckbox = QtWidgets.QCheckBox(parent=self.widget)
        self.useActualCardsCheckbox.setChecked(True)
        self.useActualCardsCheckbox.setObjectName("useActualCardsCheckbox")
        self.gridLayout_4.addWidget(self.useActualCardsCheckbox, 2, 1, 1, 1)
        self.mockedNewCardsSpinbox = QtWidgets.QSpinBox(parent=self.widget)
        self.mockedNewCardsSpinbox.setEnabled(False)
        self.mockedNewCardsSpinbox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.mockedNewCardsSpinbox.setMinimum(0)
        self.mockedNewCardsSpinbox.setMaximum(99999999)
        self.mockedNewCardsSpinbox.setProperty("value", 1000)
        self.mockedNewCardsSpinbox.setObjectName("mockedNewCardsSpinbox")
        self.gridLayout_4.addWidget(self.mockedNewCardsSpinbox, 5, 2, 1, 1)
        self.percentCorrectLapseLabel = QtWidgets.QLabel(parent=self.widget)
        self.percentCorrectLapseLabel.setObjectName("percentCorrectLapseLabel")
        self.gridLayout_4.addWidget(self.percentCorrectLapseLabel, 3, 5, 1, 1)
        self.percentCorrectYoungSpinbox = QtWidgets.QSpinBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentCorrectYoungSpinbox.sizePolicy().hasHeightForWidth())
        self.percentCorrectYoungSpinbox.setSizePolicy(sizePolicy)
        self.percentCorrectYoungSpinbox.setPrefix("")
        self.percentCorrectYoungSpinbox.setMinimum(1)
        self.percentCorrectYoungSpinbox.setMaximum(100)
        self.percentCorrectYoungSpinbox.setSingleStep(1)
        self.percentCorrectYoungSpinbox.setProperty("value", 90)
        self.percentCorrectYoungSpinbox.setObjectName("percentCorrectYoungSpinbox")
        self.gridLayout_4.addWidget(self.percentCorrectYoungSpinbox, 2, 10, 1, 1)
        self.percentCorrectMatureLabel = QtWidgets.QLabel(parent=self.widget)
        self.percentCorrectMatureLabel.setObjectName("percentCorrectMatureLabel")
        self.gridLayout_4.addWidget(self.percentCorrectMatureLabel, 3, 9, 1, 1)
        self.percentCorrectMatureSpinbox = QtWidgets.QSpinBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentCorrectMatureSpinbox.sizePolicy().hasHeightForWidth())
        self.percentCorrectMatureSpinbox.setSizePolicy(sizePolicy)
        self.percentCorrectMatureSpinbox.setPrefix("")
        self.percentCorrectMatureSpinbox.setMinimum(1)
        self.percentCorrectMatureSpinbox.setMaximum(100)
        self.percentCorrectMatureSpinbox.setSingleStep(1)
        self.percentCorrectMatureSpinbox.setProperty("value", 90)
        self.percentCorrectMatureSpinbox.setObjectName("percentCorrectMatureSpinbox")
        self.gridLayout_4.addWidget(self.percentCorrectMatureSpinbox, 3, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 5, 1, 6)
        self.verticalLayout.addWidget(self.widget)
        self.buttons = QtWidgets.QWidget(parent=simulator_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.buttons)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.simulationTitleTextfield = QtWidgets.QLineEdit(parent=self.buttons)
        self.simulationTitleTextfield.setMaximumSize(QtCore.QSize(200, 16777215))
        self.simulationTitleTextfield.setObjectName("simulationTitleTextfield")
        self.horizontalLayout_2.addWidget(self.simulationTitleTextfield)
        self.daysToSimulateLabel = QtWidgets.QLabel(parent=self.buttons)
        self.daysToSimulateLabel.setObjectName("daysToSimulateLabel")
        self.horizontalLayout_2.addWidget(self.daysToSimulateLabel)
        self.daysToSimulateSpinbox = QtWidgets.QSpinBox(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daysToSimulateSpinbox.sizePolicy().hasHeightForWidth())
        self.daysToSimulateSpinbox.setSizePolicy(sizePolicy)
        self.daysToSimulateSpinbox.setSuffix("")
        self.daysToSimulateSpinbox.setPrefix("")
        self.daysToSimulateSpinbox.setMinimum(1)
        self.daysToSimulateSpinbox.setMaximum(9999)
        self.daysToSimulateSpinbox.setSingleStep(1)
        self.daysToSimulateSpinbox.setProperty("value", 180)
        self.daysToSimulateSpinbox.setObjectName("daysToSimulateSpinbox")
        self.horizontalLayout_2.addWidget(self.daysToSimulateSpinbox)
        self.simulateButton = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulateButton.sizePolicy().hasHeightForWidth())
        self.simulateButton.setSizePolicy(sizePolicy)
        self.simulateButton.setObjectName("simulateButton")
        self.horizontalLayout_2.addWidget(self.simulateButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.clearLastSimulationButton = QtWidgets.QPushButton(parent=self.buttons)
        self.clearLastSimulationButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLastSimulationButton.sizePolicy().hasHeightForWidth())
        self.clearLastSimulationButton.setSizePolicy(sizePolicy)
        self.clearLastSimulationButton.setObjectName("clearLastSimulationButton")
        self.horizontalLayout_2.addWidget(self.clearLastSimulationButton)
        self.clearAllSimulationButton = QtWidgets.QPushButton(parent=self.buttons)
        self.clearAllSimulationButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAllSimulationButton.sizePolicy().hasHeightForWidth())
        self.clearAllSimulationButton.setSizePolicy(sizePolicy)
        self.clearAllSimulationButton.setObjectName("clearAllSimulationButton")
        self.horizontalLayout_2.addWidget(self.clearAllSimulationButton)
        self.verticalLayout.addWidget(self.buttons)
        self.graphLayout = QtWidgets.QVBoxLayout()
        self.graphLayout.setSpacing(0)
        self.graphLayout.setObjectName("graphLayout")
        self.verticalLayout.addLayout(self.graphLayout)

        self.retranslateUi(simulator_dialog)
        self.useActualCardsCheckbox.toggled['bool'].connect(self.includeSuspendedNewCardsCheckbox.setEnabled) # type: ignore
        self.useActualCardsCheckbox.toggled['bool'].connect(self.includeOverdueCardsCheckbox.setEnabled) # type: ignore
        self.simulateAdditionalNewCardsCheckbox.toggled['bool'].connect(self.mockedNewCardsSpinbox.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(simulator_dialog)
        simulator_dialog.setTabOrder(self.newCardsPerDaySpinbox, self.startingEaseSpinBox)
        simulator_dialog.setTabOrder(self.startingEaseSpinBox, self.intervalModifierSpinbox)
        simulator_dialog.setTabOrder(self.intervalModifierSpinbox, self.maximumReviewsPerDaySpinbox)
        simulator_dialog.setTabOrder(self.maximumReviewsPerDaySpinbox, self.learningStepsTextfield)
        simulator_dialog.setTabOrder(self.learningStepsTextfield, self.lapseStepsTextfield)
        simulator_dialog.setTabOrder(self.lapseStepsTextfield, self.graduatingIntervalSpinbox)
        simulator_dialog.setTabOrder(self.graduatingIntervalSpinbox, self.newLapseIntervalSpinbox)
        simulator_dialog.setTabOrder(self.newLapseIntervalSpinbox, self.maximumIntervalSpinbox)
        simulator_dialog.setTabOrder(self.maximumIntervalSpinbox, self.useActualCardsCheckbox)
        simulator_dialog.setTabOrder(self.useActualCardsCheckbox, self.simulateAdditionalNewCardsCheckbox)
        simulator_dialog.setTabOrder(self.simulateAdditionalNewCardsCheckbox, self.includeSuspendedNewCardsCheckbox)
        simulator_dialog.setTabOrder(self.includeSuspendedNewCardsCheckbox, self.includeOverdueCardsCheckbox)
        simulator_dialog.setTabOrder(self.includeOverdueCardsCheckbox, self.mockedNewCardsSpinbox)
        simulator_dialog.setTabOrder(self.mockedNewCardsSpinbox, self.percentCorrectLearningTextfield)
        simulator_dialog.setTabOrder(self.percentCorrectLearningTextfield, self.percentCorrectLapseTextfield)
        simulator_dialog.setTabOrder(self.percentCorrectLapseTextfield, self.percentCorrectYoungSpinbox)
        simulator_dialog.setTabOrder(self.percentCorrectYoungSpinbox, self.percentCorrectMatureSpinbox)
        simulator_dialog.setTabOrder(self.percentCorrectMatureSpinbox, self.simulationTitleTextfield)
        simulator_dialog.setTabOrder(self.simulationTitleTextfield, self.daysToSimulateSpinbox)
        simulator_dialog.setTabOrder(self.daysToSimulateSpinbox, self.simulateButton)
        simulator_dialog.setTabOrder(self.simulateButton, self.loadDeckConfigurationsButton)
        simulator_dialog.setTabOrder(self.loadDeckConfigurationsButton, self.clearLastSimulationButton)
        simulator_dialog.setTabOrder(self.clearLastSimulationButton, self.clearAllSimulationButton)
        simulator_dialog.setTabOrder(self.clearAllSimulationButton, self.aboutButton)

    def retranslateUi(self, simulator_dialog):
        _translate = QtCore.QCoreApplication.translate
        simulator_dialog.setWindowTitle(_translate("simulator_dialog", "Anki Simulator"))
        self.loadDeckConfigurationsButton.setText(_translate("simulator_dialog", "Load Deck Options and Performance"))
        self.manualButton.setText(_translate("simulator_dialog", "Manual"))
        self.aboutButton.setText(_translate("simulator_dialog", "About"))
        self.supportButton.setText(_translate("simulator_dialog", "❤️ Support This Add-on"))
        self.learningStepsTextfield.setText(_translate("simulator_dialog", "30 2880 8640"))
        self.newLapseIntervalSpinbox.setSuffix(_translate("simulator_dialog", "%"))
        self.label_3.setText(_translate("simulator_dialog", "<b>Deck Options</b>"))
        self.maximumIntervalLabel.setText(_translate("simulator_dialog", "Maximum interval (days)"))
        self.intervalModifierLabel.setText(_translate("simulator_dialog", "Interval modifier"))
        self.startingEaseSpinBox.setSuffix(_translate("simulator_dialog", "%"))
        self.maximumReviewsPerDayLabel.setText(_translate("simulator_dialog", "Maximum reviews per day"))
        self.lapseStepsTextfield.setText(_translate("simulator_dialog", "1440"))
        self.newLapseIntervalLabel.setText(_translate("simulator_dialog", "New lapse interval"))
        self.newCardsPerDayLabel.setText(_translate("simulator_dialog", "New cards per day"))
        self.intervalModifierSpinbox.setSuffix(_translate("simulator_dialog", "%"))
        self.graduatingIntervalLabel.setText(_translate("simulator_dialog", "Graduating interval (days)"))
        self.startingEaseLabel.setText(_translate("simulator_dialog", "Starting ease"))
        self.learningStepsLabel.setText(_translate("simulator_dialog", "Learning steps"))
        self.lapseStepsLabel.setText(_translate("simulator_dialog", "Lapse steps"))
        self.percentCorrectLearningTextfield.setText(_translate("simulator_dialog", "70 90 90"))
        self.percentCorrectLapseTextfield.setText(_translate("simulator_dialog", "90 90"))
        self.percentCorrectYoungLabel.setText(_translate("simulator_dialog", "% correct young cards"))
        self.percentCorrectLearningLabel.setText(_translate("simulator_dialog", "% correct learning steps"))
        self.label_2.setText(_translate("simulator_dialog", "<b>Simulation Options</b>"))
        self.label_4.setText(_translate("simulator_dialog", "Cards"))
        self.includeSuspendedNewCardsCheckbox.setText(_translate("simulator_dialog", "Include suspended new cards"))
        self.includeOverdueCardsCheckbox.setText(_translate("simulator_dialog", "Include overdue cards"))
        self.simulateAdditionalNewCardsCheckbox.setText(_translate("simulator_dialog", "Simulate (additional) new cards:"))
        self.useActualCardsCheckbox.setText(_translate("simulator_dialog", "Use actual cards in deck"))
        self.percentCorrectLapseLabel.setText(_translate("simulator_dialog", "% correct lapse steps"))
        self.percentCorrectYoungSpinbox.setSuffix(_translate("simulator_dialog", "%"))
        self.percentCorrectMatureLabel.setText(_translate("simulator_dialog", "% correct mature cards"))
        self.percentCorrectMatureSpinbox.setSuffix(_translate("simulator_dialog", "%"))
        self.label_5.setText(_translate("simulator_dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Your Performance </span>(Based on your past reviews)</p></body></html>"))
        self.label.setText(_translate("simulator_dialog", "Title"))
        self.simulationTitleTextfield.setText(_translate("simulator_dialog", "Simulation 1"))
        self.daysToSimulateLabel.setText(_translate("simulator_dialog", "Days to simulate"))
        self.simulateButton.setText(_translate("simulator_dialog", "Simulate"))
        self.clearLastSimulationButton.setText(_translate("simulator_dialog", "Clear last simulation"))
        self.clearAllSimulationButton.setText(_translate("simulator_dialog", "Clear all"))
