from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QTextEdit
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtCore import Qt, QTimer, QAbstractTableModel
from PyQt5 import uic
import sys
import pandas as pd
import test as pt
import test2 as pt2
from pymongo import MongoClient
from MySQLdb import *
import pyodbc




class interfaz(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaz_Grafica/Finish_Menu.ui", self) #lectura de plantilla de interfaz principal
        width = 764
        height = 568
        self.setFixedSize(width,height)
        self.pushButton_10.setCursor(Qt.PointingHandCursor)
        self.pushButton_10.clicked.connect(self.llamartest)
        self.pushButton_11.setCursor(Qt.PointingHandCursor)
        self.pushButton_11.clicked.connect(self.llamartest2)

        

    def llamartest(self):
        fieldnames = ['Iteracion','Hora']
        fieldnames1 = ['Iteracion','Hora']
        fieldnames2 = ['Iteracion','Hora']
        DB_IP = 'localhost'
        DB_ID = "root"
        DB_PW = "LS9lm10N11"
        MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='paises', charset='utf8mb4', cursorclass=cursors.DictCursor)

        mongoDB_client = MongoClient()
        mongoDB_client = MongoClient('localhost', 27017)
        mongoDB_db = mongoDB_client["dbpaises"]
        mongoDB_collection = mongoDB_db["pais"]

        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=LAPTOP-RO4OO5FH\SQLEXPRESS01;'
            r'DATABASE=paises;'
            r'Trusted_Connection=yes;')
            
        cnxn = pyodbc.connect(conn_str)


        random = []
        pt.GUI(MySQL_db,mongoDB_collection,cnxn)
        

    def llamartest2(self):
        fieldnames = ['Iteracion','Hora']
        fieldnames1 = ['Iteracion','Hora']
        fieldnames2 = ['Iteracion','Hora']
        DB_IP = 'localhost'
        DB_ID = "root"
        DB_PW = "LS9lm10N11"
        MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='paises', charset='utf8mb4', cursorclass=cursors.DictCursor)

        mongoDB_client = MongoClient()
        mongoDB_client = MongoClient('localhost', 27017)
        mongoDB_db = mongoDB_client["dbpaises"]
        mongoDB_collection = mongoDB_db["pais"]
        
        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=LAPTOP-RO4OO5FH\SQLEXPRESS01;'
            r'DATABASE=paises;'
            r'Trusted_Connection=yes;')
            
        cnxn = pyodbc.connect(conn_str)
        
        random = []
        pt2.GUI2(MySQL_db,mongoDB_collection,cnxn)   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = interfaz()
    GUI.show()
    sys.exit(app.exec_())
        

