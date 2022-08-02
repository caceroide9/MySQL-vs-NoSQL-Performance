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
import test3 as pt3
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
matplotlib.use('Agg')
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
import psycopg2
from PyQt5.QtWidgets import QPushButton
from style import *
from conexionDb import*
from conexionDb_pokemon import*
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from pandas import read_csv
import numpy as np

import matplotlib.pyplot as plt

class FxFinder():

    def __init__(self):

        self.root = tk.Tk()
    
        self.root.title("Calculadora T(n)")
        
        self.root.config(bg = 'white')
        
        self.index = 0
        self.aux_array = []
        
        self.x = []
        self.y = []
        self.y_log = []
        
        self.array = os.listdir("Data/")
        
        self.Bar_1 = tk.Frame(self.root, bg = 'white')       # Frame de botones superiores
        self.Bar_1.pack(side = 'top', fill = 'x')
        
        self.Bar_2 = tk.Frame(self.root, bg = 'white')       # Frame de botones izquierda
        self.Bar_2.pack(side = 'top')
        
        self.Bar_3 = tk.Frame(self.root, bg = 'white')       # Frame para botones inferiores
        self.Bar_3.pack(side = 'top', fill = 'x')
        
        self.categories = ['Pokemon', 'Netflix', 'Chile']
        self.sub_categories = [['Test_1', 'Test_2', 'Test_3'], 
                               ['Test_1', 'Test_2','Test_3'], 
                               ['Test_1', 'Test_2', 'Test_3']]
        self.data_bases = ['MongoDB', 'MySQL', 'SQLServer', 'PostgreSQL','CouchBase']
        
        #######################################################################################################
        
        self.Lbl_1 = ttk.Label(self.Bar_1, text = 'Categoria: ', background = 'white')
        self.Lbl_1.pack(side = 'left')
        
        #######################################################################################################
        
        self.Cb_1 = ttk.Combobox(self.Bar_1, state = 'readonly', values = self.categories)
        self.Cb_1.bind('<<ComboboxSelected>>', lambda event: self.Change_Sub_Category(self.Cb_1.get()))
        self.Cb_1.pack(side = 'left', padx = 10, pady = 10)
        
        self.Cb_1.set(self.categories[0])
        
        #######################################################################################################
        
        self.Lbl_2 = ttk.Label(self.Bar_1, text = 'Sub Categoria: ', background = 'white')
        self.Lbl_2.pack(side = 'left')
        
        #######################################################################################################
        
        self.Cb_2 = ttk.Combobox(self.Bar_1, state = 'readonly', values = self.sub_categories[0])
        self.Cb_2.pack(side = 'left', padx = 10, pady = 10)
        
        self.Cb_2.set(self.sub_categories[0][0])
        
        #######################################################################################################
        
        self.Lbl_2 = ttk.Label(self.Bar_1, text = 'Gestor a seleccionar: ', background = 'white')
        self.Lbl_2.pack(side = 'left')
        
        #######################################################################################################
        
        self.Cb_3 = ttk.Combobox(self.Bar_1, state = 'readonly', values = self.data_bases)
        self.Cb_3.pack(side = 'left', padx = 10, pady = 10)
        self.Cb_3.set(self.data_bases[0])
        
        #######################################################################################################
        
        self.Execute_button = ttk.Button(self.Bar_2, text = 'Ejecutar', command=lambda:self.Load_Data())
        self.Execute_button.pack(side = 'top', pady = 20)
        
        #######################################################################################################
        
        self.Log_box = scrolledtext.ScrolledText(self.Bar_3, wrap = "word", height = 30, width = 80, bd=5)
        self.Log_box.pack(side = 'top')
        
        #print(self.array)

        self.root.mainloop()
        
        # Cou
        # Mongo
        # MySQL
        # Postgre
        # SQLServer
        
    def Change_Sub_Category(self, opt):
        
        self.index = self.categories.index(self.Cb_1.get())
        
        self.Cb_2['values'] = self.sub_categories[self.index]
        self.Cb_2.set(self.sub_categories[self.index][0])
        
        #print(opt)
        
        
        
    def Load_Data(self):
       
       
       self.fields = []
       self.fields.append(self.Cb_1.get())
       self.fields.append(self.Cb_2.get())
       
       if self.Cb_3.get() == 'MongoDB':
              
              self.fields.append('Mongo')
              
       elif self.Cb_3.get() == 'CouchBase':
              
              self.fields.append('Cou')
              
       elif self.Cb_3.get() == 'PostgreSQL':
              
              self.fields.append('Postgres')
              
       else:
       
              self.fields.append(self.Cb_3.get())
       
       
       #self.data_bases = ['CouchBase', 'MongoDB', 'MySQL', 'SQLServer', 'PostgreSQL']
       
       if self.fields[0] == 'Pokemon':
              for name in self.array:
                     if not 'Parte' in name and self.fields[1] in name and self.fields[2] in name:
                            self.df = read_csv('Data/' + name, delimiter = ',')
                            self.data = self.df.values
                            break
              
       elif self.fields[0] == 'Netflix':
              for name in self.array:
                     if 'Parte_2' in name and self.fields[1] in name and self.fields[2] in name:
                            self.df = read_csv('Data/' + name, delimiter = ',')
                            self.data = self.df.values
                            break
       
       elif self.fields[0] == 'Chile':
              for name in self.array:
                     if 'Parte_3' in name and self.fields[1] in name and self.fields[2] in name:
                            self.df = read_csv('Data/' + name, delimiter = ',')
                            self.data = self.df.values
                            break
              
       else:
              self.Log_box.insert(tk.END, ' Archivo no Encontrado...\n')
              return
       
       #print(self.data[0][0])
       
       self.aux = []
       self.Log_box.delete('1.0', tk.END)
       self.Log_box.update_idletasks()
       for i in range(len(self.data)):
              
              self.aux.append('.....')
              self.aux.append(int(self.data[i][0]))
              self.x.append(int(self.data[i][0]))
              self.aux.append('.......')
              self.aux.append(self.data[i][1])
              self.y.append(self.data[i][1])
              self.aux.append('........')
              
              #self.aux.append(int(self.data[i][0]))
              self.aux.append(np.log(self.data[i][1]))
              self.y_log.append(np.log(self.data[i][1]))
              
              self.aux_array.append(self.aux)
              
              self.aux = []
              
       #print(self.aux_array)
              
       #for i in range(len(self.aux_array)):
              
              #print(self.aux_array[i][2], self.aux_array[i][3])
              
       self.Log_box.insert(tk.END, ' Iteracion   |   Tiempo   |          Ln(Tiempo)  \n')
       
              
       for i in self.aux_array:
              
              self.Log_box.insert(tk.END, i)
              self.Log_box.insert(tk.END, '\n')
       self.aux_array = []
              
       ################## AJUSTE DEL MODELO ################
       
       self.fit = np.polyfit(self.y_log, self.x, 1)
       self.Log_box.insert(tk.END, self.fit)
       #print(self.fit)
       
       ##########################################################
              
       #plt.scatter(self.y_log, self.x)
       #plt.show()
              
              
       self.x = []
       self.y = []
       self.y_log = []
        




class MainWindow(QMainWindow):	

        def llamartest(self):
                fieldnames = ['Iteracion','Hora']
                fieldnames1 = ['Iteracion','Hora']
                fieldnames2 = ['Iteracion','Hora']
                DB_IP = 'localhost'
                DB_ID = "USER"
                DB_PW = "PASSWORD"
                
                MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
                
                mongoDB_client = MongoClient()
                mongoDB_client = MongoClient('localhost', 27017)
                mongoDB_db = mongoDB_client["DATABASENAME"]
                mongoDB_collection = mongoDB_db["COLLECTION"]

                conn_str = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
                cnxn = pyodbc.connect(conn_str)

                conn = psycopg2.connect(dbname="DBNAME", user="USER",
                            password="PASSWORD", host="localhost", port="5432")
                random = []
                pt.GUI(MySQL_db,mongoDB_collection,cnxn,conn)
                

        def llamartest2(self):
                fieldnames = ['Iteracion','Hora']
                fieldnames1 = ['Iteracion','Hora']
                fieldnames2 = ['Iteracion','Hora']
                DB_IP = 'localhost'
                DB_ID = "USER"
                DB_PW = "PASSWORD"
                MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)

                mongoDB_client = MongoClient()
                mongoDB_client = MongoClient('localhost', 27017)
                mongoDB_db = mongoDB_client["DBNAME"]
                mongoDB_collection = mongoDB_db["COLLECTION"]
                mongoDB_collection_2 = mongoDB_db["COLLECTION"]
                
                conn_str = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBANME;'
                        r'Trusted_Connection=yes;')
                        
                cnxn = pyodbc.connect(conn_str)
                
                conn = psycopg2.connect(dbname="DBNAME", user="USER",
                            password="PASSWORD", host="localhost", port="5432")
                random = []
                pt2.GUI2(MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2)

        def llamartest3(self):
                fieldnames = ['Iteracion','Hora']
                fieldnames1 = ['Iteracion','Hora']
                fieldnames2 = ['Iteracion','Hora']
                DB_IP = 'localhost'
                DB_ID = "USER"
                DB_PW = "PASSWORD"
                MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)

                mongoDB_client = MongoClient()
                mongoDB_client = MongoClient('localhost', 27017)
                mongoDB_db = mongoDB_client["DBANME"]
                mongoDB_collection = mongoDB_db["COLLECTION"]
                mongoDB_collection_2 = mongoDB_db["COLLECTION"]
                mongoDB_collection_3 = mongoDB_db["COLLECTION"]
                
                conn_str = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
                cnxn = pyodbc.connect(conn_str)
                
                conn = psycopg2.connect(dbname="DBNAME", user="USER",
                            password="PASSWORD", host="localhost", port="5432")
                random = []
                pt3.GUI3(MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3)
       
        def llamartest4(self):
              A = FxFinder()
              


        def __init__(self):
                super(MainWindow,self).__init__()
                loadUi("Interfaz_Grafica/Finish_Menu.ui",self)
                width = 1500
                height = 830  
                self.setFixedWidth(width)
                self.setFixedWidth(height)
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
                self.pushButton_30.setCursor(Qt.PointingHandCursor)
                self.pushButton_30.clicked.connect(self.llamartest3)
                self.pushButton.setCursor(Qt.PointingHandCursor)
                self.pushButton.clicked.connect(self.gotoScreen7)
                self.pushButton_2.setCursor(Qt.PointingHandCursor)
                self.pushButton_2.clicked.connect(self.llamartest4)



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
       
        def gotoScreen7(self):
                screen7=Screen7()
                widget.addWidget(screen7)
                widget.setCurrentIndex(widget.currentIndex()+1)



class Screen2(QMainWindow):
        def pa1f1(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/TPF.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Tarjetas Perforadas')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()

        def pa1f2(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/alian.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Alianza IBM y American Airlines')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f3(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/cull.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Culliname IDMS')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f4(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/acid.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('ACID')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f5(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/UNI.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('UNIVAC I')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f6(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/BDTer.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Termino Bases de datos')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()  

        def pa1f7(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ibmr.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('IBM System R')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop() 
        
        def pa1f8(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/AUG.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Auge SQL')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop() 
        
        def pa1f9(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/MagN.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Cintas Magnéticas')
               root.geometry('1220x940')
               root.resizable (0,0)
               root.mainloop() 
        
        def pa1f10(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/diaBa.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Diagrama de estructura de datos Bachman')
               root.geometry('1230x910')
               root.resizable (0,0)
               root.mainloop() 
       
        def pa1f11(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/3capas.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Arquitectura ANSI-SPARC')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()


        def pa1f12(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ORa.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Oracle')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f13(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/DBMOP.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Data Organization and Maintenance Processor')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()  

        def pa1f14(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/DBred.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Modelo en Red')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()

        def pa1f15(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/E-R.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Modelo Entidad - Relación')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f16(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/atu.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Edgar "Ted" Codd gana premio Alan Turing')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f17(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/DiscM.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Disco Magnetico')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f18(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ibmims.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('IBM IMS')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f19(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/sdl.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Software Development Laboratories')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()  

        def pa1f20(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/BD2.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('IBM DB2')
               root.geometry('1220x850')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f21(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/IDS.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Integrated Data Store')
               root.geometry('1220x910')
               root.resizable (0,0)
               root.mainloop()

        def pa1f22(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/arelational.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Un modelo relacional')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()  

        def pa1f23(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/dist.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Bases de datos distribuidas')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa1f24(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/tER.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Teradata DBC/1012')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop() 

        def pa2f1(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Gemsto.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('GemStone/S')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()
        
        def pa2f2(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ESS.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Essbase')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()
       
        def pa2f3(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/STREA.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('StreamBase')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f4(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/REISD.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Redis')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f5(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/sqlSE.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('SQL Server')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f6(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/wwwDB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('World Wide Web')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f7(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/4j.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('NEO4J')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f8(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/xmlS.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Sistema XML')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f9(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/PostGR.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Postgre SQL')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f10(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/KDBB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('kdb+')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f11(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/LINQ.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('LINQ')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f12(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/HHHBASE.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Apache HBASE')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f13(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/koGni.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Kognitio')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f14(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/W3Crdf.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('W3C RDF')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f15(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/HIVEDB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Hive')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f16(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/bgw.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Big Query')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f17(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Orien.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Base de datos orientada a objetos')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f18(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/DahlWIN.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ole-Johan Dahl recibe premio Turing')
               root.geometry('1240x850')
               root.resizable (0,0)
               root.mainloop()

        def pa2f19(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/MAISQL.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('MySQL')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f20(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/apc.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Apache Spark')
               root.geometry('1240x880')
               root.resizable (0,0)
               root.mainloop()

        def pa2f21(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/BerDB.png") 
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Berkeley DB') 
               root.geometry('1240x910') 
               root.resizable (0,0)
               root.mainloop()

        def pa2f22(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Marklogic_DB.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Marklogic')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f23(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/MOON.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('MongoDB')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()

        def pa2f24(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/SPa.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Cloud Spanner')
               root.geometry('1240x910')
               root.resizable (0,0)
               root.mainloop()
        
        def __init__(self):
               super(Screen2,self).__init__()
               loadUi("Interfaz_Grafica/y.ui",self)
               self.pushButton_6.clicked.connect(self.gotoScreen1)
               self.pushButton_7.clicked.connect(self.gotoScreen2)
               self.pushButton_8.clicked.connect(self.gotoScreen3)
               width = 1500
               height = 830 
               self.setFixedSize(width,height)
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/parte1.png"))
               self.pushButton_2.setEnabled(False)
               self.pushButton_4.setEnabled(False)
               self.pushButton_9.setEnabled(False)
               self.pushButton_11.setEnabled(False)
               self.pushButton_13.setEnabled(False)
               self.pushButton_15.setEnabled(False)
               self.pushButton_17.setEnabled(False)
               self.pushButton_19.setEnabled(False)
               self.pushButton_21.setEnabled(False)
               self.pushButton_23.setEnabled(False)
               self.pushButton_25.setEnabled(False)
               self.pushButton_27.setEnabled(False)
               self.pushButton_29.setEnabled(False)
               self.pushButton_31.setEnabled(False)
               self.pushButton_33.setEnabled(False)
               self.pushButton_35.setEnabled(False)
               self.pushButton_37.setEnabled(False)
               self.pushButton_39.setEnabled(False)
               self.pushButton_41.setEnabled(False)
               self.pushButton_43.setEnabled(False)
               self.pushButton_45.setEnabled(False)
               self.pushButton_47.setEnabled(False)
               self.pushButton_49.setEnabled(False)
               self.pushButton_51.setEnabled(False)
               self.pushButton.clicked.connect(self.pa1f1)
               self.pushButton_3.clicked.connect(self.pa1f2)
               self.pushButton_5.clicked.connect(self.pa1f3)
               self.pushButton_10.clicked.connect(self.pa1f4)
               self.pushButton_12.clicked.connect(self.pa1f5)
               self.pushButton_14.clicked.connect(self.pa1f6)
               self.pushButton_16.clicked.connect(self.pa1f7)
               self.pushButton_18.clicked.connect(self.pa1f8)
               self.pushButton_20.clicked.connect(self.pa1f9)
               self.pushButton_22.clicked.connect(self.pa1f10)
               self.pushButton_24.clicked.connect(self.pa1f11)
               self.pushButton_26.clicked.connect(self.pa1f12)
               self.pushButton_28.clicked.connect(self.pa1f13)
               self.pushButton_30.clicked.connect(self.pa1f14)
               self.pushButton_32.clicked.connect(self.pa1f15)
               self.pushButton_34.clicked.connect(self.pa1f16)
               self.pushButton_36.clicked.connect(self.pa1f17)
               self.pushButton_38.clicked.connect(self.pa1f18)
               self.pushButton_40.clicked.connect(self.pa1f19)
               self.pushButton_42.clicked.connect(self.pa1f20)
               self.pushButton_44.clicked.connect(self.pa1f21)
               self.pushButton_46.clicked.connect(self.pa1f22)
               self.pushButton_48.clicked.connect(self.pa1f23)
               self.pushButton_50.clicked.connect(self.pa1f24)
               self.pushButton_2.clicked.connect(self.pa2f1)
               self.pushButton_4.clicked.connect(self.pa2f2)
               self.pushButton_9.clicked.connect(self.pa2f3)
               self.pushButton_11.clicked.connect(self.pa2f4)
               self.pushButton_13.clicked.connect(self.pa2f5)
               self.pushButton_15.clicked.connect(self.pa2f6)
               self.pushButton_17.clicked.connect(self.pa2f7)
               self.pushButton_19.clicked.connect(self.pa2f8)
               self.pushButton_21.clicked.connect(self.pa2f9)
               self.pushButton_23.clicked.connect(self.pa2f10)
               self.pushButton_25.clicked.connect(self.pa2f11)
               self.pushButton_27.clicked.connect(self.pa2f12)
               self.pushButton_29.clicked.connect(self.pa2f13)
               self.pushButton_31.clicked.connect(self.pa2f14)
               self.pushButton_33.clicked.connect(self.pa2f15)
               self.pushButton_35.clicked.connect(self.pa2f16)
               self.pushButton_37.clicked.connect(self.pa2f17)
               self.pushButton_39.clicked.connect(self.pa2f18)
               self.pushButton_41.clicked.connect(self.pa2f19)
               self.pushButton_43.clicked.connect(self.pa2f20)
               self.pushButton_45.clicked.connect(self.pa2f21)
               self.pushButton_47.clicked.connect(self.pa2f22)
               self.pushButton_49.clicked.connect(self.pa2f23)
               self.pushButton_51.clicked.connect(self.pa2f24)
               self.pushButton.setCursor(Qt.PointingHandCursor)
               self.pushButton_3.setCursor(Qt.PointingHandCursor)
               self.pushButton_5.setCursor(Qt.PointingHandCursor)
               self.pushButton_10.setCursor(Qt.PointingHandCursor)
               self.pushButton_12.setCursor(Qt.PointingHandCursor)
               self.pushButton_14.setCursor(Qt.PointingHandCursor)
               self.pushButton_16.setCursor(Qt.PointingHandCursor)
               self.pushButton_18.setCursor(Qt.PointingHandCursor)
               self.pushButton_20.setCursor(Qt.PointingHandCursor)
               self.pushButton_22.setCursor(Qt.PointingHandCursor)
               self.pushButton_24.setCursor(Qt.PointingHandCursor)
               self.pushButton_26.setCursor(Qt.PointingHandCursor)
               self.pushButton_28.setCursor(Qt.PointingHandCursor)
               self.pushButton_30.setCursor(Qt.PointingHandCursor)
               self.pushButton_32.setCursor(Qt.PointingHandCursor)
               self.pushButton_34.setCursor(Qt.PointingHandCursor)
               self.pushButton_36.setCursor(Qt.PointingHandCursor)
               self.pushButton_38.setCursor(Qt.PointingHandCursor)
               self.pushButton_40.setCursor(Qt.PointingHandCursor)
               self.pushButton_42.setCursor(Qt.PointingHandCursor)
               self.pushButton_44.setCursor(Qt.PointingHandCursor)
               self.pushButton_46.setCursor(Qt.PointingHandCursor)
               self.pushButton_48.setCursor(Qt.PointingHandCursor)
               self.pushButton_50.setCursor(Qt.PointingHandCursor)
               self.close()
               
               
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)
       
        def gotoScreen2(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/parte1.png"))
               self.pushButton.setEnabled(True)
               self.pushButton_3.setEnabled(True)
               self.pushButton_5.setEnabled(True)
               self.pushButton_10.setEnabled(True)
               self.pushButton_12.setEnabled(True)
               self.pushButton_14.setEnabled(True)
               self.pushButton_16.setEnabled(True)
               self.pushButton_18.setEnabled(True)
               self.pushButton_20.setEnabled(True)
               self.pushButton_22.setEnabled(True)
               self.pushButton_24.setEnabled(True)
               self.pushButton_26.setEnabled(True)
               self.pushButton_28.setEnabled(True)
               self.pushButton_30.setEnabled(True)
               self.pushButton_32.setEnabled(True)
               self.pushButton_34.setEnabled(True)
               self.pushButton_36.setEnabled(True)
               self.pushButton_38.setEnabled(True)
               self.pushButton_40.setEnabled(True)
               self.pushButton_42.setEnabled(True)
               self.pushButton_44.setEnabled(True)
               self.pushButton_46.setEnabled(True)
               self.pushButton_48.setEnabled(True)
               self.pushButton_50.setEnabled(True)
               self.pushButton.setCursor(Qt.PointingHandCursor)
               self.pushButton_3.setCursor(Qt.PointingHandCursor)
               self.pushButton_5.setCursor(Qt.PointingHandCursor)
               self.pushButton_10.setCursor(Qt.PointingHandCursor)
               self.pushButton_12.setCursor(Qt.PointingHandCursor)
               self.pushButton_14.setCursor(Qt.PointingHandCursor)
               self.pushButton_16.setCursor(Qt.PointingHandCursor)
               self.pushButton_18.setCursor(Qt.PointingHandCursor)
               self.pushButton_20.setCursor(Qt.PointingHandCursor)
               self.pushButton_22.setCursor(Qt.PointingHandCursor)
               self.pushButton_24.setCursor(Qt.PointingHandCursor)
               self.pushButton_26.setCursor(Qt.PointingHandCursor)
               self.pushButton_28.setCursor(Qt.PointingHandCursor)
               self.pushButton_30.setCursor(Qt.PointingHandCursor)
               self.pushButton_32.setCursor(Qt.PointingHandCursor)
               self.pushButton_34.setCursor(Qt.PointingHandCursor)
               self.pushButton_36.setCursor(Qt.PointingHandCursor)
               self.pushButton_38.setCursor(Qt.PointingHandCursor)
               self.pushButton_40.setCursor(Qt.PointingHandCursor)
               self.pushButton_42.setCursor(Qt.PointingHandCursor)
               self.pushButton_44.setCursor(Qt.PointingHandCursor)
               self.pushButton_46.setCursor(Qt.PointingHandCursor)
               self.pushButton_48.setCursor(Qt.PointingHandCursor)
               self.pushButton_50.setCursor(Qt.PointingHandCursor)
               self.pushButton_2.setEnabled(False)
               self.pushButton_4.setEnabled(False)
               self.pushButton_9.setEnabled(False)
               self.pushButton_11.setEnabled(False)
               self.pushButton_13.setEnabled(False)
               self.pushButton_15.setEnabled(False)
               self.pushButton_17.setEnabled(False)
               self.pushButton_19.setEnabled(False)
               self.pushButton_21.setEnabled(False)
               self.pushButton_23.setEnabled(False)
               self.pushButton_25.setEnabled(False)
               self.pushButton_27.setEnabled(False)
               self.pushButton_29.setEnabled(False)
               self.pushButton_31.setEnabled(False)
               self.pushButton_33.setEnabled(False)
               self.pushButton_35.setEnabled(False)
               self.pushButton_37.setEnabled(False)
               self.pushButton_39.setEnabled(False)
               self.pushButton_41.setEnabled(False)
               self.pushButton_43.setEnabled(False)
               self.pushButton_45.setEnabled(False)
               self.pushButton_47.setEnabled(False)
               self.pushButton_49.setEnabled(False)
               self.pushButton_51.setEnabled(False)
        
               
                       
        def gotoScreen3(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/part2_v2.png"))
               self.pushButton.setEnabled(False)
               self.pushButton_3.setEnabled(False)
               self.pushButton_5.setEnabled(False)
               self.pushButton_10.setEnabled(False)
               self.pushButton_12.setEnabled(False)
               self.pushButton_14.setEnabled(False)
               self.pushButton_16.setEnabled(False)
               self.pushButton_18.setEnabled(False)
               self.pushButton_20.setEnabled(False)
               self.pushButton_22.setEnabled(False)
               self.pushButton_24.setEnabled(False)
               self.pushButton_26.setEnabled(False)
               self.pushButton_28.setEnabled(False)
               self.pushButton_30.setEnabled(False)
               self.pushButton_32.setEnabled(False)
               self.pushButton_34.setEnabled(False)
               self.pushButton_36.setEnabled(False)
               self.pushButton_38.setEnabled(False)
               self.pushButton_40.setEnabled(False)
               self.pushButton_42.setEnabled(False)
               self.pushButton_44.setEnabled(False)
               self.pushButton_46.setEnabled(False)
               self.pushButton_48.setEnabled(False)
               self.pushButton_50.setEnabled(False)
               self.pushButton_2.setEnabled(True)
               self.pushButton_4.setEnabled(True)
               self.pushButton_9.setEnabled(True)
               self.pushButton_11.setEnabled(True)
               self.pushButton_13.setEnabled(True)
               self.pushButton_15.setEnabled(True)
               self.pushButton_17.setEnabled(True)
               self.pushButton_19.setEnabled(True)
               self.pushButton_21.setEnabled(True)
               self.pushButton_23.setEnabled(True)
               self.pushButton_25.setEnabled(True)
               self.pushButton_27.setEnabled(True)
               self.pushButton_29.setEnabled(True)
               self.pushButton_31.setEnabled(True)
               self.pushButton_33.setEnabled(True)
               self.pushButton_35.setEnabled(True)
               self.pushButton_37.setEnabled(True)
               self.pushButton_39.setEnabled(True)
               self.pushButton_41.setEnabled(True)
               self.pushButton_43.setEnabled(True)
               self.pushButton_45.setEnabled(True)
               self.pushButton_47.setEnabled(True)
               self.pushButton_49.setEnabled(True)
               self.pushButton_51.setEnabled(True)
               self.pushButton_2.setCursor(Qt.PointingHandCursor)
               self.pushButton_4.setCursor(Qt.PointingHandCursor)
               self.pushButton_9.setCursor(Qt.PointingHandCursor)
               self.pushButton_11.setCursor(Qt.PointingHandCursor)
               self.pushButton_13.setCursor(Qt.PointingHandCursor)
               self.pushButton_15.setCursor(Qt.PointingHandCursor)
               self.pushButton_17.setCursor(Qt.PointingHandCursor)
               self.pushButton_19.setCursor(Qt.PointingHandCursor)
               self.pushButton_21.setCursor(Qt.PointingHandCursor)
               self.pushButton_23.setCursor(Qt.PointingHandCursor)
               self.pushButton_25.setCursor(Qt.PointingHandCursor)
               self.pushButton_27.setCursor(Qt.PointingHandCursor)
               self.pushButton_29.setCursor(Qt.PointingHandCursor)
               self.pushButton_31.setCursor(Qt.PointingHandCursor)
               self.pushButton_33.setCursor(Qt.PointingHandCursor)
               self.pushButton_35.setCursor(Qt.PointingHandCursor)
               self.pushButton_37.setCursor(Qt.PointingHandCursor)
               self.pushButton_39.setCursor(Qt.PointingHandCursor)
               self.pushButton_41.setCursor(Qt.PointingHandCursor)
               self.pushButton_43.setCursor(Qt.PointingHandCursor)
               self.pushButton_45.setCursor(Qt.PointingHandCursor)
               self.pushButton_47.setCursor(Qt.PointingHandCursor)
               self.pushButton_49.setCursor(Qt.PointingHandCursor)
               self.pushButton_51.setCursor(Qt.PointingHandCursor)
               
               
               
               
               
              
               
       

               
                
               
              
               
              
            
               
        

        


class Screen3(QMainWindow):
        def concepts_PKK(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/PkEy.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Llave Primaria')
               root.resizable (0,0)
               root.mainloop()
                    
        def concepts_AlmaDDato(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/AlmcAe.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Almacenamiento de datos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_TrigG(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/TriGEr.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Triggers')
               root.resizable (0,0)
               root.mainloop()

        def concepts_ParTIC(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/PArti.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Particion')
               root.resizable (0,0)
               root.mainloop()

        def concepts_SGBDDAD(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/SGGbd.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Sistema de Gestion de Bases de datos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_BDDAnali(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/AnaLI.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos Analiticas')
               root.resizable (0,0)
               root.mainloop()

        def concepts_BddTrans(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/TranSAc.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos Transaccionales')
               root.resizable (0,0)
               root.mainloop()

        def concepts_HasHH(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/HASHHhh.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Hash')
               root.resizable (0,0)
               root.mainloop()

        def concepts_AtribuTO(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/ATRibut.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Atributos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_MaRedu(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/MAPred.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Mapa Reducido')
               root.resizable (0,0)
               root.mainloop()

        def concepts_DocumnTS(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DOcumT.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos de documentos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_disenIO(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DisenIO.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Diseño de Bases de datos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_BDDRelac(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/BDRELAcio.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos Relacionales')
               root.resizable (0,0)
               root.mainloop()

        def concepts_DataCENT(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DaCen.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto DataCenter')
               root.resizable (0,0)
               root.mainloop()

        def concepts_NormaLIzacion(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/NORMZ.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Normalizacion')
               root.resizable (0,0)
               root.mainloop()

           
        def concepts_NoRela(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/BDNRElac.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos No Relacionales')
               root.resizable (0,0)
               root.mainloop()

        def concepts_DbGra(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DBGRAfos.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Bases de datos tipo Grafos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_Visual(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/VSUAL.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Visualización')
               root.resizable (0,0)
               root.mainloop()

        def concepts_MeKano(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/MEKAno.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Mecanografia')
               root.resizable (0,0)
               root.mainloop()

        def concepts_ClaveVA(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/CLav-VA.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Clave Valor')
               root.resizable (0,0)
               root.mainloop()

        def concepts_RoleSS(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/RolBDD.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Roles')
               root.resizable (0,0)
               root.mainloop()

        def concepts_ColumNAR(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/ColUMNar.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Base de Datos Columnar')
               root.resizable (0,0)
               root.mainloop()

        def concepts_Durabili(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DuraBiliDAd.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Durabilidad')
               root.resizable (0,0)
               root.mainloop()

        def concepts_EsquemaD(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/EDDatos.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Esquema de Datos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_Replic(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/ReplicaCi.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Replicacion')
               root.resizable (0,0)
               root.mainloop()



        def concepts_BigDa(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/BiGDa.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto BigData')
               root.resizable (0,0)
               root.mainloop()

        def concepts_DataB(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DBASES.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Base de Datos')
               root.resizable (0,0)
               root.mainloop()

        def concepts_OSour(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/OSou.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Open Source')
               root.resizable (0,0)
               root.mainloop()

        def concepts_infOR(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/inforMES.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Informes')
               root.resizable (0,0)
               root.mainloop()

        def concepts_REL(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/RELAC.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Relacion')
               root.resizable (0,0)
               root.mainloop()
        
        def concepts_Escaa(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/EscaaLA.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Escalabilidad')
               root.resizable (0,0)
               root.mainloop()

        def concepts_ACID(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/aciDS.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto ACID')
               root.resizable (0,0)
               root.mainloop()

        def concepts_CONSIS(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/consT.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Consistencia')
               root.resizable (0,0)
               root.mainloop()

        def concepts_DSET(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/SETTTT.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Dataset')
               root.resizable (0,0)
               root.mainloop()


        def concepts_UF(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/ufp.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Usuario Final')
               root.resizable (0,0)
               root.mainloop()

        def concepts_dATOSS(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/datosx.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Datos')
               root.resizable (0,0)
               root.mainloop()


       
        def concepts_DMLL(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/dmlll.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto DML')
               root.resizable (0,0)
               root.mainloop()


        def concepts_TeoCAP(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/capT.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Teorema CAP')
               root.resizable (0,0)
               root.mainloop()

        def concepts_cloud(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/cloudd.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Cloud')
               root.resizable (0,0)
               root.mainloop()

        
        def concepts_sqlll(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/SQLLLa.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto SQL')
               root.resizable (0,0)
               root.mainloop()


        def concepts_noosqll(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/noosqll.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto NOSQL')
               root.resizable (0,0)
               root.mainloop()

        def concepts_ddll(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/ddll.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto DDL')
               root.resizable (0,0)
               root.mainloop()


        def concepts_BUP(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/BCK.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Backup')
               root.resizable (0,0)
               root.mainloop()


        def concepts_dba(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/DBAA.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto DBA')
               root.resizable (0,0)
               root.mainloop()

        def concepts_CRUD(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/CRUD_Cp.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto CRUD')
               root.resizable (0,0)
               root.mainloop()


        def concepts_fk(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/concep_fk.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Llave Foranea')
               root.resizable (0,0)
               root.mainloop()

        def concepts_query(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/qconsulta.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Query')
               root.resizable (0,0)
               root.mainloop()

        def concepts_datalake(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/dlake.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Data Lake')
               root.resizable (0,0)
               root.mainloop()

        def concepts_entidad(self):
               root=Tk()
               image = Image.open('Interfaz_Grafica/entidash.png')
               image = image.resize((450, 750), Image.ANTIALIAS)
               my_img = ImageTk.PhotoImage(image)
               my_lbl = Label(image = my_img)
               my_lbl.pack()
               root.title('Concepto Entidad')
               root.resizable (0,0)
               root.mainloop()

        

               

        def __init__(self):
                super(Screen3,self).__init__()
                loadUi("Interfaz_Grafica/Conceptos.ui",self)
                self.pushButton_7.clicked.connect(self.gotoScreen1)
                self.pushButton_52.clicked.connect(self.gotoCasos)
                self.pushButton_51.clicked.connect(self.gotoConce)
                self.pushButton_53.clicked.connect(self.gotoVDRela)
                self.pushButton_54.clicked.connect(self.gotoVDNoRela)
                self.pushButton_55.clicked.connect(self.gotoNoSQLSheet1)
                self.pushButton_56.clicked.connect(self.gotoNoSQLSheet2)
                self.pushButton_57.clicked.connect(self.gotoSQLSheet)

                self.label_2.setPixmap(QPixmap("Interfaz_Grafica/concepts_images.png")) 
                width = 1500
                height = 830 
                self.setFixedSize(width,height)
                
                self.pushButton_20.setCursor(Qt.PointingHandCursor)
                self.pushButton_19.setCursor(Qt.PointingHandCursor)
                self.pushButton_18.setCursor(Qt.PointingHandCursor)
                self.pushButton_17.setCursor(Qt.PointingHandCursor)
                self.pushButton_16.setCursor(Qt.PointingHandCursor)
                self.pushButton_15.setCursor(Qt.PointingHandCursor)
                self.pushButton_14.setCursor(Qt.PointingHandCursor)
                self.pushButton_12.setCursor(Qt.PointingHandCursor)
                self.pushButton_13.setCursor(Qt.PointingHandCursor)
                self.pushButton_11.setCursor(Qt.PointingHandCursor)
                self.pushButton_10.setCursor(Qt.PointingHandCursor)
                self.pushButton_8.setCursor(Qt.PointingHandCursor)
                self.pushButton_9.setCursor(Qt.PointingHandCursor)
                self.pushButton_6.setCursor(Qt.PointingHandCursor)
                self.pushButton_5.setCursor(Qt.PointingHandCursor)
                self.pushButton_4.setCursor(Qt.PointingHandCursor)
                self.pushButton_3.setCursor(Qt.PointingHandCursor)
                self.pushButton_2.setCursor(Qt.PointingHandCursor)
                self.pushButton_21.setCursor(Qt.PointingHandCursor)
                self.pushButton.setCursor(Qt.PointingHandCursor)
                self.pushButton_49.setCursor(Qt.PointingHandCursor)
                self.pushButton_22.setCursor(Qt.PointingHandCursor)
                self.pushButton_50.setCursor(Qt.PointingHandCursor)
                self.pushButton_48.setCursor(Qt.PointingHandCursor)
                self.pushButton_47.setCursor(Qt.PointingHandCursor)
                self.pushButton_44.setCursor(Qt.PointingHandCursor)
                self.pushButton_46.setCursor(Qt.PointingHandCursor)
                self.pushButton_45.setCursor(Qt.PointingHandCursor)
                self.pushButton_38.setCursor(Qt.PointingHandCursor)
                self.pushButton_42.setCursor(Qt.PointingHandCursor)
                self.pushButton_43.setCursor(Qt.PointingHandCursor)
                self.pushButton_39.setCursor(Qt.PointingHandCursor)
                self.pushButton_36.setCursor(Qt.PointingHandCursor)
                self.pushButton_37.setCursor(Qt.PointingHandCursor)
                self.pushButton_41.setCursor(Qt.PointingHandCursor)
                self.pushButton_40.setCursor(Qt.PointingHandCursor)
                self.pushButton_34.setCursor(Qt.PointingHandCursor)
                self.pushButton_35.setCursor(Qt.PointingHandCursor)
                self.pushButton_33.setCursor(Qt.PointingHandCursor)
                self.pushButton_31.setCursor(Qt.PointingHandCursor)
                self.pushButton_32.setCursor(Qt.PointingHandCursor)
                self.pushButton_30.setCursor(Qt.PointingHandCursor)
                self.pushButton_29.setCursor(Qt.PointingHandCursor)
                self.pushButton_28.setCursor(Qt.PointingHandCursor)
                self.pushButton_27.setCursor(Qt.PointingHandCursor)
                self.pushButton_25.setCursor(Qt.PointingHandCursor)
                self.pushButton_26.setCursor(Qt.PointingHandCursor)
                self.pushButton_23.setCursor(Qt.PointingHandCursor)
                self.pushButton_24.setCursor(Qt.PointingHandCursor)
                
                self.pushButton_20.clicked.connect(self.concepts_datalake)
                self.pushButton_19.clicked.connect(self.concepts_entidad)
                self.pushButton_18.clicked.connect(self.concepts_query)
                self.pushButton_17.clicked.connect(self.concepts_fk)
                self.pushButton_16.clicked.connect(self.concepts_CRUD) 
                self.pushButton_15.clicked.connect(self.concepts_dba) 
                self.pushButton_14.clicked.connect(self.concepts_BUP)
                self.pushButton_12.clicked.connect(self.concepts_ddll)
                self.pushButton_13.clicked.connect(self.concepts_noosqll)
                self.pushButton_11.clicked.connect(self.concepts_sqlll)
                self.pushButton_10.clicked.connect(self.concepts_cloud)
                self.pushButton_8.clicked.connect(self.concepts_TeoCAP)
                self.pushButton_9.clicked.connect(self.concepts_DMLL)
                self.pushButton_6.clicked.connect(self.concepts_dATOSS)
                self.pushButton_5.clicked.connect(self.concepts_UF)
                self.pushButton_4.clicked.connect(self.concepts_DSET)
                self.pushButton_3.clicked.connect(self.concepts_ACID)
                self.pushButton_2.clicked.connect(self.concepts_CONSIS)
                self.pushButton_21.clicked.connect(self.concepts_infOR)
                self.pushButton.clicked.connect(self.concepts_REL)
                self.pushButton_49.clicked.connect(self.concepts_Escaa)
                self.pushButton_22.clicked.connect(self.concepts_BigDa) 
                self.pushButton_50.clicked.connect(self.concepts_DataB) 
                self.pushButton_48.clicked.connect(self.concepts_OSour)
                self.pushButton_47.clicked.connect(self.concepts_Durabili)
                self.pushButton_44.clicked.connect(self.concepts_EsquemaD)
                self.pushButton_46.clicked.connect(self.concepts_Replic)

                self.pushButton_45.clicked.connect(self.concepts_NoRela)
                self.pushButton_38.clicked.connect(self.concepts_DbGra)
                self.pushButton_42.clicked.connect(self.concepts_Visual)
                self.pushButton_43.clicked.connect(self.concepts_MeKano)
                self.pushButton_39.clicked.connect(self.concepts_ClaveVA)
                self.pushButton_36.clicked.connect(self.concepts_RoleSS)
                self.pushButton_37.clicked.connect(self.concepts_ColumNAR)

                self.pushButton_41.clicked.connect(self.concepts_PKK)
                self.pushButton_40.clicked.connect(self.concepts_AlmaDDato)
                self.pushButton_34.clicked.connect(self.concepts_TrigG)
                self.pushButton_35.clicked.connect(self.concepts_ParTIC)
                self.pushButton_33.clicked.connect(self.concepts_SGBDDAD)
                self.pushButton_31.clicked.connect(self.concepts_BDDAnali)
                self.pushButton_32.clicked.connect(self.concepts_BddTrans)
                self.pushButton_30.clicked.connect(self.concepts_HasHH)
                self.pushButton_29.clicked.connect(self.concepts_AtribuTO)
                self.pushButton_28.clicked.connect(self.concepts_MaRedu)
                self.pushButton_27.clicked.connect(self.concepts_DocumnTS)
                self.pushButton_25.clicked.connect(self.concepts_disenIO)
                self.pushButton_26.clicked.connect(self.concepts_BDDRelac)
                self.pushButton_23.clicked.connect(self.concepts_DataCENT)
                self.pushButton_24.clicked.connect(self.concepts_NormaLIzacion)

        def gotoNoSQLSheet1(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/sqlsheetmongo1.png"))

        def gotoNoSQLSheet2(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/sqlsheetmongo2.png"))

        def gotoSQLSheet(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/sqlsheet.png"))
       
        def gotoVDRela(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/Rel.png"))
              self.pushButton.setEnabled(False)
              self.pushButton_2.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_4.setEnabled(False)
              self.pushButton_5.setEnabled(False)
              self.pushButton_6.setEnabled(False)
              self.pushButton_9.setEnabled(False)
              self.pushButton_8.setEnabled(False)
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_48.setEnabled(False)
              self.pushButton_47.setEnabled(False)
              self.pushButton_44.setEnabled(False)
              self.pushButton_46.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_38.setEnabled(False)
              self.pushButton_43.setEnabled(False)
              self.pushButton_42.setEnabled(False)
              self.pushButton_39.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_41.setEnabled(False)
              self.pushButton_40.setEnabled(False)
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_33.setEnabled(False)
              self.pushButton_31.setEnabled(False)
              self.pushButton_32.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_29.setEnabled(False)
              self.pushButton_28.setEnabled(False)
              self.pushButton_27.setEnabled(False)
              self.pushButton_26.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
        
        def gotoVDNoRela(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/NoRe.png"))
              self.pushButton.setEnabled(False)
              self.pushButton_2.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_4.setEnabled(False)
              self.pushButton_5.setEnabled(False)
              self.pushButton_6.setEnabled(False)
              self.pushButton_9.setEnabled(False)
              self.pushButton_8.setEnabled(False)
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_48.setEnabled(False)
              self.pushButton_47.setEnabled(False)
              self.pushButton_44.setEnabled(False)
              self.pushButton_46.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_38.setEnabled(False)
              self.pushButton_43.setEnabled(False)
              self.pushButton_42.setEnabled(False)
              self.pushButton_39.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_41.setEnabled(False)
              self.pushButton_40.setEnabled(False)
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_33.setEnabled(False)
              self.pushButton_31.setEnabled(False)
              self.pushButton_32.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_29.setEnabled(False)
              self.pushButton_28.setEnabled(False)
              self.pushButton_27.setEnabled(False)
              self.pushButton_26.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)

        def gotoCasos(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/CaUs.png"))
              self.pushButton.setEnabled(False)
              self.pushButton_2.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_4.setEnabled(False)
              self.pushButton_5.setEnabled(False)
              self.pushButton_6.setEnabled(False)
              self.pushButton_9.setEnabled(False)
              self.pushButton_8.setEnabled(False)
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_48.setEnabled(False)
              self.pushButton_47.setEnabled(False)
              self.pushButton_44.setEnabled(False)
              self.pushButton_46.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_38.setEnabled(False)
              self.pushButton_43.setEnabled(False)
              self.pushButton_42.setEnabled(False)
              self.pushButton_39.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_41.setEnabled(False)
              self.pushButton_40.setEnabled(False)
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_33.setEnabled(False)
              self.pushButton_31.setEnabled(False)
              self.pushButton_32.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_29.setEnabled(False)
              self.pushButton_28.setEnabled(False)
              self.pushButton_27.setEnabled(False)
              self.pushButton_26.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
        
        def gotoConce(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/concepts_images.png"))
              self.pushButton.setEnabled(True)
              self.pushButton_2.setEnabled(True)
              self.pushButton_49.setEnabled(True)
              self.pushButton_22.setEnabled(True)
              self.pushButton_3.setEnabled(True)
              self.pushButton_21.setEnabled(True)
              self.pushButton_4.setEnabled(True)
              self.pushButton_5.setEnabled(True)
              self.pushButton_6.setEnabled(True)
              self.pushButton_9.setEnabled(True)
              self.pushButton_8.setEnabled(True)
              self.pushButton_10.setEnabled(True)
              self.pushButton_11.setEnabled(True)
              self.pushButton_13.setEnabled(True)
              self.pushButton_12.setEnabled(True)
              self.pushButton_15.setEnabled(True)
              self.pushButton_14.setEnabled(True)
              self.pushButton_17.setEnabled(True)
              self.pushButton_16.setEnabled(True)
              self.pushButton_18.setEnabled(True)
              self.pushButton_20.setEnabled(True)
              self.pushButton_19.setEnabled(True)
              self.pushButton_50.setEnabled(True)
              self.pushButton_48.setEnabled(True)
              self.pushButton_47.setEnabled(True)
              self.pushButton_44.setEnabled(True)
              self.pushButton_46.setEnabled(True)
              self.pushButton_45.setEnabled(True)
              self.pushButton_38.setEnabled(True)
              self.pushButton_43.setEnabled(True)
              self.pushButton_42.setEnabled(True)
              self.pushButton_39.setEnabled(True)
              self.pushButton_37.setEnabled(True)
              self.pushButton_36.setEnabled(True)
              self.pushButton_41.setEnabled(True)
              self.pushButton_40.setEnabled(True)
              self.pushButton_34.setEnabled(True)
              self.pushButton_35.setEnabled(True)
              self.pushButton_33.setEnabled(True)
              self.pushButton_31.setEnabled(True)
              self.pushButton_32.setEnabled(True)
              self.pushButton_30.setEnabled(True)
              self.pushButton_29.setEnabled(True)
              self.pushButton_28.setEnabled(True)
              self.pushButton_27.setEnabled(True)
              self.pushButton_26.setEnabled(True)
              self.pushButton_25.setEnabled(True)
              self.pushButton_23.setEnabled(True)
              self.pushButton_24.setEnabled(True)
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)



class Screen4(QMainWindow):
       def m_productos(self):
                       datos = self.datosTotal.buscar_productos()
                       i = len(datos)
                       self.tabla_productos.setRowCount(i)
                       tablerow = 0
                       for row in datos:
                              self.tabla_productos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
                              self.tabla_productos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
                              self.tabla_productos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
                              self.tabla_productos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
                              self.tabla_productos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
                              tablerow +=1

       def insert_productos(self):
              codigo = self.codigoA.text() 
              nombre = self.nombreA.text()
              modelo = self.modeloA.text()
              precio = self.precioA.text()
              cantidad = self.cantidadA.text()
              self.datosTotal.inserta_producto(codigo, nombre, modelo, precio, cantidad)
              self.codigoA.clear()
              self.nombreA.clear()
              self.modeloA.clear()
              self.precioA.clear()
              self.cantidadA.clear()

       def modificar_productos(self):
              id_producto = self.id_producto.text() 
              id_producto = str("'" + id_producto + "'")
              nombreXX = self.datosTotal.busca_producto(id_producto)

              if nombreXX != None:
                     self.id_buscar.setText("ACTUALIZAR")
                     codigoM = self.codigo_actualizar.text() 
                     nombreM = self.nombre_actualizar.text()
                     modeloM = self.modelo_actualizar.text()
                     precioM = self.precio_actualizar.text()
                     cantidadM = self.cantidad_actualizar.text()

                     act = self.datosTotal.actualiza_productos(codigoM,nombreM , modeloM, precioM, cantidadM)
                     if act == 1:
                            self.id_buscar.setText("ACTUALIZADO")				
                            self.codigo_actualizar.clear()
                            self.nombre_actualizar.clear()
                            self.modelo_actualizar.clear()
                            self.precio_actualizar.clear()
                            self.cantidad_actualizar.clear()
                            self.id_producto.clear()

                     elif act == 0:
                            self.id_buscar.setText("ERROR")
                     else:
                            self.id_buscar.setText("INCORRECTO")		
                            

       def buscar_producto(self):
              nombre_producto = self.codigoB.text()
              nombre_producto = str("'" + nombre_producto + "'")

              datosB = self.datosTotal.busca_producto(nombre_producto)
              i = len(datosB)

              self.tabla_buscar.setRowCount(i)
              tablerow = 0
              for row in datosB:
                     self.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
                     self.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
                     self.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
                     self.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
                     self.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
                     tablerow +=1

       def eliminar_producto(self):
              eliminar = self.codigo_borrar.text()
              eliminar = str("'"+ eliminar + "'")
              resp = (self.datosTotal.elimina_productos(eliminar))
              datos = self.datosTotal.buscar_productos()
              i = len(datos)
              self.tabla_borrar.setRowCount(i)
              tablerow = 0
              for row in datos:
                     self.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
                     self.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
                     self.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
                     self.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
                     self.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
                     tablerow +=1

                     if resp == None:
                            self.borrar_ok.setText("NO EXISTE")
                     elif resp == 0:
                            self.borrar_ok.setText("NO EXISTE")

                     else:
                            self.borrar_ok.setText("SE ELIMINO")

       
       #####

       def m_productosPo(self):
                       datos = self.datosTotal.buscar_productosPO()
                       i = len(datos)
                       self.tabla_productosPo.setRowCount(i)
                       tablerow = 0
                       for row in datos:
                              self.tabla_productosPo.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                              self.tabla_productosPo.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
                              self.tabla_productosPo.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
                              self.tabla_productosPo.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
                              self.tabla_productosPo.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
                              self.tabla_productosPo.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
                              self.tabla_productosPo.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[6])))
                              self.tabla_productosPo.setItem(tablerow,6,QtWidgets.QTableWidgetItem(str(row[7])))
                              self.tabla_productosPo.setItem(tablerow,7,QtWidgets.QTableWidgetItem(str(row[8])))
                              self.tabla_productosPo.setItem(tablerow,8,QtWidgets.QTableWidgetItem(str(row[9])))
                              self.tabla_productosPo.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[10])))
                              self.tabla_productosPo.setItem(tablerow,10,QtWidgets.QTableWidgetItem(str(row[11])))
                              self.tabla_productosPo.setItem(tablerow,11,QtWidgets.QTableWidgetItem(str(row[12])))
                              self.tabla_productosPo.setItem(tablerow,12,QtWidgets.QTableWidgetItem(str(row[13])))
                              tablerow +=1

       def insert_productosPo(self):
              pk_id= self.a1.text() 
              artist=self.a2.text() 
              song=self.a3.text() 
              duration_ms=self.a4.text() 
              explicit=self.a5.text() 
              year=self.a6.text() 
              popularity=self.a7.text() 
              danceability=self.a8.text() 
              energy=self.a9.text() 
              key=self.a10.text() 
              mode=self.a11.text() 
              acousticness=self.a12.text() 
              instrumentalness=self.a13.text() 
              liveness=self.a14.text() 
              valence=self.a15.text() 
              tempo=self.a16.text() 
              genre=self.a17.text()  
              self.datosTotal.inserta_productoPO(pk_id, artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, mode, acousticness, instrumentalness, liveness, valence, tempo, genre)
              self.a1.clear()
              self.a2.clear()
              self.a3.clear()
              self.a4.clear()
              self.a5.clear()
              self.a6.clear()
              self.a7.clear()
              self.a8.clear()
              self.a9.clear()
              self.a10.clear()
              self.a11.clear()
              self.a12.clear()
              self.a13.clear()
              self.a14.clear()
              self.a15.clear()
              self.a16.clear()
              self.a17.clear()

       def modificar_productosPo(self):
              id_producto = self.id_producto.text() 
              id_producto = str("'" + id_producto + "'")
              nombreXX = self.datosTotal.busca_productoPo(id_producto)

              if nombreXX != None:
                     self.id_buscar.setText("ACTUALIZAR")
                     codigoM = self.codigo_actualizar.text() 
                     nombreM = self.nombre_actualizar.text()
                     modeloM = self.modelo_actualizar.text()
                     precioM = self.precio_actualizar.text()
                     cantidadM = self.cantidad_actualizar.text()

                     act = self.datosTotal.actualiza_productosPO(codigoM,nombreM , modeloM, precioM, cantidadM)
                     if act == 1:
                            self.id_buscar.setText("ACTUALIZADO")				
                            self.codigo_actualizar.clear()
                            self.nombre_actualizar.clear()
                            self.modelo_actualizar.clear()
                            self.precio_actualizar.clear()
                            self.cantidad_actualizar.clear()
                            self.id_producto.clear()

                     elif act == 0:
                            self.id_buscar.setText("ERROR")
                     else:
                            self.id_buscar.setText("INCORRECTO")		
                            

       def buscar_productoPO(self):
              nombre_producto = self.codigoB_2.text()
              nombre_producto = str("'" + nombre_producto + "'")

              codigoB_2 = self.datosTotal.busca_productoPO(nombre_producto)
              i = len(codigoB_2)

              self.tabla_buscarPo.setRowCount(i)
              tablerow = 0
              for row in codigoB_2:
                     self.tabla_buscarPo.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                     self.tabla_buscarPo.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[1])))
                     self.tabla_buscarPo.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[2])))
                     self.tabla_buscarPo.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
                     self.tabla_buscarPo.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
                     self.tabla_buscarPo.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[5])))
                     self.tabla_buscarPo.setItem(tablerow,6,QtWidgets.QTableWidgetItem(str(row[6])))
                     self.tabla_buscarPo.setItem(tablerow,7,QtWidgets.QTableWidgetItem(str(row[7])))
                     self.tabla_buscarPo.setItem(tablerow,8,QtWidgets.QTableWidgetItem(str(row[8])))
                     self.tabla_buscarPo.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[9])))
                     self.tabla_buscarPo.setItem(tablerow,10,QtWidgets.QTableWidgetItem(str(row[10])))
                     self.tabla_buscarPo.setItem(tablerow,11,QtWidgets.QTableWidgetItem(str(row[11])))
                     self.tabla_buscarPo.setItem(tablerow,12,QtWidgets.QTableWidgetItem(str(row[12])))
                     self.tabla_buscarPo.setItem(tablerow,13,QtWidgets.QTableWidgetItem(str(row[13])))
                     tablerow +=1

       def eliminar_productoPo(self):
              eliminar = self.codigo_borrarPO.text()
              eliminar = str("'"+ eliminar + "'")
              resp = (self.datosTotal.elimina_productosPO(eliminar))
              datos = self.datosTotal.buscar_productosPO()
              i = len(datos)
              self.tabla_borrarPO.setRowCount(i)
              tablerow = 0
              for row in datos:
                     self.tabla_borrarPO.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
                     self.tabla_borrarPO.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row[2])))
                     self.tabla_borrarPO.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(row[3])))
                     self.tabla_borrarPO.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[4])))
                     self.tabla_borrarPO.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[5])))
                     tablerow +=1

                     if resp == None:
                            self.borrar_okPO.setText("NO EXISTE")
                     elif resp == 0:
                            self.borrar_okPO.setText("NO EXISTE")

                     else:
                            self.borrar_okPO.setText("SE ELIMINO")
       	
       
       def __init__(self):
                super(Screen4,self).__init__()
                loadUi("Interfaz_Grafica/Diseno.ui",self)
                width = 1500
                height = 830 
                self.setFixedSize(width,height)
                self.datosTotal = Registro_datos()
                self.label.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
                self.label_15.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
                self.label_16.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
                self.label_17.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
                self.label_18.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
                self.bt_refrescar.clicked.connect(self.m_productos)
                self.bt_agregar.clicked.connect(self.insert_productos)
                self.bt_buscar.clicked.connect(self.buscar_producto)
                self.bt_borrar.clicked.connect(self.eliminar_producto)
                self.bt_actualizar.clicked.connect(self.modificar_productos)
                self.tabla_productos.setColumnWidth(0,98)
                self.tabla_productos.setColumnWidth(1,100)
                self.tabla_productos.setColumnWidth(2,98)
                self.tabla_productos.setColumnWidth(3,98)
                self.tabla_productos.setColumnWidth(4,98)
                self.tabla_borrar.setColumnWidth(0,98)
                self.tabla_borrar.setColumnWidth(1,100)
                self.tabla_borrar.setColumnWidth(2,98)
                self.tabla_borrar.setColumnWidth(3,98)
                self.tabla_borrar.setColumnWidth(4,98)
                self.tabla_buscar.setColumnWidth(0,98)
                self.tabla_buscar.setColumnWidth(1,100)
                self.tabla_buscar.setColumnWidth(2,98)
                self.tabla_buscar.setColumnWidth(3,98)
                self.tabla_buscar.setColumnWidth(4,98)
                self.tabla_productos.move(300, 100)
                self.bt_refrescar.move(575, 600)
                self.tabla_productosPo.setVisible(False)
                self.bt_refrescarPo.setVisible(False)
                self.codigoB_2.setVisible(False)
                self.tabla_buscarPo.setVisible(False)
                self.bt_buscarPo.setVisible(False)
                self.codigoB.setVisible(True)
                self.bt_borrarPO.setVisible(False)
                self.tabla_borrarPO.setVisible(False)
                self.codigo_borrarPO.setVisible(False)
                self.borrar_okPO.setVisible(False)
                self.label_21.setVisible(False)
                self.label_20.setVisible(False)
                self.label_22.setVisible(False)
                self.label_23.setVisible(False)
                self.label_25.setVisible(False)
                self.label_26.setVisible(False)
                self.label_27.setVisible(False)
                self.label_28.setVisible(False)
                self.label_29.setVisible(False)
                self.label_30.setVisible(False)
                self.label_31.setVisible(False)
                self.label_32.setVisible(False)
                self.label_24.setVisible(False)
                self.label_33.setVisible(False)
                self.label_34.setVisible(False)
                self.label_35.setVisible(False)
                self.label_36.setVisible(False)
                self.a1.setVisible(False)
                self.a2.setVisible(False)
                self.a3.setVisible(False)
                self.a4.setVisible(False)
                self.a5.setVisible(False)
                self.a6.setVisible(False)
                self.a7.setVisible(False)
                self.a8.setVisible(False)
                self.a9.setVisible(False)
                self.a10.setVisible(False)
                self.a11.setVisible(False)
                self.a12.setVisible(False)
                self.a13.setVisible(False)
                self.a14.setVisible(False)
                self.a15.setVisible(False)
                self.a16.setVisible(False)
                self.a17.setVisible(False)
                self.pushButton_6.clicked.connect(self.gotoScreen1)
                self.pushButton_7.clicked.connect(self.gotoCRUD_Prcts)
                self.pushButton_8.clicked.connect(self.gotoCRUD_POK)
                self.codigoB.move(600, 50)
                self.label_2.move(450, 50)
                self.tabla_buscar.move(300, 100)
                self.bt_buscar.move(575, 600)
                self.label_3.move(250,50)
                self.label_4.move(250,150)
                self.label_5.move(250,250)
                self.label_6.move(250,350)
                self.label_7.move(250,450)
                self.codigoA.move(400,70)
                self.nombreA.move(400,170)
                self.modeloA.move(400,270)
                self.precioA.move(400,370)
                self.cantidadA.move(400,470)
                
       def gotoCRUD_POK(self):
              self.label.setPixmap(QPixmap("Interfaz_Grafica/pokAS.png"))
              self.label_15.setPixmap(QPixmap("Interfaz_Grafica/pokAS.png"))
              self.label_16.setPixmap(QPixmap("Interfaz_Grafica/pokAS.png"))
              self.label_17.setPixmap(QPixmap("Interfaz_Grafica/pokAS.png"))
              self.label_18.setPixmap(QPixmap("Interfaz_Grafica/pokAS.png"))
              self.tabla_productosPo.move(300, 100)
              self.bt_refrescarPo.move(575, 600)
              
              self.codigoB_2.move(600, 50)
              self.label_2.move(450, 50)

              self.codigoB_2.setVisible(True)
              self.label_2.setVisible(True)
              self.tabla_buscarPo.move(300, 100)
              self.bt_buscarPo.move(575, 600)
              self.bt_refrescar.setVisible(False)
              self.bt_agregar.setVisible(False)
              self.bt_buscar.setVisible(False)
              self.bt_borrar.setVisible(False)
              self.bt_actualizar.setVisible(False)
              self.tabla_productos.setVisible(False)
              self.tabla_borrar.setVisible(False)
              self.tabla_buscar.setVisible(False)
              self.tabla_productosPo.setVisible(True)
              self.bt_refrescarPo.setVisible(True)
              self.codigoB.setVisible(False)
              self.codigoB_2.setVisible(True)
              self.tabla_buscarPo.setVisible(True)
              self.bt_buscarPo.setVisible(True)
              self.bt_borrarPO.setVisible(True)
              self.tabla_borrarPO.setVisible(True)
              self.codigo_borrarPO.setVisible(True)
              self.borrar_okPO.setVisible(True)
              self.borrar_ok.setVisible(False)
              self.codigo_borrar.setVisible(False)
              self.label_3.setVisible(False)
              self.label_4.setVisible(False)
              self.label_5.setVisible(False)
              self.label_6.setVisible(False)
              self.label_7.setVisible(False)
              self.codigoA.setVisible(False)
              self.nombreA.setVisible(False)
              self.modeloA.setVisible(False)
              self.precioA.setVisible(False)
              self.cantidadA.setVisible(False)
              self.datosTotal = Registro_datos_Pok()
              self.label_21.setVisible(True)
              self.label_20.setVisible(True)
              self.label_22.setVisible(True)
              self.label_23.setVisible(True)
              self.label_25.setVisible(True)
              self.label_26.setVisible(True)
              self.label_27.setVisible(True)
              self.label_28.setVisible(True)
              self.label_29.setVisible(True)
              self.label_30.setVisible(True)
              self.label_31.setVisible(True)
              self.label_32.setVisible(True)
              self.label_24.setVisible(True)
              self.label_33.setVisible(True)
              self.label_34.setVisible(True)
              self.label_35.setVisible(True)
              self.label_36.setVisible(True)
              self.a1.setVisible(True)
              self.a2.setVisible(True)
              self.a3.setVisible(True)
              self.a4.setVisible(True)
              self.a5.setVisible(True)
              self.a6.setVisible(True)
              self.a7.setVisible(True)
              self.a8.setVisible(True)
              self.a9.setVisible(True)
              self.a10.setVisible(True)
              self.a11.setVisible(True)
              self.a12.setVisible(True)
              self.a13.setVisible(True)
              self.a14.setVisible(True)
              self.a15.setVisible(True)
              self.a16.setVisible(True)
              self.a17.setVisible(True)
              self.bt_agregarPO.setVisible(True)
              self.bt_refrescarPo.clicked.connect(self.m_productosPo)
              self.bt_buscarPo.clicked.connect(self.buscar_productoPO)
              self.bt_borrarPO.clicked.connect(self.eliminar_productoPo)
              self.bt_agregarPO.clicked.connect(self.insert_productosPo)
              self.label_21.move(250,35)
              self.label_20.move(250,70)
              self.label_22.move(250,105)
              self.label_23.move(250,140)
              self.label_25.move(250,175)
              self.label_26.move(250,210)
              self.label_27.move(250,245)
              self.label_28.move(250,280)
              self.label_29.move(250,315)
              self.label_30.move(250,350)
              self.label_31.move(250,385)
              self.label_32.move(250,420)
              self.label_24.move(250,455)
              self.label_33.move(250,490)
              self.label_34.move(250,525)
              self.label_35.move(250,560)
              self.label_36.move(250,595)
              self.a1.move(400,35)
              self.a2.move(400,70)
              self.a3.move(400,105)
              self.a4.move(400,140)
              self.a5.move(400,175)
              self.a6.move(400,210)
              self.a7.move(400,245)
              self.a8.move(400,280)
              self.a9.move(400,315)
              self.a10.move(400,350)
              self.a11.move(400,385)
              self.a12.move(400,420)
              self.a13.move(400,455)
              self.a14.move(400,490)
              self.a15.move(400,525)
              self.a16.move(400,560)
              self.a17.move(400,595)
              

                
       def gotoCRUD_Prcts(self):
              self.label.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
              self.label_15.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
              self.label_16.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
              self.label_17.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
              self.label_18.setPixmap(QPixmap("Interfaz_Grafica/123sd.png"))
              width = 1500
              height = 830 
              self.setFixedSize(width,height)
              self.datosTotal = Registro_datos()
              self.bt_refrescar.clicked.connect(self.m_productos)
              self.bt_agregar.clicked.connect(self.insert_productos)
              self.bt_buscar.clicked.connect(self.buscar_producto)
              self.bt_borrar.clicked.connect(self.eliminar_producto)
              self.bt_actualizar.clicked.connect(self.modificar_productos)
              self.tabla_productos.setColumnWidth(0,98)
              self.tabla_productos.setColumnWidth(1,100)
              self.tabla_productos.setColumnWidth(2,98)
              self.tabla_productos.setColumnWidth(3,98)
              self.tabla_productos.setColumnWidth(4,98)
              self.tabla_borrar.setColumnWidth(0,98)
              self.tabla_borrar.setColumnWidth(1,100)
              self.tabla_borrar.setColumnWidth(2,98)
              self.tabla_borrar.setColumnWidth(3,98)
              self.tabla_borrar.setColumnWidth(4,98)
              self.tabla_buscar.setColumnWidth(0,98)
              self.tabla_buscar.setColumnWidth(1,100)
              self.tabla_buscar.setColumnWidth(2,98)
              self.tabla_buscar.setColumnWidth(3,98)
              self.tabla_buscar.setColumnWidth(4,98)
              self.tabla_productosPo.setVisible(False)
              self.bt_refrescarPo.setVisible(False)
              self.bt_refrescar.setVisible(True)
              self.bt_agregar.setVisible(True)
              self.bt_buscar.setVisible(True)
              self.bt_borrar.setVisible(True)
              self.bt_actualizar.setVisible(True)
              self.tabla_productos.setVisible(True)
              self.tabla_borrar.setVisible(True)
              self.tabla_buscar.setVisible(True)
              self.codigoB_2.setVisible(False)
              self.tabla_buscarPo.setVisible(False)
              self.bt_buscarPo.setVisible(False)
              self.codigoB.setVisible(True)
              self.bt_borrarPO.setVisible(False)
              self.tabla_borrarPO.setVisible(False)
              self.codigo_borrarPO.setVisible(False)
              self.borrar_okPO.setVisible(False)
              self.label_21.setVisible(False)
              self.label_20.setVisible(False)
              self.label_22.setVisible(False)
              self.label_23.setVisible(False)
              self.label_25.setVisible(False)
              self.label_26.setVisible(False)
              self.label_27.setVisible(False)
              self.label_28.setVisible(False)
              self.label_29.setVisible(False)
              self.label_30.setVisible(False)
              self.label_31.setVisible(False)
              self.label_32.setVisible(False)
              self.label_24.setVisible(False)
              self.label_33.setVisible(False)
              self.label_34.setVisible(False)
              self.label_35.setVisible(False)
              self.label_36.setVisible(False)
              self.a1.setVisible(False)
              self.a2.setVisible(False)
              self.a3.setVisible(False)
              self.a4.setVisible(False)
              self.a5.setVisible(False)
              self.a6.setVisible(False)
              self.a7.setVisible(False)
              self.a8.setVisible(False)
              self.a9.setVisible(False)
              self.a10.setVisible(False)
              self.a11.setVisible(False)
              self.a12.setVisible(False)
              self.a13.setVisible(False)
              self.a14.setVisible(False)
              self.a15.setVisible(False)
              self.a16.setVisible(False)
              self.a17.setVisible(False)
              self.label_3.setVisible(True)
              self.label_4.setVisible(True)
              self.label_5.setVisible(True)
              self.label_6.setVisible(True)
              self.label_7.setVisible(True)
              self.codigoA.setVisible(True)
              self.nombreA.setVisible(True)
              self.modeloA.setVisible(True)
              self.precioA.setVisible(True)
              self.cantidadA.setVisible(True)
              self.bt_agregarPO.setVisible(False)
              self.tabla_productos.move(300, 100)
              self.bt_refrescar.move(575, 600)
              self.codigoB.move(600, 50)
              self.label_2.move(450, 50)
              self.tabla_buscar.move(300, 100)
              self.bt_buscar.move(575, 600)
              self.label_3.move(250,50)
              self.label_4.move(250,150)
              self.label_5.move(250,250)
              self.label_6.move(250,350)
              self.label_7.move(250,450)
              self.codigoA.move(400,70)
              self.nombreA.move(400,170)
              self.modeloA.move(400,270)
              self.precioA.move(400,370)
              self.cantidadA.move(400,470)
        
       def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)


class Screen5(QMainWindow):
        def __init__(self):
              super(Screen5,self).__init__()
              loadUi("Interfaz_Grafica/talbex.ui",self)
              self.pushButton_6.clicked.connect(self.gotoScreen1)
              self.pushButton_8.clicked.connect(self.gotoScreen2)
              self.pushButton_9.clicked.connect(self.gotoScreen3)
              self.pushButton_7.clicked.connect(self.gotoScreen4)
              self.Pajs.setVisible(True)
              self.Pajs_2.setVisible(True)
              self.Pajs_3.setVisible(True)
              self.Pajs_4.setVisible(True)
              self.Pajs_4.setVisible(True)
              self.NetMy.setVisible(False)
              self.Net_My2.setVisible(False)
              self.Net_My3.setVisible(False)
              self.Net_My4.setVisible(False)
              self.DisnetMy_2.setVisible(False)
              self.Disnet_My2_2.setVisible(False)
              self.Disnet_My3_2.setVisible(False)
              self.Disnet_My4_2.setVisible(False)
              self.Region_MS.setVisible(False)
              self.Provincia_MS.setVisible(False)
              self.Comuna_MS.setVisible(False)
              self.Comuna_SQLS.setVisible(False)
              self.Provincia_SQLS.setVisible(False)
              self.Region_SQLS.setVisible(False)
              self.Region_Post.setVisible(False)
              self.Comuna_Post.setVisible(False)
              self.Provincia_Post.setVisible(False)
              self.Comuna_Mongo.setVisible(False)
              self.Region_Mongo.setVisible(False)
              self.Provincia_Mongo.setVisible(False)
              self.Pajs.setColumnWidth(0, 50)
              self.Pajs.setColumnWidth(1, 110)
              self.Pajs.setColumnWidth(2, 50)
              self.Pajs.setColumnWidth(3, 110)
              self.Pajs.setColumnWidth(4, 110)
              self.Pajs.setColumnWidth(5, 50)
              self.Pajs.setColumnWidth(6, 110)
              self.Pajs.setColumnWidth(7, 110)
              self.Pajs.setColumnWidth(8, 50)
              self.Pajs.setColumnWidth(9, 50)
              self.Pajs.setColumnWidth(10, 50)
              self.Pajs.setColumnWidth(11, 110)
              self.Pajs.setColumnWidth(12, 110)
              self.Pajs.setColumnWidth(13, 110)
              self.label.setPixmap(QPixmap("Interfaz_Grafica/kjnk.png"))
              self.loaddata()
              self.loaddataSQLS()
              self.loaddataPost()
              self.loadMong()

        def loadMong(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBANME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Pajs_4.setRowCount(898)
              for row in result:
                     self.Pajs_4.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['type_number'])))
                     self.Pajs_4.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['name'])))
                     self.Pajs_4.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['generation'])))
                     self.Pajs_4.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row['status'])))
                     self.Pajs_4.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row['species'])))
                     self.Pajs_4.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row['type_number'])))
                     self.Pajs_4.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row['type_1'])))
                     self.Pajs_4.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row['type_2'])))
                     self.Pajs_4.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row['height_m'])))
                     self.Pajs_4.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row['weight_kg'])))
                     self.Pajs_4.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row['abilities_number'])))
                     self.Pajs_4.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row['ability_1'])))
                     self.Pajs_4.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(row['ability_2'])))
                     self.Pajs_4.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(row['ability_hidden'])))
                     tablerow+=1
       
              
              
        def loadMongNet(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBNAME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Net_My4.setRowCount(898)
              for row in result:
                     self.Net_My4.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['show_id'])))
                     self.Net_My4.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['type'])))
                     self.Net_My4.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['title'])))
                     
                     
                     
                     self.Net_My4.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row['release_year'])))
                    
                     self.Net_My4.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row['listed_in'])))
                     self.Net_My4.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row['description'])))
                     tablerow+=1
        
        def loadMongDisney(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBNAME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Disnet_My4_2.setRowCount(898)
              for row in result:
                     self.Disnet_My4_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['show_id'])))
                     self.Disnet_My4_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['type'])))
                     self.Disnet_My4_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['title'])))
                     
                     
                     
                     self.Disnet_My4_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row['release_year'])))
                    
                     self.Disnet_My4_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row['listed_in'])))
                     self.Disnet_My4_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row['description'])))
                     tablerow+=1
       
        def MongoRegion(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBNAME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Region_Mongo.setRowCount(898)
              for row in result:
                     self.Region_Mongo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['id'])))
                     self.Region_Mongo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['nombre'])))
                     self.Region_Mongo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['ISO_3166_2_CL'])))
                     tablerow+=1

        def MongoProvincia(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBNAME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Provincia_Mongo.setRowCount(898)
              for row in result:
                     self.Provincia_Mongo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['id'])))
                     self.Provincia_Mongo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['nombre'])))
                     self.Provincia_Mongo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['idRegion'])))
                     tablerow+=1

        def MongoComuna(self):
              mongoDB_client = MongoClient()
              mongoDB_client = MongoClient('localhost', 27017)
              mongoDB_db = mongoDB_client["DBNAME"]
              mongoDB_collection = mongoDB_db["COLLECTION"]
              result=(mongoDB_collection.find())
              tablerow=0
              self.Comuna_Mongo.setRowCount(898)
              for row in result:
                     self.Comuna_Mongo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['id'])))
                     self.Comuna_Mongo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['nombre'])))
                     self.Comuna_Mongo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['idProvincia'])))
                     tablerow+=1


        def loaddataPost(self):
              conn = psycopg2.connect(dbname="DBNAME", user="USER",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM pokemones'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Pajs_3.setRowCount(898)
              for row in registro:
                     self.Pajs_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Pajs_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Pajs_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Pajs_3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Pajs_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Pajs_3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Pajs_3.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Pajs_3.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Pajs_3.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Pajs_3.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Pajs_3.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Pajs_3.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     self.Pajs_3.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(row[12])))
                     self.Pajs_3.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(row[13])))
                     tablerow+=1
        
        def RegionPost(self):
              conn = psycopg2.connect(dbname="DBNAME", user="USER",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM tbl_region'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Region_Post.setRowCount(898)
              for row in registro:
                     self.Region_Post.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Region_Post.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Region_Post.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1
        
        def ProvinciaPost(self):
              conn = psycopg2.connect(dbname="DBNAME", user="postgres",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM tbl_provincia'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Provincia_Post.setRowCount(898)
              for row in registro:
                     self.Provincia_Post.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Provincia_Post.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Provincia_Post.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1

        def ComunaPost(self):
              conn = psycopg2.connect(dbname="DBNAME", user="postgres",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM tbl_comuna'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Comuna_Post.setRowCount(898)
              for row in registro:
                     self.Comuna_Post.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Comuna_Post.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Comuna_Post.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1
              
        def loaddataPostNet(self):
              conn = psycopg2.connect(dbname="DBNAME", user="postgres",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM netflix'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Net_My3.setRowCount(898)
              for row in registro:
                     self.Net_My3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Net_My3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Net_My3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Net_My3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Net_My3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Net_My3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Net_My3.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Net_My3.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Net_My3.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Net_My3.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Net_My3.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Net_My3.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     tablerow+=1
       
        def loaddataPostDisen(self):
              conn = psycopg2.connect(dbname="DBNAME", user="postgres",
                            password="PASSWORD", host="localhost", port="5432")
              cur = conn.cursor()
              sqlstr = 'SELECT * FROM disney'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Disnet_My3_2.setRowCount(898)
              for row in registro:
                     self.Disnet_My3_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Disnet_My3_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Disnet_My3_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Disnet_My3_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Disnet_My3_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Disnet_My3_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Disnet_My3_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Disnet_My3_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Disnet_My3_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Disnet_My3_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Disnet_My3_2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Disnet_My3_2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     tablerow+=1

        def loaddata(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM pokemones'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Pajs.setRowCount(898)
              for row in registro:
                     self.Pajs.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["pk_number"])))
                     self.Pajs.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["name"])))
                     self.Pajs.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["generation"])))
                     self.Pajs.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row["status"])))
                     self.Pajs.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row["species"])))
                     self.Pajs.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row["number_type"])))
                     self.Pajs.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row["type_1"])))
                     self.Pajs.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row["type_2"])))
                     self.Pajs.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row["height"])))
                     self.Pajs.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row["weight"])))
                     self.Pajs.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row["n_abilities"])))
                     self.Pajs.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row["abilities_1"])))
                     self.Pajs.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(row["abilities_2"])))
                     self.Pajs.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(row["abilities_hidden"])))
                     tablerow+=1

        def ComunaMY(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM tbl_comuna'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Comuna_MS.setRowCount(898)
              for row in registro:
                     self.Comuna_MS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["id"])))
                     self.Comuna_MS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["nombre"])))
                     self.Comuna_MS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["idProvincia"])))
                     tablerow+=1
        
        def ProvinciaMY(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM tbl_provincia'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Provincia_MS.setRowCount(898)
              for row in registro:
                     self.Provincia_MS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["id"])))
                     self.Provincia_MS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["nombre"])))
                     self.Provincia_MS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["idRegion"])))
                     tablerow+=1

        def RegionMY(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM tbl_region'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Region_MS.setRowCount(898)
              for row in registro:
                     self.Region_MS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["id"])))
                     self.Region_MS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["nombre"])))
                     self.Region_MS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["ISO_3166_2_CL"])))
                     tablerow+=1
       
        
        
        def loaddataMy(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBANME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM netflix'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.NetMy.setRowCount(898)
              for row in registro:
                     self.NetMy.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["show_id"])))
                     self.NetMy.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["type"])))
                     self.NetMy.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["title"])))
                     self.NetMy.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row["director"])))
                     self.NetMy.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row["cast"])))
                     self.NetMy.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row["country"])))
                     self.NetMy.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row["date_added"])))
                     self.NetMy.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row["release_year"])))
                     self.NetMy.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row["rating"])))
                     self.NetMy.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row["duration"])))
                     self.NetMy.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row["listed_in"])))
                     self.NetMy.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row["description"])))
                     tablerow+=1
        
        def loaddataMyDis(self):
              DB_IP = 'localhost'
              DB_ID = "USER"
              DB_PW = "PASSWORD"
              MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='DBNAME', charset='utf8mb4', cursorclass=cursors.DictCursor)
              cur = MySQL_db.cursor()
              sqlstr = 'SELECT * FROM disney'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.DisnetMy_2.setRowCount(898)
              for row in registro:
                     self.DisnetMy_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["show_id"])))
                     self.DisnetMy_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row["type"])))
                     self.DisnetMy_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row["title"])))
                     self.DisnetMy_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row["director"])))
                     self.DisnetMy_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row["cast"])))
                     self.DisnetMy_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row["country"])))
                     self.DisnetMy_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row["date_added"])))
                     self.DisnetMy_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row["release_year"])))
                     self.DisnetMy_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row["rating"])))
                     self.DisnetMy_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row["duration"])))
                     self.DisnetMy_2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row["listed_in"])))
                     self.DisnetMy_2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row["description"])))
                     tablerow+=1

        def loaddataSQLSNet(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM netflix'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Net_My2.setRowCount(898)
              for row in registro:
                     self.Net_My2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Net_My2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Net_My2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Net_My2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Net_My2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Net_My2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Net_My2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Net_My2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Net_My2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Net_My2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Net_My2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Net_My2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     tablerow+=1

        def ComunaSQLS(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM tbl_comuna'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Comuna_SQLS.setRowCount(898)
              for row in registro:
                     self.Comuna_SQLS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Comuna_SQLS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Comuna_SQLS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1
       
        def ProvinciaSQLS(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM tbl_provincia'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Provincia_SQLS.setRowCount(898)
              for row in registro:
                     self.Provincia_SQLS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Provincia_SQLS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Provincia_SQLS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1
       
        def RegionSQLS(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM tbl_region'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Region_SQLS.setRowCount(898)
              for row in registro:
                     self.Region_SQLS.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Region_SQLS.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Region_SQLS.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     tablerow+=1

        def loaddataSQLSDisney(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBNAME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM disney'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Disnet_My2_2.setRowCount(898)
              for row in registro:
                     self.Disnet_My2_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Disnet_My2_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Disnet_My2_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Disnet_My2_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Disnet_My2_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Disnet_My2_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Disnet_My2_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Disnet_My2_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Disnet_My2_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Disnet_My2_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Disnet_My2_2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Disnet_My2_2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     tablerow+=1

        def loaddataSQLS(self):
              conn_strR = (
                        r'DRIVER={SQL Server};'
                        r'SERVER=localhost\SQLEXPRESS;'
                        r'DATABASE=DBANME;'
                        r'Trusted_Connection=yes;')
                        
              cnxn = pyodbc.connect(conn_strR) 
              cur = cnxn.cursor()
              sqlstr = 'SELECT * FROM pokemon'
              tablerow=0
              cur.execute(sqlstr,)
              registro = cur.fetchall()
              self.Pajs_2.setRowCount(898)
              for row in registro:
                     self.Pajs_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                     self.Pajs_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                     self.Pajs_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                     self.Pajs_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                     self.Pajs_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                     self.Pajs_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                     self.Pajs_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                     self.Pajs_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                     self.Pajs_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                     self.Pajs_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                     self.Pajs_2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                     self.Pajs_2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                     self.Pajs_2.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(str(row[12])))
                     self.Pajs_2.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(str(row[13])))
                     tablerow+=1     
              
        
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)

        def gotoScreen2(self):
              self.label.setPixmap(QPixmap("Interfaz_Grafica/jjjjjjjj.png"))
              self.Pajs.setVisible(False)
              self.Pajs_2.setVisible(False)
              self.Pajs_3.setVisible(False)
              self.Pajs_4.setVisible(False)
              self.NetMy.setVisible(True)
              self.Net_My2.setVisible(True)
              self.Net_My3.setVisible(True)
              self.Net_My4.setVisible(True)
              self.DisnetMy_2.setVisible(True)
              self.Disnet_My2_2.setVisible(True)
              self.Disnet_My3_2.setVisible(True)
              self.Disnet_My4_2.setVisible(True)
              self.Region_MS.setVisible(False)
              self.Provincia_MS.setVisible(False)
              self.Comuna_MS.setVisible(False)
              self.Comuna_SQLS.setVisible(False)
              self.Provincia_SQLS.setVisible(False)
              self.Region_SQLS.setVisible(False)
              self.Region_Post.setVisible(False)
              self.Comuna_Post.setVisible(False)
              self.Provincia_Post.setVisible(False)
              self.Comuna_Mongo.setVisible(False)
              self.Region_Mongo.setVisible(False)
              self.Provincia_Mongo.setVisible(False)
              self.loaddataMy()
              self.loaddataSQLSNet()
              self.loaddataPostNet()
              self.loadMongNet()
              self.loaddataMyDis()
              self.loaddataSQLSDisney()
              self.loaddataPostDisen()
              self.loadMongDisney()
              

        def gotoScreen3(self):
              self.label.setPixmap(QPixmap("Interfaz_Grafica/Mapa-Ubicación-Chile.png"))
              self.Pajs.setVisible(False)
              self.Pajs_2.setVisible(False)
              self.Pajs_3.setVisible(False)
              self.Pajs_4.setVisible(False)
              self.NetMy.setVisible(False)
              self.Net_My2.setVisible(False)
              self.Net_My3.setVisible(False)
              self.Net_My4.setVisible(False)
              self.DisnetMy_2.setVisible(False)
              self.Disnet_My2_2.setVisible(False)
              self.Disnet_My3_2.setVisible(False)
              self.Disnet_My4_2.setVisible(False)
              self.Region_MS.setVisible(True)
              self.Provincia_MS.setVisible(True)
              self.Comuna_MS.setVisible(True)
              self.Region_SQLS.setVisible(True)
              self.Comuna_SQLS.setVisible(True)
              self.Provincia_SQLS.setVisible(True)
              self.Region_Post.setVisible(True)
              self.Comuna_Post.setVisible(True)
              self.Provincia_Post.setVisible(True)
              self.Comuna_Mongo.setVisible(True)
              self.Region_Mongo.setVisible(True)
              self.Provincia_Mongo.setVisible(True)
              self.RegionSQLS()
              self.ProvinciaSQLS()
              self.ComunaSQLS()
              self.ComunaMY()
              self.ProvinciaMY()
              self.RegionMY()
              self.ComunaPost()
              self.ProvinciaPost()
              self.RegionPost()
              self.MongoComuna()
              self.MongoRegion()
              self.MongoProvincia()
             
        
        def gotoScreen4(self):
              self.label.setPixmap(QPixmap("Interfaz_Grafica/kjnk.png"))
              self.Pajs.setVisible(True)
              self.Pajs_2.setVisible(True)
              self.Pajs_3.setVisible(True)
              self.Pajs_4.setVisible(True)
              self.NetMy.setVisible(False)
              self.Net_My2.setVisible(False)
              self.Net_My3.setVisible(False)
              self.Net_My4.setVisible(False)
              self.DisnetMy_2.setVisible(False)
              self.Disnet_My2_2.setVisible(False)
              self.Disnet_My3_2.setVisible(False)
              self.Disnet_My4_2.setVisible(False)
              self.Region_MS.setVisible(False)
              self.Provincia_MS.setVisible(False)
              self.Comuna_MS.setVisible(False)
              self.Comuna_SQLS.setVisible(False)
              self.Provincia_SQLS.setVisible(False)
              self.Region_SQLS.setVisible(False)
              self.Region_Post.setVisible(False)
              self.Comuna_Post.setVisible(False)
              self.Provincia_Post.setVisible(False)
              self.Comuna_Mongo.setVisible(False)
              self.Region_Mongo.setVisible(False)
              self.Provincia_Mongo.setVisible(False)
              self.loaddata()
              self.loaddataSQLS()
              self.loaddataPost()
              self.loadMong()

                

        


       
       



class Screen6(QMainWindow):
        def __init__(self):
                super(Screen6,self).__init__()
                loadUi("Interfaz_Grafica/h.ui",self)
                self.pushButton_6.clicked.connect(self.gotoScreen1)
                self.pushButton_69.clicked.connect(self.gotoCata)
                self.pushButton_70.clicked.connect(self.gotoPopuGe)
                self.pushButton_71.clicked.connect(self.gotoTendeanu)
                self.pushButton_72.clicked.connect(self.gotolastmonth)
                self.pushButton_73.clicked.connect(self.gotoTipLic)
                self.pushButton_74.clicked.connect(self.gotoTenLi)
                self.pushButton_75.clicked.connect(self.gotoTenxDB)

                width = 1500
                height = 830
                self.setFixedSize(width,height)
                self.label_2.setPixmap(QPixmap("Interfaz_Grafica/r7.png"))
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
                self.pushButton_53.setCursor(Qt.PointingHandCursor) 
                self.pushButton_53.clicked.connect(self.algo)
                self.pushButton_54.setCursor(Qt.PointingHandCursor) 
                self.pushButton_54.clicked.connect(self.zure)
                self.pushButton_55.setCursor(Qt.PointingHandCursor) 
                self.pushButton_55.clicked.connect(self.kdb)
                self.pushButton_56.setCursor(Qt.PointingHandCursor) 
                self.pushButton_56.clicked.connect(self.single)
                self.pushButton_57.setCursor(Qt.PointingHandCursor) 
                self.pushButton_57.clicked.connect(self.esfinge)
                self.pushButton_58.setCursor(Qt.PointingHandCursor) 
                self.pushButton_58.clicked.connect(self.gallo)
                self.pushButton_59.setCursor(Qt.PointingHandCursor) 
                self.pushButton_59.clicked.connect(self.prome)
                self.pushButton_60.setCursor(Qt.PointingHandCursor) 
                self.pushButton_60.clicked.connect(self.riak)
                self.pushButton_61.setCursor(Qt.PointingHandCursor) 
                self.pushButton_61.clicked.connect(self.ignite)
                self.pushButton_62.setCursor(Qt.PointingHandCursor) 
                self.pushButton_62.clicked.connect(self.liebre)
                self.pushButton_63.setCursor(Qt.PointingHandCursor) 
                self.pushButton_63.clicked.connect(self.interbase)
                self.pushButton_64.setCursor(Qt.PointingHandCursor) 
                self.pushButton_64.clicked.connect(self.ehcache)
                self.pushButton_65.setCursor(Qt.PointingHandCursor) 
                self.pushButton_65.clicked.connect(self.ingres)                 
                self.pushButton_66.setCursor(Qt.PointingHandCursor) 
                self.pushButton_66.clicked.connect(self.aero)
                self.pushButton_67.setCursor(Qt.PointingHandCursor) 
                self.pushButton_67.clicked.connect(self.any)
     
        def gotoCata(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/r7.png"))
              self.pushButton_2.setEnabled(True)
              self.pushButton_3.setEnabled(True)
              self.pushButton_4.setEnabled(True) 
              self.pushButton_5.setEnabled(True)
              self.pushButton_7.setEnabled(True) 
              self.pushButton_8.setEnabled(True) 
              self.pushButton_9.setEnabled(True) 
              self.pushButton_10.setEnabled(True)
              self.pushButton_11.setEnabled(True)
              self.pushButton_12.setEnabled(True)
              self.pushButton_13.setEnabled(True)
              self.pushButton_14.setEnabled(True)
              self.pushButton_15.setEnabled(True)
              self.pushButton_16.setEnabled(True)
              self.pushButton_17.setEnabled(True)
              self.pushButton_18.setEnabled(True)
              self.pushButton_19.setEnabled(True)
              self.pushButton_20.setEnabled(True)
              self.pushButton_21.setEnabled(True)
              self.pushButton_22.setEnabled(True)
              self.pushButton_23.setEnabled(True)
              self.pushButton_24.setEnabled(True)
              self.pushButton_25.setEnabled(True)
              self.pushButton_26.setEnabled(True) 
              self.pushButton_28.setEnabled(True) 
              self.pushButton_29.setEnabled(True)
              self.pushButton_30.setEnabled(True)
              self.pushButton_31.setEnabled(True) 
              self.pushButton_32.setEnabled(True) 
              self.pushButton_33.setEnabled(True) 
              self.pushButton_34.setEnabled(True)
              self.pushButton_35.setEnabled(True)
              self.pushButton_36.setEnabled(True)
              self.pushButton_37.setEnabled(True)
              self.pushButton_38.setEnabled(True) 
              self.pushButton_39.setEnabled(True) 
              self.pushButton_40.setEnabled(True)
              self.pushButton_41.setEnabled(True) 
              self.pushButton_42.setEnabled(True) 
              self.pushButton_43.setEnabled(True) 
              self.pushButton_44.setEnabled(True)
              self.pushButton_45.setEnabled(True)
              self.pushButton_46.setEnabled(True) 
              self.pushButton_47.setEnabled(True) 
              self.pushButton_48.setEnabled(True)
              self.pushButton_49.setEnabled(True)
              self.pushButton_50.setEnabled(True)
              self.pushButton_51.setEnabled(True) 
              self.pushButton_52.setEnabled(True)
              self.pushButton_53.setEnabled(True) 
              self.pushButton_54.setEnabled(True) 
              self.pushButton_55.setEnabled(True) 
              self.pushButton_56.setEnabled(True) 
              self.pushButton_57.setEnabled(True) 
              self.pushButton_58.setEnabled(True) 
              self.pushButton_59.setEnabled(True) 
              self.pushButton_60.setEnabled(True) 
              self.pushButton_61.setEnabled(True) 
              self.pushButton_62.setEnabled(True) 
              self.pushButton_63.setEnabled(True) 
              self.pushButton_64.setEnabled(True) 
              self.pushButton_65.setEnabled(True) 
              self.pushButton_66.setEnabled(True) 
              self.pushButton_67.setEnabled(True)

        def gotoPopuGe(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/xTs.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False) 
                
       
        def gotoTendeanu(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/rsg1.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False)

        def gotolastmonth(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/rsg2.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False)

        def gotoTipLic(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/rsg3.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False)

        def gotoTenLi(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/rsg4.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False)

        def gotoTenxDB(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/rsg5.png"))
              self.pushButton_2.setEnabled(False)
              self.pushButton_3.setEnabled(False)
              self.pushButton_4.setEnabled(False) 
              self.pushButton_5.setEnabled(False)
              self.pushButton_7.setEnabled(False) 
              self.pushButton_8.setEnabled(False) 
              self.pushButton_9.setEnabled(False) 
              self.pushButton_10.setEnabled(False)
              self.pushButton_11.setEnabled(False)
              self.pushButton_12.setEnabled(False)
              self.pushButton_13.setEnabled(False)
              self.pushButton_14.setEnabled(False)
              self.pushButton_15.setEnabled(False)
              self.pushButton_16.setEnabled(False)
              self.pushButton_17.setEnabled(False)
              self.pushButton_18.setEnabled(False)
              self.pushButton_19.setEnabled(False)
              self.pushButton_20.setEnabled(False)
              self.pushButton_21.setEnabled(False)
              self.pushButton_22.setEnabled(False)
              self.pushButton_23.setEnabled(False)
              self.pushButton_24.setEnabled(False)
              self.pushButton_25.setEnabled(False)
              self.pushButton_26.setEnabled(False) 
              self.pushButton_28.setEnabled(False) 
              self.pushButton_29.setEnabled(False)
              self.pushButton_30.setEnabled(False)
              self.pushButton_31.setEnabled(False) 
              self.pushButton_32.setEnabled(False) 
              self.pushButton_33.setEnabled(False) 
              self.pushButton_34.setEnabled(False)
              self.pushButton_35.setEnabled(False)
              self.pushButton_36.setEnabled(False)
              self.pushButton_37.setEnabled(False)
              self.pushButton_38.setEnabled(False) 
              self.pushButton_39.setEnabled(False) 
              self.pushButton_40.setEnabled(False)
              self.pushButton_41.setEnabled(False) 
              self.pushButton_42.setEnabled(False) 
              self.pushButton_43.setEnabled(False) 
              self.pushButton_44.setEnabled(False)
              self.pushButton_45.setEnabled(False)
              self.pushButton_46.setEnabled(False) 
              self.pushButton_47.setEnabled(False) 
              self.pushButton_48.setEnabled(False)
              self.pushButton_49.setEnabled(False)
              self.pushButton_50.setEnabled(False)
              self.pushButton_51.setEnabled(False) 
              self.pushButton_52.setEnabled(False)
              self.pushButton_53.setEnabled(False) 
              self.pushButton_54.setEnabled(False) 
              self.pushButton_55.setEnabled(False) 
              self.pushButton_56.setEnabled(False) 
              self.pushButton_57.setEnabled(False) 
              self.pushButton_58.setEnabled(False) 
              self.pushButton_59.setEnabled(False) 
              self.pushButton_60.setEnabled(False) 
              self.pushButton_61.setEnabled(False) 
              self.pushButton_62.setEnabled(False) 
              self.pushButton_63.setEnabled(False) 
              self.pushButton_64.setEnabled(False) 
              self.pushButton_65.setEnabled(False) 
              self.pushButton_66.setEnabled(False) 
              self.pushButton_67.setEnabled(False)



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

        def zure(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/zure.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Microsoft Azure Search')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def algo(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/algo.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Algolia')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def kdb(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/kdb.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha kdb+')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def single(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/single.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha SingleStore')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def esfinge(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/esfinge.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Sphinx')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def gallo(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/gallo.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha CockroachDB')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def ignite(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ignite.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Ignite')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def riak(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/Riak.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Riak KV')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def liebre(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/liebre.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Jackrabbit')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def interbase(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/interbase.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Interbase')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()
       
        def ehcache(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ehcache.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Ehcache')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def ingres(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/ingres.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Ingres')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def prome(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/prome.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Prometheus')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def aero(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/aero.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha Aerospike')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

        def any(self):
               root= tk.Tk()
               upload= Image.open("Interfaz_Grafica/any.png")
               image=ImageTk.PhotoImage(upload)
               label= Label(root,image=image)
               label.place(x=0,y=0)
               root.title('Ficha SAP SQL Anywhere')
               root.geometry('1520x610')
               root.resizable (0,0)
               root.tk.call('wm', 'iconphoto', root, tk.PhotoImage(file='database-setting.png'))
               root.mainloop()

class Screen7(QMainWindow):
        def __init__(self):
                super(Screen7,self).__init__()
                loadUi("Interfaz_Grafica/h7.ui",self)
                self.pushButton_6.clicked.connect(self.gotoScreen1)
                self.pushButton_69.clicked.connect(self.gotoT1M1)
                self.pushButton_70.clicked.connect(self.gotoT2M1)
                self.pushButton_71.clicked.connect(self.gotoT3M1)
                self.pushButton_72.clicked.connect(self.gotoT1M2)
                self.pushButton_73.clicked.connect(self.gotoT2M2)
                self.pushButton_74.clicked.connect(self.gotoT3M2)
                self.pushButton_75.clicked.connect(self.gotoT1M3)
                self.pushButton_76.clicked.connect(self.gotoT2M3)
                self.pushButton_77.clicked.connect(self.gotoT3M3)
                

                width = 1500
                height = 830
                self.setFixedSize(width,height)
                self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T1M1VIEW.png"))
       
        def gotoScreen1(self):
                mainwindow=MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)
        
        def gotoT1M1(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T1M1VIEW.png"))
        
        def gotoT2M1(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T2M1VIEW.png"))
       
        def gotoT3M1(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T3M1VIEW.png"))
  
        def gotoT1M2(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T1M2VIEW.png"))
         
        def gotoT2M2(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T2M2VIEW.png"))
         
        def gotoT3M2(self):
               self.label_2.setPixmap(QPixmap("Interfaz_Grafica/T3M2VIEW.png"))

        def gotoT3M3(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/M3T3_FI.png"))
       
        def gotoT1M3(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/M3T3_FI.png"))

        def gotoT2M3(self):
              self.label_2.setPixmap(QPixmap("Interfaz_Grafica/M3T3_FI.png"))




               
                
                

		

app= QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
widget.addWidget(mainwindow)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")