# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UpdateUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 195)
        self.OKButton = QtWidgets.QDialogButtonBox(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(520, 20, 81, 241))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.OKButton.setFont(font)
        self.OKButton.setOrientation(QtCore.Qt.Vertical)
        self.OKButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OKButton.setObjectName("OKButton")
        self.WeightLabel = QtWidgets.QLabel(Dialog)
        self.WeightLabel.setGeometry(QtCore.QRect(20, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.WeightLabel.setFont(font)
        self.WeightLabel.setObjectName("WeightLabel")
        self.ChestLabel = QtWidgets.QLabel(Dialog)
        self.ChestLabel.setGeometry(QtCore.QRect(150, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.ChestLabel.setFont(font)
        self.ChestLabel.setObjectName("ChestLabel")
        self.UnderLabel = QtWidgets.QLabel(Dialog)
        self.UnderLabel.setGeometry(QtCore.QRect(270, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.UnderLabel.setFont(font)
        self.UnderLabel.setObjectName("UnderLabel")
        self.BellyLabel = QtWidgets.QLabel(Dialog)
        self.BellyLabel.setGeometry(QtCore.QRect(150, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.BellyLabel.setFont(font)
        self.BellyLabel.setObjectName("BellyLabel")
        self.LThighLabel = QtWidgets.QLabel(Dialog)
        self.LThighLabel.setGeometry(QtCore.QRect(270, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.LThighLabel.setFont(font)
        self.LThighLabel.setObjectName("LThighLabel")
        self.LBicepLabel = QtWidgets.QLabel(Dialog)
        self.LBicepLabel.setGeometry(QtCore.QRect(390, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.LBicepLabel.setFont(font)
        self.LBicepLabel.setObjectName("LBicepLabel")
        self.BloodLabel = QtWidgets.QLabel(Dialog)
        self.BloodLabel.setGeometry(QtCore.QRect(390, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.BloodLabel.setFont(font)
        self.BloodLabel.setObjectName("BloodLabel")
        self.WeightEnter = QtWidgets.QLineEdit(Dialog)
        self.WeightEnter.setGeometry(QtCore.QRect(10, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.WeightEnter.setFont(font)
        self.WeightEnter.setText("")
        self.WeightEnter.setObjectName("WeightEnter")
        self.ChestEnter = QtWidgets.QLineEdit(Dialog)
        self.ChestEnter.setGeometry(QtCore.QRect(140, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.ChestEnter.setFont(font)
        self.ChestEnter.setText("")
        self.ChestEnter.setObjectName("ChestEnter")
        self.UnderEnter = QtWidgets.QLineEdit(Dialog)
        self.UnderEnter.setGeometry(QtCore.QRect(260, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.UnderEnter.setFont(font)
        self.UnderEnter.setText("")
        self.UnderEnter.setObjectName("UnderEnter")
        self.BloodEnter = QtWidgets.QLineEdit(Dialog)
        self.BloodEnter.setGeometry(QtCore.QRect(380, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.BloodEnter.setFont(font)
        self.BloodEnter.setText("")
        self.BloodEnter.setObjectName("BloodEnter")
        self.BellyEnter = QtWidgets.QLineEdit(Dialog)
        self.BellyEnter.setGeometry(QtCore.QRect(140, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.BellyEnter.setFont(font)
        self.BellyEnter.setText("")
        self.BellyEnter.setObjectName("BellyEnter")
        self.LThighEnter = QtWidgets.QLineEdit(Dialog)
        self.LThighEnter.setGeometry(QtCore.QRect(260, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.LThighEnter.setFont(font)
        self.LThighEnter.setText("")
        self.LThighEnter.setObjectName("LThighEnter")
        self.LBicepEnter = QtWidgets.QLineEdit(Dialog)
        self.LBicepEnter.setGeometry(QtCore.QRect(380, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.LBicepEnter.setFont(font)
        self.LBicepEnter.setText("")
        self.LBicepEnter.setObjectName("LBicepEnter")
        self.UpdateButton = QtWidgets.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(500, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.UpdateButton.setFont(font)
        self.UpdateButton.setObjectName("UpdateButton")
        self.DateLabel = QtWidgets.QLabel(Dialog)
        self.DateLabel.setGeometry(QtCore.QRect(220, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.GoalLabel = QtWidgets.QLabel(Dialog)
        self.GoalLabel.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.GoalLabel.setFont(font)
        self.GoalLabel.setObjectName("GoalLabel")
        self.GoalEnter = QtWidgets.QLineEdit(Dialog)
        self.GoalEnter.setGeometry(QtCore.QRect(10, 110, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.GoalEnter.setFont(font)
        self.GoalEnter.setText("")
        self.GoalEnter.setObjectName("GoalEnter")
        self.DateEnter = QtWidgets.QDateEdit(Dialog)
        self.DateEnter.setGeometry(QtCore.QRect(250, 160, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.DateEnter.setFont(font)
        self.DateEnter.setObjectName("DateEnter")

        self.retranslateUi(Dialog)
        self.OKButton.accepted.connect(Dialog.accept) # type: ignore
        self.OKButton.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.WeightLabel.setText(_translate("Dialog", "Weight"))
        self.ChestLabel.setText(_translate("Dialog", "Chest"))
        self.UnderLabel.setText(_translate("Dialog", "Under Chest"))
        self.BellyLabel.setText(_translate("Dialog", "Belly"))
        self.LThighLabel.setText(_translate("Dialog", "Left Thigh"))
        self.LBicepLabel.setText(_translate("Dialog", "Left Bicep"))
        self.BloodLabel.setText(_translate("Dialog", "Blood Sugar"))
        self.UpdateButton.setText(_translate("Dialog", "Update"))
        self.DateLabel.setText(_translate("Dialog", "Date (MM/DD/YYYY)"))
        self.GoalLabel.setText(_translate("Dialog", "Goal Weight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
