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
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import os
import csv
import string
import time
import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import threading
from pymongo import MongoClient
from MySQLdb import *
import threading
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import psutil
#from win32api import GetSystemMetrics
from PIL import ImageTk, Image


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
                width = 1500
                height = 850  
                self.setFixedSize(width,height)
                self.label_2.setPixmap(QPixmap("Interfaz_Grafica/db.jpg")) 
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
                self.pushButton_12.setCursor(Qt.PointingHandCursor)
                self.pushButton_12.clicked.connect(self.gotoScreen6)

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

        def gotoScreen6(self):
                screen6=Screen6()
                widget.addWidget(screen6)
                widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QMainWindow):
        def __init__(self):
                super(Screen2,self).__init__()
                loadUi("Interfaz_Grafica/Historia1.ui",self)
                self.pushButton_9.clicked.connect(self.gotoScreen1)
                width = 1500  
                height = 850
                self.setFixedSize(width,height)
                self.label.setPixmap(QPixmap("Interfaz_Grafica/Rf2.png")) 
               
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class Screen3(QMainWindow):
        def __init__(self):
                super(Screen3,self).__init__()
                loadUi("Interfaz_Grafica/Conceptos.ui",self)
                self.pushButton_7.clicked.connect(self.gotoScreen1)
                width = 1500  
                height = 850
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
                width = 1500  
                height = 850
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
                width = 1500  
                height = 850
                self.setFixedSize(width,height)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b2=Button(win, text='Subtract')
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)


class Screen6(QMainWindow):
        def __init__(self):
                super(Screen6,self).__init__()
                loadUi("Interfaz_Grafica/h.ui",self)
                self.pushButton_6.clicked.connect(self.gotoScreen1)
                width = 1500  
                height = 850
                self.setFixedSize(width,height)
                self.label_2.setPixmap(QPixmap("Interfaz_Grafica/r6.png"))
                self.pushButton_2.setCursor(Qt.PointingHandCursor) 
                self.pushButton_2.clicked.connect(self.oracle)
                self.pushButton_3.setCursor(Qt.PointingHandCursor) 
                self.pushButton_3.clicked.connect(self.mysql)
                self.pushButton_4.setCursor(Qt.PointingHandCursor) 
                self.pushButton_4.clicked.connect(self.sqlserver)
                self.pushButton_5.setCursor(Qt.PointingHandCursor) 
                self.pushButton_5.clicked.connect(self.postgre)
                self.pushButton_7.setCursor(Qt.PointingHandCursor) 
                self.pushButton_7.clicked.connect(self.mongo)
                self.pushButton_8.setCursor(Qt.PointingHandCursor) 
                self.pushButton_8.clicked.connect(self.redis)
                self.pushButton_9.setCursor(Qt.PointingHandCursor) 
                self.pushButton_9.clicked.connect(self.ibmdb2)
                self.pushButton_10.setCursor(Qt.PointingHandCursor) 
                self.pushButton_10.clicked.connect(self.elastic)
                self.pushButton_11.setCursor(Qt.PointingHandCursor) 
                self.pushButton_11.clicked.connect(self.acess)
                self.pushButton_12.setCursor(Qt.PointingHandCursor) 
                self.pushButton_12.clicked.connect(self.sqlite)
                self.pushButton_13.setCursor(Qt.PointingHandCursor) 
                self.pushButton_13.clicked.connect(self.casandra)
                self.pushButton_14.setCursor(Qt.PointingHandCursor) 
                self.pushButton_14.clicked.connect(self.mariadb)
                self.pushButton_15.setCursor(Qt.PointingHandCursor) 
                self.pushButton_15.clicked.connect(self.spu)
                self.pushButton_16.setCursor(Qt.PointingHandCursor) 
                self.pushButton_16.clicked.connect(self.snow)
                self.pushButton_17.setCursor(Qt.PointingHandCursor) 
                self.pushButton_17.clicked.connect(self.azure)
                self.pushButton_18.setCursor(Qt.PointingHandCursor) 
                self.pushButton_18.clicked.connect(self.dinamo)
                self.pushButton_19.setCursor(Qt.PointingHandCursor) 
                self.pushButton_19.clicked.connect(self.hive)
                self.pushButton_20.setCursor(Qt.PointingHandCursor) 
                self.pushButton_20.clicked.connect(self.teradata)
                self.pushButton_21.setCursor(Qt.PointingHandCursor) 
                self.pushButton_21.clicked.connect(self.neo4j)
                self.pushButton_22.setCursor(Qt.PointingHandCursor) 
                self.pushButton_22.clicked.connect(self.Solr)
                self.pushButton_23.setCursor(Qt.PointingHandCursor) 
                self.pushButton_23.clicked.connect(self.SAPHANA)
                self.pushButton_24.setCursor(Qt.PointingHandCursor) 
                self.pushButton_24.clicked.connect(self.filemarker)
                self.pushButton_25.setCursor(Qt.PointingHandCursor) 
                self.pushButton_25.clicked.connect(self.sapas)
                self.pushButton_26.setCursor(Qt.PointingHandCursor) 
                self.pushButton_26.clicked.connect(self.bq)
                self.pushButton_28.setCursor(Qt.PointingHandCursor) 
                self.pushButton_28.clicked.connect(self.mazurecosmo)
                self.pushButton_29.setCursor(Qt.PointingHandCursor) 
                self.pushButton_29.clicked.connect(self.PostGIS)
                self.pushButton_30.setCursor(Qt.PointingHandCursor) 
                self.pushButton_30.clicked.connect(self.InfluxDB)
                self.pushButton_31.setCursor(Qt.PointingHandCursor) 
                self.pushButton_31.clicked.connect(self.Couchbase)
                self.pushButton_32.setCursor(Qt.PointingHandCursor) 
                self.pushButton_32.clicked.connect(self.Firebird)
                self.pushButton_33.setCursor(Qt.PointingHandCursor) 
                self.pushButton_33.clicked.connect(self.AmazonRedshift)
                self.pushButton_34.setCursor(Qt.PointingHandCursor) 
                self.pushButton_34.clicked.connect(self.Informix)
                self.pushButton_35.setCursor(Qt.PointingHandCursor) 
                self.pushButton_35.clicked.connect(self.Memcached)
                self.pushButton_36.setCursor(Qt.PointingHandCursor) 
                self.pushButton_36.clicked.connect(self.SparkSQL)
                self.pushButton_37.setCursor(Qt.PointingHandCursor) 
                self.pushButton_37.clicked.connect(self.Sinapse)
                self.pushButton_38.setCursor(Qt.PointingHandCursor) 
                self.pushButton_38.clicked.connect(self.Vertica)
                self.pushButton_39.setCursor(Qt.PointingHandCursor) 
                self.pushButton_39.clicked.connect(self.Netezza)
                self.pushButton_40.setCursor(Qt.PointingHandCursor) 
                self.pushButton_40.clicked.connect(self.Fire)
                self.pushButton_41.setCursor(Qt.PointingHandCursor) 
                self.pushButton_41.clicked.connect(self.Impala)
                self.pushButton_42.setCursor(Qt.PointingHandCursor) 
                self.pushButton_42.clicked.connect(self.dBASE)
                self.pushButton_43.setCursor(Qt.PointingHandCursor) 
                self.pushButton_43.clicked.connect(self.Presto)
                self.pushButton_44.setCursor(Qt.PointingHandCursor) 
                self.pushButton_44.clicked.connect(self.Greenplum)
                self.pushButton_45.setCursor(Qt.PointingHandCursor) 
                self.pushButton_45.clicked.connect(self.ClickHouse)
                self.pushButton_46.setCursor(Qt.PointingHandCursor) 
                self.pushButton_46.clicked.connect(self.AmazonAu)
                self.pushButton_47.setCursor(Qt.PointingHandCursor) 
                self.pushButton_47.clicked.connect(self.etcd)
                self.pushButton_48.setCursor(Qt.PointingHandCursor) 
                self.pushButton_48.clicked.connect(self.Hasel)
                self.pushButton_49.setCursor(Qt.PointingHandCursor) 
                self.pushButton_49.clicked.connect(self.h2)
                self.pushButton_50.setCursor(Qt.PointingHandCursor) 
                self.pushButton_50.clicked.connect(self.Market)
                self.pushButton_51.setCursor(Qt.PointingHandCursor) 
                self.pushButton_51.clicked.connect(self.datastax)
                self.pushButton_52.setCursor(Qt.PointingHandCursor) 
                self.pushButton_52.clicked.connect(self.Realm)
     



        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)

        

        def oracle(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ra3.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Oracle')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop() 
        
        def mysql(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/mysql.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha MySQL')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop() 

        def sqlserver(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/sqlserver.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha SQL Server')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))

               root.mainloop() 

        def postgre(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/postgre.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Postgre SQL')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop() 
        
        def mongo(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/mongo1.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha MongoDB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def redis(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/redis.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Redis')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def ibmdb2(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/IBM.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha IBM DB2')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def elastic(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Elastic.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Elasticsearch')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def acess(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Acess.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Microsoft Access')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def sqlite(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/SQLite.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha SQLite')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def casandra(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/casandra.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha cassandra')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def mariadb(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Mariadb.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha MariaDB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def spu(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/spu.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Splunk')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def snow(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/snow.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Snowflake')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def azure(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/azure.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Microsoft Azure SQL Database')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def dinamo(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/dinamo.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Amazon DynamoDB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def hive(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/hive.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Hive')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def teradata(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Teradata.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Teradata')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def neo4j(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/neo4j.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Teradata')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Solr(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Solr.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Solr')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def SAPHANA(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/SAP-HANA.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha SAP-HANA')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def filemarker(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/filemarker.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha FileMarker')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
        
        def sapas(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/SAPAS.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Servidor adaptativo de SAP')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def bq(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Bq.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Google Big Query')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def hbase(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/HBase.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha HBase')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
      
        def mazurecosmo(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Microsoft Azure Cosmos DB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Microsoft Azure Cosmos DB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def PostGIS(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/PostGIS.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha PostGIS')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def InfluxDB(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/InfluxDB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha InfluxDB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Couchbase(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Couchbase.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Couchbase')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
              
        def Firebird(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Firebird.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Firebird')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def AmazonRedshift(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Amazon Redshift.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Amazon Redshift')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Informix(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Informix.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Informix')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Memcached(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Memcached.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Memcached')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def SparkSQL(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Spark SQL.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Spark SQL')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Sinapse(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Synapse.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Microsoft Azure Synapse Analytics')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def Vertica(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Vertica.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Vertica')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Netezza(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Netezza.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Netezza')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Fire(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Fire.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Fire')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Impala(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Impala.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Impala')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def dBASE(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/dBASE.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha dBASE')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Presto(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Presto.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Presto')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Greenplum(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Greenplum.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Greenplum')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def ClickHouse(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ClickHouse.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha ClickHouse')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def AmazonAu(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/AmazonAu.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha AmazonAu')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()


        def etcd(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/etcd.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha etcd')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()


        def Hasel(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Hasel.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Hasel')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()


        def h2(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/H2.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha H2')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def Market(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Market.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Market')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def datastax(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/datastax.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha datastax')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()


        def Realm(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Realm.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Realm')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()


app= QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
widget.addWidget(mainwindow)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")