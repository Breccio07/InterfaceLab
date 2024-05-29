from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit
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
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels(["Nome","Cognome","Ore"])
        
        self.lNome = self.findChild(QLabel, "lNome")
        self.lCognome = self.findChild(QLabel, "lCognome")
        self.lOre = self.findChild(QLabel, "lOre")
        
        self.line_Nome = self.findChild(QLineEdit, "Line_Nome")
        self.line_Cognome = self.findChild(QLineEdit, "Line_Cognome")
        self.line_Ore = self.findChild(QLineEdit, "Line_Ore")
        
        self.show()
            
        
    def clickedBtn(self):
        
        riga=0
        
        lista=[{'nomeP':"Matteo","cognomeP":"Picciolini","oreP":"18"},{'nomeP':"Claudia","cognomeP":"Ricci","oreP":"18"},{'nomeP':"Marco","cognomeP":"Bonatti","oreP":"18"}]
        
        for element in lista:
            
           item_nomeP = QTableWidgetItem(element["nomeP"])
           item_cognomeP = QTableWidgetItem(element["cognomeP"])
           item_oreP= QTableWidgetItem(element["oreP"])
           
           self.table.setItem(riga, 0, item_nomeP)
           self.table.setItem(riga, 1, item_cognomeP)
           self.table.setItem(riga, 2, item_oreP)
           
           riga = riga+1
        
        
        
app = QApplication(sys.argv)
window = UI()
app.exec_()