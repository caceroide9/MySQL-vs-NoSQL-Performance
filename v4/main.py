import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow
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
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

class MainWindow(QMainWindow):

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

        def __init__(self):
                super(MainWindow,self).__init__()
                loadUi("Interfaz_Grafica/Finish_Menu.ui",self)
                width = 764
                height = 568
                self.setFixedSize(width,height)
                self.pushButton_10.setCursor(Qt.PointingHandCursor)
                self.pushButton_10.clicked.connect(self.llamartest)
                self.pushButton_11.setCursor(Qt.PointingHandCursor)
                self.pushButton_11.clicked.connect(self.llamartest2)
                self.pushButton_9.setCursor(Qt.PointingHandCursor)
                self.pushButton_9.clicked.connect(self.gotoScreen2)
                self.pushButton_7.setCursor(Qt.PointingHandCursor)
                self.pushButton_7.clicked.connect(self.gotoScreen3)
                self.pushButton_6.setCursor(Qt.PointingHandCursor)
                self.pushButton_6.clicked.connect(self.gotoScreen4)
                self.pushButton_8.setCursor(Qt.PointingHandCursor)
                self.pushButton_8.clicked.connect(self.gotoScreen5)

        def gotoScreen2(self):
                screen2=Screen2()
                widget.addWidget(screen2)
                widget.setCurrentIndex(widget.currentIndex()+1)

        def gotoScreen3(self):
                screen3=Screen3()
                widget.addWidget(screen3)
                widget.setCurrentIndex(widget.currentIndex()+1)

        def gotoScreen4(self):
                screen4=Screen4()
                widget.addWidget(screen4)
                widget.setCurrentIndex(widget.currentIndex()+1)

        def gotoScreen5(self):
                screen5=Screen5()
                widget.addWidget(screen5)
                widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QMainWindow):
        def __init__(self):
                super(Screen2,self).__init__()
                loadUi("Interfaz_Grafica/Historia.ui",self)
                self.pushButton_9.clicked.connect(self.gotoScreen1)
                width = 764
                height = 568
                self.setFixedSize(width,height)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class Screen3(QMainWindow):
        def __init__(self):
                super(Screen3,self).__init__()
                loadUi("Interfaz_Grafica/Conceptos.ui",self)
                self.pushButton_7.clicked.connect(self.gotoScreen1)
                width = 764
                height = 568
                self.setFixedSize(width,height)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class Screen4(QMainWindow):
        def __init__(self):
                super(Screen4,self).__init__()
                loadUi("Interfaz_Grafica/Diseno.ui",self)
                self.pushButton_6.clicked.connect(self.gotoScreen1)
                width = 764
                height = 568
                self.setFixedSize(width,height)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class Screen5(QMainWindow):
        def __init__(self):
                super(Screen5,self).__init__()
                loadUi("Interfaz_Grafica/Database.ui",self)
                self.pushButton_8.clicked.connect(self.gotoScreen1)
                width = 764
                height = 568
                self.setFixedSize(width,height)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


app= QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
widget.addWidget(mainwindow)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")