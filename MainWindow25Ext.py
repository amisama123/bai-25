from PyQt6.QtWidgets import QMessageBox


from bai25.MainWindow25 import Ui_MainWindow



class MainWindow25Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSingalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSingalAndSlot(self):
        self.pushButtonKiemTra.clicked.connect(self.cuaso_moi)
        self.pushButton.clicked.connect(self.thoat_khong)
    def thoat_khong(self):
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle('xác nhận tiep tục')
        dlg.setText('Tiếp không?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        if dlg.exec()==QMessageBox.StandardButton.No:
            #self.MainWindow.close()
            exit()
        else:
            self.lineEditNhapChuoi.setText("")
            self.lineEdit.setText('')
            self.lineEditNhapChuoi.setFocus()
    def cuaso_moi(self):
        def CheckDoiXung(s):
            flag = True
            for i in range(len(s)):
                if s[i] != s[len(s) - i - 1]:
                    flag = False
                    break
            return flag
        a=str(self.lineEditNhapChuoi.text())
        if CheckDoiXung(a)==True:
            ansDoiXung="chuỗi bạn nhập đối xứng"
        else:
            ansDoiXung="chuỗi bạn nhập không đối xứng"
        self.lineEdit.setText(str(ansDoiXung))
