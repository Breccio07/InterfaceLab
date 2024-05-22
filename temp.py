from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\danielemorelli\Documents\dcoenti\mainwindow.ui", self)
        
        self.tableWidget = QTableWidget()
        
        # find the widgets in the xml file
        
        self.button= self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.clickedBtn)
        
        self.table = self.findChild(QTableWidget, "tabella")
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabel(["Name","Cognome"])
        
        
        self.show()
        
    def clickedBtn(self):
        item_name = QTableWidgetItem("ciao")
        self.table.setItem(1,0 item_name)
        
app = QApplication(sys.argv)
window = UI()
app.exec_()