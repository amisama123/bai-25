# Form implementation generated from reading ui file 'C:\Users\Admin\mypythoncode\K24406H\bai25\MainWindow25.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 297)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 181, 20))
        self.label.setStyleSheet("color: rgb(0, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditNhapChuoi = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditNhapChuoi.setGeometry(QtCore.QRect(150, 60, 241, 20))
        self.lineEditNhapChuoi.setStyleSheet("background-color: rgb(207, 215, 255);")
        self.lineEditNhapChuoi.setObjectName("lineEditNhapChuoi")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 411, 101))
        self.groupBox_2.setStyleSheet("background-color: rgb(207, 255, 238);\n"
"color: rgb(0, 0, 0);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonKiemTra = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonKiemTra.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.pushButtonKiemTra.setStyleSheet("background-color: rgb(255, 233, 143);")
        self.pushButtonKiemTra.setObjectName("pushButtonKiemTra")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 160, 361, 91))
        self.groupBox.setStyleSheet("background-color: rgb(255, 229, 199);\n"
"color: rgb(255, 0, 4);\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 301, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(244, 255, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(225, 224, 255);")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEditNhapChuoi.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Kiểm tra chuỗi đối xứng</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Nhập vào một chuỗi"))
        self.pushButtonKiemTra.setText(_translate("MainWindow", "Kiểm tra"))
        self.groupBox.setTitle(_translate("MainWindow", "Kết Quả:"))
        self.pushButton.setText(_translate("MainWindow", "oki"))
