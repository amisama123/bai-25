from PyQt6.QtWidgets import QApplication, QMainWindow

from bai25.MainWindow25Ext import MainWindow25Ext

app=QApplication([])
MainWindow=QMainWindow()
myui=MainWindow25Ext()
myui.setupUi(MainWindow)
myui.showWindow()
app.exec()
