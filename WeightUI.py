from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import datetime as dt
import csv

matplotlib.use("Qt5Agg")

from UpdateUI import *
from Plotter import *

from WeightClass import *

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

class Storage():
    data = {}


class MyGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        WeightGUI = self
        WeightGUI.setObjectName("WeightGUI")
        WeightGUI.resize(416, 313)
        self.centralwidget = QtWidgets.QWidget(WeightGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.WeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.WeightLabel.setGeometry(QtCore.QRect(50, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.WeightLabel.setFont(font)
        self.WeightLabel.setObjectName("WeightLabel")
        self.ImportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportButton.setGeometry(QtCore.QRect(280, 40, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.ImportButton.setFont(font)
        self.ImportButton.setObjectName("ImportButton")
        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateButton.setGeometry(QtCore.QRect(280, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.UpdateButton.setFont(font)
        self.UpdateButton.setObjectName("UpdateButton")
        self.PlotButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlotButton.setGeometry(QtCore.QRect(280, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.PlotButton.setFont(font)
        self.PlotButton.setObjectName("PlotButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.WeightList = QtWidgets.QListWidget(self.centralwidget)
        self.WeightList.setGeometry(QtCore.QRect(10, 40, 256, 192))
        self.WeightList.setObjectName("listWidget")
        WeightGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WeightGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 22))
        self.menubar.setObjectName("menubar")
        WeightGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WeightGUI)
        self.statusbar.setObjectName("statusbar")
        WeightGUI.setStatusBar(self.statusbar)

        self.retranslateUi(WeightGUI)
        QtCore.QMetaObject.connectSlotsByName(WeightGUI)
        
        self.show()
        self.ButtonManager()
        self.WeightList.itemSelectionChanged.connect(self.ButtonManager)
        
        
        self.ImportButton.clicked.connect(self.AddItem)
        self.UpdateButton.clicked.connect(self.UpdateMenu)
        self.PlotButton.clicked.connect(self.PlotWin)
        self.SaveButton.clicked.connect(self.Save)

    def retranslateUi(self, WeightGUI):
        _translate = QtCore.QCoreApplication.translate
        WeightGUI.setWindowTitle(_translate("WeightGUI", "MainWindow"))
        self.WeightLabel.setText(_translate("WeightGUI", "Weight List"))
        self.ImportButton.setText(_translate("WeightGUI", "Import Data"))
        self.UpdateButton.setText(_translate("WeightGUI", "Update Data"))
        self.PlotButton.setText(_translate("WeightGUI", "Plot"))
        self.SaveButton.setText(_translate("WeightGUI", "Save"))
        
    def ImportData(self, spec=["AFM Image File", "All Files (*)", ""]):
        fname, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self, spec[0], spec[2], spec[1])
        
        if fname:
            print(fname)
            return fname
        
    def AddItem(self):
        items = self.ImportData()
        if items:
            for item in items:
                self.WeightList.addItem(item)
            for i in range(self.WeightList.count()):
                self.WeightList.item(i).setText(self.WeightList.item(i).text().rsplit('/', 1)[-1][:-4])
                Storage.data.update({f"{self.WeightList.item(i).text()}": 
                    WeightTracker(self.WeightList.item(i).text()+".csv")})
                
                
    def UpdateWin(self):
        self.UpdateWindow = QtWidgets.QDialog()
        self.UpdateUI = Ui_Dialog()
        self.UpdateUI.setupUi(self.UpdateWindow)
        self.UpdateWindow.show()
        
    def PlotterWin(self):
        self.PlotWindow = QtWidgets.QDialog()
        self.PlotUI = Ui_Plot()
        self.PlotUI.setupUi(self.PlotWindow)
        self.PlotWindow.show()
        
    def PlotWin(self):
        self.PlotterWin()
        self.checks = [self.PlotUI.BellyLabel, self.PlotUI.ChestLabel, self.PlotUI.LBicepLabel, self.PlotUI.LThighLabel, self.PlotUI.SugarLabel, self.PlotUI.UnderLabel, self.PlotUI.WeightLabel]
        
        self.PlotUI.PlotButton.clicked.connect(self.PlotShow)
        
        
        
        
    def PlotShow(self):
                
        self.plots = [check.text() for check in self.checks if check.isChecked()]
                
        n = self.WeightList.currentItem().text()
            
        self.dates = [dt.datetime.strptime(date, "%m/%d/%Y") for date in Storage.data[f"{n}"].dates]
            
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
        # Storage.data[f"{n}"].data["Dates"]
        
        for key in self.plots:
            plt.plot(self.dates, Storage.data[f"{n}"].data[f"{key}"], label=f"{key}")
        if "Weight" in self.plots:
            plt.plot(self.dates, Storage.data[f"{n}"].data["Goal Weight"], label="Goal Weight")
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()
        
    def UpdateMenu(self):
        self.UpdateWin()
        self.UpdateUI.UpdateButton.clicked.connect(self.UpdateData)
        
    def UpdateData(self):
        n = self.WeightList.currentItem().text()
        
        date = [str(self.UpdateUI.DateEnter.date().toPyDate().strftime("%m/%d/%Y").rstrip(","))]
        Storage.data[f"{n}"].data["Weight"] += [float(self.UpdateUI.WeightEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Dates"] += date
        Storage.data[f"{n}"].data["Chest"] += [float(self.UpdateUI.ChestEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Belly"] += [float(self.UpdateUI.BellyEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Under"] += [float(self.UpdateUI.UnderEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Left Thigh"] += [float(self.UpdateUI.LThighEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Left Bicep"] += [float(self.UpdateUI.LBicepEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Blood Sugar"] += [float(self.UpdateUI.BloodEnter.text().rstrip(","))]
        Storage.data[f"{n}"].data["Goal Weight"] += [float(self.UpdateUI.GoalEnter.text().rstrip(","))]
        self.UpdateWindow.close()
        
    def ButtonManager(self):
        samp = self.WeightList.currentItem()
        
        if samp:
            self.UpdateButton.setEnabled(True)
            self.SaveButton.setEnabled(True)
            self.PlotButton.setEnabled(True)
            
        else:
            self.UpdateButton.setEnabled(False)
            self.SaveButton.setEnabled(False)
            self.PlotButton.setEnabled(False)
            
    def Save(self):
        n = self.WeightList.currentItem().text()
        fields = Storage.data[f"{n}"].labels
        path = os.path.abspath(f"{n}")
        data = Storage.data[f"{n}"].data
        
        with open(path+".csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(zip(*data.values()))
        print("Saved!")
        
def main():
    app = QtWidgets.QApplication([])
    window = MyGUI()
    app.exit(app.exec_())

if __name__ == "__main__":
    main()