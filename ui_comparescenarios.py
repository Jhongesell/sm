# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:/Users/Public/QSWATPlus3/QSWATPlus\ui_comparescenarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_compareScenarios(object):
    def setupUi(self, compareScenarios):
        compareScenarios.setObjectName("compareScenarios")
        compareScenarios.resize(328, 168)
        self.label = QtWidgets.QLabel(compareScenarios)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(compareScenarios)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 121, 16))
        self.label_2.setObjectName("label_2")
        self.scenario1 = QtWidgets.QComboBox(compareScenarios)
        self.scenario1.setGeometry(QtCore.QRect(20, 70, 121, 22))
        self.scenario1.setObjectName("scenario1")
        self.scenario2 = QtWidgets.QComboBox(compareScenarios)
        self.scenario2.setGeometry(QtCore.QRect(180, 70, 121, 22))
        self.scenario2.setObjectName("scenario2")
        self.okButton = QtWidgets.QPushButton(compareScenarios)
        self.okButton.setGeometry(QtCore.QRect(230, 120, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(compareScenarios)
        self.cancelButton.setGeometry(QtCore.QRect(130, 120, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(compareScenarios)
        QtCore.QMetaObject.connectSlotsByName(compareScenarios)

    def retranslateUi(self, compareScenarios):
        _translate = QtCore.QCoreApplication.translate
        compareScenarios.setWindowTitle(_translate("compareScenarios", "Compare Scenarios"))
        self.label.setText(_translate("compareScenarios", "Scenario 1"))
        self.label_2.setText(_translate("compareScenarios", "Scenario 2"))
        self.okButton.setText(_translate("compareScenarios", "OK"))
        self.cancelButton.setText(_translate("compareScenarios", "Cancel"))
