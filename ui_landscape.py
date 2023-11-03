# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:/Users/Public/QSWATPlus3/QSWATPlus\ui_landscape.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_landscapeDialog(object):
    def setupUi(self, landscapeDialog):
        landscapeDialog.setObjectName("landscapeDialog")
        landscapeDialog.resize(393, 255)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/QSWATPlus/swatplus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        landscapeDialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(landscapeDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hillslopesCheckBox = QtWidgets.QCheckBox(landscapeDialog)
        self.hillslopesCheckBox.setEnabled(True)
        self.hillslopesCheckBox.setAutoFillBackground(False)
        self.hillslopesCheckBox.setChecked(False)
        self.hillslopesCheckBox.setObjectName("hillslopesCheckBox")
        self.gridLayout_2.addWidget(self.hillslopesCheckBox, 0, 0, 1, 2)
        self.floodplainCheckBox = QtWidgets.QCheckBox(landscapeDialog)
        self.floodplainCheckBox.setChecked(True)
        self.floodplainCheckBox.setObjectName("floodplainCheckBox")
        self.gridLayout_2.addWidget(self.floodplainCheckBox, 0, 2, 1, 2)
        self.methodTab = QtWidgets.QTabWidget(landscapeDialog)
        self.methodTab.setEnabled(True)
        self.methodTab.setToolTip("")
        self.methodTab.setObjectName("methodTab")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)
        self.bufferMultiplier = QtWidgets.QSpinBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferMultiplier.sizePolicy().hasHeightForWidth())
        self.bufferMultiplier.setSizePolicy(sizePolicy)
        self.bufferMultiplier.setMinimum(1)
        self.bufferMultiplier.setProperty("value", 10)
        self.bufferMultiplier.setObjectName("bufferMultiplier")
        self.gridLayout_4.addWidget(self.bufferMultiplier, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)
        self.methodTab.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 5)
        self.ridgeThresholdCells = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ridgeThresholdCells.sizePolicy().hasHeightForWidth())
        self.ridgeThresholdCells.setSizePolicy(sizePolicy)
        self.ridgeThresholdCells.setMinimumSize(QtCore.QSize(0, 20))
        self.ridgeThresholdCells.setObjectName("ridgeThresholdCells")
        self.gridLayout_3.addWidget(self.ridgeThresholdCells, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)
        self.ridgeThresholdArea = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ridgeThresholdArea.sizePolicy().hasHeightForWidth())
        self.ridgeThresholdArea.setSizePolicy(sizePolicy)
        self.ridgeThresholdArea.setMinimumSize(QtCore.QSize(0, 20))
        self.ridgeThresholdArea.setObjectName("ridgeThresholdArea")
        self.gridLayout_3.addWidget(self.ridgeThresholdArea, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 3, 1, 1)
        self.areaUnitsBox = QtWidgets.QComboBox(self.tab)
        self.areaUnitsBox.setMinimumSize(QtCore.QSize(0, 20))
        self.areaUnitsBox.setObjectName("areaUnitsBox")
        self.gridLayout_3.addWidget(self.areaUnitsBox, 2, 4, 1, 1)
        self.methodTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.branchThreshold = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.branchThreshold.sizePolicy().hasHeightForWidth())
        self.branchThreshold.setSizePolicy(sizePolicy)
        self.branchThreshold.setObjectName("branchThreshold")
        self.gridLayout.addWidget(self.branchThreshold, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.methodTab.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.methodTab, 1, 0, 1, 4)
        self.slopePositionSpinBox = QtWidgets.QDoubleSpinBox(landscapeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slopePositionSpinBox.sizePolicy().hasHeightForWidth())
        self.slopePositionSpinBox.setSizePolicy(sizePolicy)
        self.slopePositionSpinBox.setMaximum(1.0)
        self.slopePositionSpinBox.setSingleStep(0.01)
        self.slopePositionSpinBox.setProperty("value", 0.1)
        self.slopePositionSpinBox.setObjectName("slopePositionSpinBox")
        self.gridLayout_2.addWidget(self.slopePositionSpinBox, 2, 0, 1, 1)
        self.slopePositionLabel = QtWidgets.QLabel(landscapeDialog)
        self.slopePositionLabel.setObjectName("slopePositionLabel")
        self.gridLayout_2.addWidget(self.slopePositionLabel, 2, 1, 1, 3)
        self.createButton = QtWidgets.QPushButton(landscapeDialog)
        self.createButton.setObjectName("createButton")
        self.gridLayout_2.addWidget(self.createButton, 3, 2, 1, 1)
        self.doneButton = QtWidgets.QPushButton(landscapeDialog)
        self.doneButton.setObjectName("doneButton")
        self.gridLayout_2.addWidget(self.doneButton, 3, 3, 1, 1)

        self.retranslateUi(landscapeDialog)
        self.methodTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(landscapeDialog)

    def retranslateUi(self, landscapeDialog):
        _translate = QtCore.QCoreApplication.translate
        landscapeDialog.setWindowTitle(_translate("landscapeDialog", "Landscape analysis"))
        self.hillslopesCheckBox.setToolTip(_translate("landscapeDialog", "Divide each subbasin into left and right hillslopes plus, for subbasins containing a stream source, the headwater area."))
        self.hillslopesCheckBox.setText(_translate("landscapeDialog", "Calculate hillslopes"))
        self.floodplainCheckBox.setToolTip(_translate("landscapeDialog", "Divide each subbasin into a floodplain and upslope area."))
        self.floodplainCheckBox.setText(_translate("landscapeDialog", "Calculate floodplain"))
        self.label_5.setText(_translate("landscapeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use a channel buffer as the floodplain</p></body></html>"))
        self.bufferMultiplier.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>The width of the buffer each side of the stream is the stream width times the buffer multiplier.</p></body></html>"))
        self.label_6.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>The width of the buffer each side of the stream is the stream width times the buffer multiplier.</p></body></html>"))
        self.label_6.setText(_translate("landscapeDialog", "Buffer multiplier                                                    "))
        self.methodTab.setTabText(self.methodTab.indexOf(self.tab_3), _translate("landscapeDialog", "Buffer channels"))
        self.label.setText(_translate("landscapeDialog", "Use an inverted DEM to calculate ridges"))
        self.label_4.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>The minimum number of cells flowing to a point in an inverted DEM for the point to be considered a ridge cell.  The default is the same number of cells as the stream delineation threshold.</p></body></html>"))
        self.label_4.setText(_translate("landscapeDialog", "Ridge threshold"))
        self.ridgeThresholdCells.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>The minimum number of cells flowing to a point in an inverted DEM for the point to be considered a ridge cell. The default is the same number of cells as the stream delineation threshold.</p></body></html>"))
        self.label_7.setText(_translate("landscapeDialog", "Number of cells"))
        self.ridgeThresholdArea.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>The minimum area flowing to a point in an inverted DEM for the point to be considered a ridge cell. The default is the same area as the stream delineation threshold.</p></body></html>"))
        self.label_8.setText(_translate("landscapeDialog", "Area "))
        self.methodTab.setTabText(self.methodTab.indexOf(self.tab), _translate("landscapeDialog", "DEM inversion"))
        self.label_2.setText(_translate("landscapeDialog", "Use branch lengths to calculate ridges"))
        self.branchThreshold.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>Adjacent points are defined as ridge points if the flow length in metres to where their flow paths join is at least this threshold. The default threshold is 2√A where A is the subbasin threshold in square metres.</p></body></html>"))
        self.label_3.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>Adjacent points are defined as ridge points if the flow length in metres to where their flow paths join is at least this threshold. The default threshold is 2√A where A is the subbasin threshold in square metres.</p></body></html>"))
        self.label_3.setText(_translate("landscapeDialog", "Threshold branch length in metres                 "))
        self.methodTab.setTabText(self.methodTab.indexOf(self.tab_2), _translate("landscapeDialog", "Branch length"))
        self.slopePositionSpinBox.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>Maximum ratio of height of a  point above valley floor to height of ridge above valley floor for a point to be in the floodplain.  Must be between 0 and 1.</p></body></html>"))
        self.slopePositionLabel.setToolTip(_translate("landscapeDialog", "<html><head/><body><p>Maximum ratio of height of a  point above valley floor to height of ridge above valley floor for a point to be in the floodplain.  Must be between 0 and 1.</p></body></html>"))
        self.slopePositionLabel.setText(_translate("landscapeDialog", "Slope position threshold"))
        self.createButton.setText(_translate("landscapeDialog", "Create"))
        self.doneButton.setText(_translate("landscapeDialog", "Done"))
from . import resources_rc
