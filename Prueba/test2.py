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


def rand(entry_box):
    global random
    random=entry_box.get()
    print(random)
      

def rand1(entry_box2):
    global topic_str
    topic_str=entry_box2.get()

def rand2(entry_box3):
    global topic
    topic=entry_box3.get()
    

def Test3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn):
    global RUNNING3
    RUNNING3= True
    log_box3.insert(tk.END, ' Iniciando...')
    t3= threading.Thread(name = 'ping', target = TESTT3, daemon=False, args=(log_box3,MySQL_db,mongoDB_collection,cnxn,conn))
    t3.start()


def Test1(logbox,MySQL_db,mongoDB_collection,cnxn,conn):
    global RUNNING1
    RUNNING1= True
    logbox.insert(tk.END, ' Iniciando...')
    t1= threading.Thread(name = 'ping', target = TESTT1, daemon=False, args=(logbox,MySQL_db,mongoDB_collection,cnxn,conn))
    t1.start()
   

def Test2(log_box2,MySQL_db,mongoDB_collection,cnxn,conn):
    global RUNNING2
    RUNNING2= True
    log_box2.insert(tk.END, ' Iniciando...')
    t2= threading.Thread(name = 'ping', target = TESTT2, daemon=False, args=(log_box2,MySQL_db,mongoDB_collection,cnxn,conn))
    t2.start()

def TESTT3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn):
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames = ['Iteracion', 'Hora']
    if not os.path.exists('Data/MySQL_Test_3.csv'):
    
        with open('Data/MySQL_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/MySQL_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/Mongo_Test_3.csv'):
    
        with open('Data/Mongo_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Mongo_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/SQLServerTest_3.csv'):
    
        with open('Data/SQLServerTest_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/SQLServerTest_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()


    if not os.path.exists('Data/Postgres_Test_3.csv'):
    
        with open('Data/Postgres_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Postgres_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    
    global start7
    start7 = time.process_time()
    log_box3.insert(tk.END, ' TEST 3 MongoDB...')
    result =list( mongoDB_collection.find({'Nombre': {'$regex': topic}}))
    
    x1 = range(len(result))
    aux=start7/len(result)
    for n1 in x1:
        if(not RUNNING3):
                break
        a=n1
        b=aux
        aux=aux+start7/len(result)
        info1 = {
        'Iteracion': a,
        'Hora' : b,
        }
        with open('Data/Mongo_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames2 = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
            csv_writer.writerow(info1)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)

    

    global start4
    log_box3.insert(tk.END, ' \nTEST 3 MySQL...')
    start4 = time.process_time()
    with MySQL_db.cursor() as cursor:
        sql = "SELECT count(*) as cont FROM pais WHERE Nombre LIKE %s"
        temp_topic = '%' + topic + '%'
        cursor.execute(sql, (temp_topic,))
        result = cursor.fetchone()
        x2 = range(result.get("cont"))
        aux1=start4/result.get("cont")
        for n2 in x2:
            if(not RUNNING3):
                break
            a=n2
            b=aux1
            aux1=aux1+start4/result.get("cont")
            info = {
            'Iteracion': a,
            'Hora' : b,
            }
            with open('Data/MySQL_Test_3.csv', 'a', newline = '') as csv_file:
                fieldnames2 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
                csv_writer.writerow(info)
                log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
                log_box3.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)

    global start77
    log_box3.insert(tk.END, ' \nTEST 3 SQL Server...')
    start77 = time.process_time()
    with cnxn.cursor() as cursor:
        sqls="SELECT count(*) as cont FROM pais WHERE Nombre LIKE ?"
        temp_topic = '%' + topic + '%'
        cursor.execute(sqls, (temp_topic,))
        resultW = cursor.fetchone()
        x2 = range(resultW[0])
        aux1=start77/(resultW[0])
        for n2 in x2:
            if(not RUNNING3):
                break
            a=n2
            b=aux1
            aux1=aux1+start77/resultW[0]
            info = {
            'Iteracion': a,
            'Hora' : b,
            }
            with open('Data/SQLServerTest_3.csv', 'a', newline = '') as csv_file:
                fieldnames2 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
                csv_writer.writerow(info)
                log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
                log_box3.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)


    global start99
    log_box3.insert(tk.END, ' \nTEST 3 Postgres...')
    start99 = time.process_time()
    with conn.cursor() as cursor:
        sql99 = 'select count(*) from public."Paises" where "Nombre" like  %s'
        temp_topic = '%' + topic + '%'
        cursor.execute(sql99, (temp_topic,))
        resultZ = cursor.fetchone()
        x99 = range(resultZ[0])
        aux99=start99/(resultZ[0])
        for n99 in x99:
            if(not RUNNING3):
                break
            a99=n99
            b99=aux99
            aux99=aux99+start99/result.get("cont")
            info99 = {
            'Iteracion': a99,
            'Hora' : b99,
            }
            with open('Data/Postgres_Test_3.csv', 'a', newline = '') as csv_file:
                fieldnames2 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
                csv_writer.writerow(info99)
                log_box3.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
                log_box3.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)
    log_box3.insert(tk.END, '***\nTerminado Test3***')
        


	
		
def TESTT2(log_box2,MySQL_db,mongoDB_collection,cnxn,conn):
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames = ['Iteracion', 'Hora']
    if not os.path.exists('Data/MySQLTest_2.csv'):
    
        with open('Data/MySQLTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/MySQLTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/MongoTest_2.csv'):
    
        with open('Data/MongoTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/MongoTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    
    if not os.path.exists('Data/SQLServerTest_2.csv'):
    
        with open('Data/SQLServerTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/SQLServerTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/PostgresTest_2.csv'):
    
        with open('Data/PostgresTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/PostgresTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    global start3
    start3 = 0
    log_box2.insert(tk.END, ' TEST 2 MongoDB...')
    result=list(mongoDB_collection.find({'Nombre': topic_str}))
    star3=time.process_time() + start3
    
    x1 = range(len(result))
    aux=star3/len(result)
    for n1 in x1:
        if(not RUNNING2):
                break
        a1=n1
        b1=aux
        aux=aux+star3/len(result)
        infox = {
        'Iteracion': a1,
        'Hora' : b1,
        }
        with open('Data/MongoTest_2.csv', 'a', newline = '') as csv_file:
            fieldnames1 = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writerow(infox)
            log_box2.insert(tk.END, f"\n\n Iteracion: {a1}, Hora: {b1}")
            log_box2.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)

    

    global start4
    log_box2.insert(tk.END, ' \nTEST 2 MySQL...')
    start4 = 0
    aux1=0
    with MySQL_db.cursor() as cursor:
        sql = "SELECT Nombre FROM pais WHERE Nombre=%s;"
        cursor.execute(sql, (topic_str,))
        result = cursor.fetchall()
        start4=time.process_time() + start4
        x = range(len(result))
        aux1=start4/len(result)
        for n in x:
            if(not RUNNING2):
                break
            a1=n
            #print(a)
            b1=aux1
            aux1=aux1+start4/len(result)
            #print(b)
            infoy = {
                'Iteracion': a1,
                'Hora' : b1,}
            with open('Data/MySQLTest_2.csv', 'a', newline = '') as csv_file:
                fieldnames1 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
                csv_writer.writerow(infoy)
                log_box2.insert(tk.END, f"\n\n Iteracion: {a1}, Hora: {b1}")
                log_box2.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)

    global start8
    log_box2.insert(tk.END, ' \nTEST 2 SQL Server...')
    start8 = 0
    aux8=0
    with cnxn.cursor() as cursor:
        sqls = "SELECT Nombre FROM pais WHERE Nombre=?;"
        cursor.execute(sqls, (topic_str,))
        resultx = cursor.fetchall()
        print(len(resultx))
        start8=time.process_time() + start8
        x8 = range(len(resultx))
        aux8=start8/len(resultx)
        for n8 in x8:
            if(not RUNNING2):
                break
            a8=n8
            b8=aux8
            aux8=aux8+start8/len(resultx)
            infoz = {
                'Iteracion': a8,
                'Hora' : b8,}
            with open('Data/SQLServerTest_2.csv', 'a', newline = '') as csv_file:
                fieldnames1 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
                csv_writer.writerow(infoz)
                log_box2.insert(tk.END, f"\n\n Iteracion: {a8}, Hora: {b8}")
                log_box2.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)


    global start99
    log_box2.insert(tk.END, ' \nTEST 2 Postgres...')
    start99 = 0
    aux99=0
    with conn.cursor() as cursor:
        sqls = 'select * from public."Paises" where "Nombre"=%s;'
        cursor.execute(sqls, (topic_str,))
        resultx = cursor.fetchall()
        print(len(resultx))
        start99=time.process_time() + start99
        x99 = range(len(resultx))
        aux8=start99/len(resultx)
        for n99 in x99:
            if(not RUNNING2):
                break
            a99=n99
            b99=aux99
            aux99=aux99+start99/len(resultx)
            infob = {
                'Iteracion': a99,
                'Hora' : b99,}
            with open('Data/PostgresTest_2.csv', 'a', newline = '') as csv_file:
                fieldnames1 = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
                csv_writer.writerow(infob)
                log_box2.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
                log_box2.see("end") 
                cut_duration = 0
                scan_interval = 1
                time.sleep(scan_interval)

    log_box2.insert(tk.END, '***\nTerminado Test2***')
    
def TESTT1(log_box,MySQL_db,mongoDB_collection,cnxn,conn):
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames = ['Iteracion', 'Hora']
    if not os.path.exists('Data/Parte2_MySQLTest_1.csv'):
    
        with open('Data/Parte2_MySQLTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte2_MySQLTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/Parte2_MongoTest_1.csv'):
    
        with open('Data/Parte2_MongoTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte2_MongoTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/Parte2_SQLServerTest_1.csv'):
    
        with open('Data/Parte2_SQLServerTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte2_SQLServerTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    
    if not os.path.exists('Data/Parte2_PostgresTest_1.csv'):
    
        with open('Data/Parte2_PostgresTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte2_PostgresTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    global start69
    start69=0
    log_box.insert(tk.END, ' \nTEST 1 MongoDB...')
    if(random=='ASC'):
        list(mongoDB_collection.find().sort('title', -1))
        
    else:
        list(mongoDB_collection.find().sort('title', 1))
    start69=time.process_time() + start69
    a=1
    b= start69
    info1 = {
        'Iteracion': a,
        'Hora' : b,
        }
    with open('Data/Parte2_MongoTest_1.csv', 'a', newline = '') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
        csv_writer.writerow(info1)
        log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)


    global start70
    start70=0
    log_box.insert(tk.END, ' \nTEST 1 MySQL...')
    with MySQL_db.cursor() as cursor:
        if(random=='ASC'):
            sql = 'SELECT * FROM netflix order by title ASC'
        else:
            sql = 'SELECT * FROM netflix order by title DESC'
        cursor.execute(sql)
        result = cursor.fetchall()
        start70=time.process_time() + start70
        a=1
        b=start70
        info = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte2_MySQLTest_1.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info)
            log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        

    global start71
    start71=0
    log_box.insert(tk.END, ' \nTEST 1 SQL Server...')
    with cnxn.cursor() as cursor:
        if(random=='ASC'):
            sqls = "SELECT * FROM netflix order by title ASC;"
        else:
            sqls = "SELECT * FROM netflix order by title DESC;"
        
        cursor.execute(sqls)
        resultW = cursor.fetchall()
        start71=time.process_time() + start71
        a2=1
        b2=start71
        info3 = {
            'Iteracion': a2,
            'Hora' : b2,
            }
        with open('Data/Parte2_SQLServerTest_1.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info3)
            log_box.insert(tk.END, f"\n\n Iteracion: {a2}, Hora: {b2}")
            log_box.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
    
    global start81
    start81=0
    log_box.insert(tk.END, ' \nTEST 1 Postgres...')
    with conn.cursor() as cursor:
        if(random=='ASC'):
            sql99 = 'SELECT * FROM public."netflix"  ORDER BY "title" ASC'
        else:
            sql99 = 'SELECT * FROM public."netflix"  ORDER BY "title" DESC'

        cursor.execute(sql99)
        resultW = cursor.fetchall()
        start81=time.process_time() + start81
        a99=1
        b99=start81
        info99 = {
            'Iteracion': a99,
            'Hora' : b99,
        }
        with open('Data/Parte2_PostgresTest_1.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info99)
            log_box.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
            log_box.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)

    
    
    
def monitor(log_box):
    global elapsed_time
    global acc_time
    cut_time = 0
    back_online_time = 0
    cut_duration = 0
    cut_detector = False
    
    while RUNNING:
        if cut_detector:
            cut_duration = cut_time - back_online_time
            cut_duration = cut_duration.microseconds
            cut_duration = cut_duration * 10**(-3)
            acc_time+= cut_duration
            cut_detector = False

class GRAPH_LABEL():  
    def __init__(self):    
        self.frame = Toplevel()
        self.icon = Image.open('Graphs/Test1.png')
        self.icon = self.icon.resize((1920 - 50, 1080 - 100))
        self.img = ImageTk.PhotoImage(self.icon)
        self.graph_label = ttk.Label(self.frame, image = self.img)
        self.graph_label.image = self.img
        self.graph_label.pack()

class GRAPH_LABEL2():  
    def __init__(self):    
        self.frame = Toplevel()
        self.icon = Image.open('Graphs/Test2.png')
        self.icon = self.icon.resize((1920 - 50, 1080 - 100))
        self.img = ImageTk.PhotoImage(self.icon)
        self.graph_label = ttk.Label(self.frame, image = self.img)
        self.graph_label.image = self.img
        self.graph_label.pack()
    
class GRAPH_LABEL3():  
    def __init__(self):    
        self.frame = Toplevel()
        self.icon = Image.open('Graphs/Test3.png')
        self.icon = self.icon.resize((1920 - 50, 1080 - 100))
        self.img = ImageTk.PhotoImage(self.icon)
        self.graph_label = ttk.Label(self.frame, image = self.img)
        self.graph_label.image = self.img
        self.graph_label.pack()


def SHOW_GRAPH():

    data = pd.read_csv('Data/Parte2_MySQLTest_1.csv', index_col = None)
    dataq = pd.read_csv('Data/Parte2_MongoTest_1.csv', index_col = None)
    datay = pd.read_csv('Data/Parte2_SQLServerTest_1.csv', index_col = None)
    dataz = pd.read_csv('Data/Parte2_PostgresTest_1.csv', index_col = None)
    x = data['Iteracion']
    y = data['Hora']
    y1 = dataq['Hora']
    x1=dataq['Iteracion']
    y2 = datay['Hora']
    x2=datay['Iteracion']
    y3 = dataz['Hora']
    x3=dataz['Iteracion']

    numero_de_grupos = len(y)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras =0.25
    plt.figure(figsize = (20, 15))
    
    plt.bar(indice_barras, y, width=ancho_barras, label='Mongo DB')
    plt.bar(indice_barras + ancho_barras, y1, width=ancho_barras, label='MySQL')
    plt.bar(indice_barras + ancho_barras + ancho_barras, y2, width=ancho_barras, label='SQL Server')
    plt.bar(indice_barras + ancho_barras + ancho_barras+ ancho_barras,y3, width=ancho_barras, label='PostgreSQL')
    plt.legend(loc='best')

    ## Se colocan los indicadores en el eje x
    plt.xticks(indice_barras + ancho_barras, x)
    plt.ylabel('Tiempo Acumulado Transcurrido (s)')
    plt.xlabel('Iteracion')
    plt.title('Ordenar peliculas de Netflix')
    #plt.show()
    plt.savefig('Graphs/Parte2_Test1.png', bbox_inches='tight', dpi = 300)
    GRAPH_LABEL()

def SHOW_GRAPH2():

    data = pd.read_csv('Data/MySQLTest_2.csv', index_col = None)
    dataq = pd.read_csv('Data/MongoTest_2.csv', index_col = None)
    datay = pd.read_csv('Data/SQLServerTest_2.csv', index_col = None)
    dataz = pd.read_csv('Data/PostgresTest_2.csv', index_col = None)
    x = data['Iteracion']
    y = data['Hora']
    y1 = dataq['Hora']
    x1=dataq['Iteracion']
    y2 = datay['Hora']
    x2=datay['Iteracion']
    y3=dataz['Hora']
    x3=dataz['Iteracion']
    numero_de_grupos = len(y)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras =0.25
    plt.figure(figsize = (20, 15))
    
    plt.bar(indice_barras, y, width=ancho_barras, label='Mongo DB')
    plt.bar(indice_barras + ancho_barras, y1, width=ancho_barras, label='MySQL')
    plt.bar(indice_barras + ancho_barras + ancho_barras, y2, width=ancho_barras, label='SQL Server')
    plt.bar(indice_barras + ancho_barras + ancho_barras + ancho_barras, y3, width=ancho_barras, label='Postgres SQL')
    plt.legend(loc='best')

    ## Se colocan los indicadores en el eje x
    plt.xticks(indice_barras + ancho_barras, x)
    plt.ylabel('Tiempo Acumulado Transcurrido (s)')
    plt.xlabel('Iteracion')
    plt.title('Busqueda por texto')
    #plt.show()
    #plt.legend()
    plt.savefig('Graphs/Test2.png', bbox_inches='tight', dpi = 300)
    GRAPH_LABEL2()

def SHOW_GRAPH3():
    data = pd.read_csv('Data/MySQL_Test_3.csv', index_col = None)
    dataq = pd.read_csv('Data/Mongo_Test_3.csv', index_col = None)
    datay = pd.read_csv('Data/SQLServerTest_3.csv', index_col = None)
    dataz = pd.read_csv('Data/Postgres_Test_3.csv', index_col = None)
    x = data['Iteracion']
    y = data['Hora']
    y1 = dataq['Hora']
    x1=dataq['Iteracion']
    y2 = datay['Hora']
    x2=datay['Iteracion']
    y3 = dataz['Hora']
    x3=dataz['Iteracion']
    
    numero_de_grupos = len(y)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras =0.25
    plt.figure(figsize = (20, 15))
    
    plt.bar(indice_barras, y, width=ancho_barras, label='Mongo DB')
    plt.bar(indice_barras + ancho_barras, y1, width=ancho_barras, label='MySQL')
    plt.bar(indice_barras + ancho_barras + ancho_barras, y2, width=ancho_barras, label='SQL Server')
    plt.bar(indice_barras + ancho_barras + ancho_barras + ancho_barras , y3, width=ancho_barras, label='Postgres SQL')
    plt.legend(loc='best')

    ## Se colocan los indicadores en el eje x
    plt.xticks(indice_barras + ancho_barras, x)
    plt.ylabel('Tiempo Acumulado Transcurrido (s)')
    plt.xlabel('Iteracion')
    plt.title('Busqueda por texto contenido')
    #plt.show()
    #plt.legend()
    plt.savefig('Graphs/Test3.png', bbox_inches='tight', dpi = 300)
    GRAPH_LABEL3()


def THREAD_STOP(log_box):
    global RUNNING1
    RUNNING1=False

def THREAD_STOP2(log_box2):
    global RUNNING2
    RUNNING2=False

def THREAD_STOP3(log_box3):
    global RUNNING3
    RUNNING3=False

def CHECK_RESOURCES(label):
    global RESOURCES
    RESOURCES = True

    while RESOURCES:
    
        # % de utilizacion de cpu
        
        cpu = psutil.cpu_percent(1) # tasa de uso de CPU en un segundo, unidad
        cpu_per = '% .2f %%'% cpu # se convierte en un porcentaje, mantenga dos decimales
        
        # Utilizacion de memoria
        
        mem = psutil.virtual_memory()
        mem_per = '%.2f%%' % mem[2]
        mem_total = str(int(mem[0] / 1024 / 1024)) + 'MB'
        mem_used = str(int(mem[3] / 1024 / 1024)) + 'MB'
        
        # Utilizacion del disco principal
        
        c_info = psutil.disk_usage("C:")
        c_per = '%.2f%%' % c_info[3]
        
        ##################################
        # evita que el programa intente insertar texto en label cuando el objeto se destruya
        try:

            #label.configure(text = '\nPorcentaje de\nuso de CPU: ' + cpu_per + '\n\nPorcentaje de memoria\nutilizada: ' +  mem_per + '\n\nMemoria total: ' +  mem_total + '\n\nMemoria en uso: ' + mem_used + '\n\nEspacio usado en\nDisco: ' + c_per)
            #label.configure(text = 'CPU: ' + cpu_per + '  |  RAM: ' +  mem_used + '/' + mem_total + ' (' + mem_per + ')' + '  |  ALM: ' + c_per)
            label.configure(text = 'CPU: ' + cpu_per + '  |  RAM: ' +  mem_used + '/' + mem_total + ' (' + mem_per + ')')

        except: pass

        if not RESOURCES:

            return

        #time.sleep(0.3)
        
        #frame.after(1000, CHECK_RESOURCES, frame, label)
    

    
def EXIT_APP(root):
    global RESOURCES
    global RUNNING
    RUNNING = True
    
    if RUNNING:
        
        RUNNING = False
    
    root.destroy()
    
            
def GUI2(MySQL_db,mongoDB_collection,cnxn,conn):
    
    root = Tk()
    root.title("Connection monitor")
    
    root.geometry('1500x850')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='database-setting.png'))
    
    ########## Frame levels ##############

    ##################### GENERAL FRAMES #####################

    general_frame_1 = ttk.Frame(root)
    general_frame_1.pack(side = 'top')

    general_frame_2 = ttk.Frame(root)
    general_frame_2.pack(side = 'top')

    general_frame_3 = ttk.Frame(root)
    general_frame_3.pack(side = 'top')

    general_frame_4 = ttk.Frame(root)
    general_frame_4.pack(side = 'top')

    ##########################################################

    #################### GENERAL FRAME 1 SUB FRAMES ####################

    gf_1_column_1 = ttk.Frame(general_frame_1)
    gf_1_column_1.pack(side = 'left')

    gf_1_column_2 = ttk.Frame(general_frame_1)
    gf_1_column_2.pack(side = 'left', padx = 220)

    gf_1_column_3 = ttk.Frame(general_frame_1)
    gf_1_column_3.pack(side = 'left')

    ####################################################################

    ################### gf_1_column_1 SUB FRAMES #######################

    column_1_div_1 = ttk.Frame(gf_1_column_1)
    column_1_div_1.pack(side = 'top')

    column_1_div_2 = ttk.Frame(gf_1_column_1)
    column_1_div_2.pack(side = 'top')

    ################### gf_1_column_2 SUB FRAMES #######################

    column_2_div_1 = ttk.Frame(gf_1_column_2)
    column_2_div_1.pack(side = 'top')

    column_2_div_2 = ttk.Frame(gf_1_column_2)
    column_2_div_2.pack(side = 'top')

    ################### gf_1_column_3 SUB FRAMES #######################

    column_3_div_1 = ttk.Frame(gf_1_column_3)
    column_3_div_1.pack(side = 'top')

    column_3_div_2 = ttk.Frame(gf_1_column_3)
    column_3_div_2.pack(side = 'top')

    
    column_2_div_3 = ttk.Frame(gf_1_column_3)
    column_2_div_3.pack(side = 'top')

    ##############################################################

    ##################### column_1_div_2 DIVITION FOR BUTTONS #######################
    
    div_2_top_div_c1 = ttk.Frame(column_1_div_2)
    div_2_top_div_c1.pack(side = 'top')

    div_2_bottom_c1 = ttk.Frame(column_1_div_2)
    div_2_bottom_c1.pack(side = 'top')

    ##################### column_2_div_2 DIVITION FOR BUTTONS #######################
    
    div_2_top_div_c2 = ttk.Frame(column_2_div_2)
    div_2_top_div_c2.pack(side = 'top')

    div_2_bottom_c2 = ttk.Frame(column_2_div_2)
    div_2_bottom_c2.pack(side = 'top')

    ###############################################################################################################################################
    div_2_top_div_c3 = ttk.Frame(column_2_div_3)
    div_2_top_div_c3.pack(side = 'top')

    div_2_bottom_c3 = ttk.Frame(column_2_div_3)
    div_2_bottom_c3.pack(side = 'top')
    ###############################################################################################################################################

    '''##### Level 1 #####
    
    left_frame = ttk.Frame(root)
    left_frame.pack(side = 'left')
    
    right_frame = ttk.Frame(root)
    right_frame.pack(side = 'right')
    
    ##### Level 2 Left #####
    
    level2L_1 = ttk.Frame(left_frame)
    level2L_1.pack(side = 'top')
    level2L_12 = ttk.Frame(left_frame)
    level2L_12.pack(side = 'top')
    level2L_121 = ttk.Frame(left_frame)
    level2L_121.pack(side = 'top')
    level2L_13 = ttk.Frame(left_frame)
    level2L_13.pack(side = 'top')
    level2L_14 = ttk.Frame(left_frame)
    level2L_14.pack(side = 'top')
    
    level2L_2 = ttk.Frame(left_frame)
    level2L_2.pack(side = 'top')
    
    level2L_3 = ttk.Frame(left_frame)
    level2L_3.pack(side = 'top')
    
    ##### Level 2 Right #####
    
    level2R_1 = ttk.Frame(left_frame)
    level2R_1.pack(side = 'top')
    
    level2R_2 = ttk.Frame(left_frame)
    level2R_2.pack(side = 'top')
    level2R_2 = ttk.Frame(left_frame)
    level2R_2.pack(side = 'top')'''
    
    ################## Frame 1 ##########################
    value_list = ['ASC','DESC']
    value_list2 = ['Chile', 'Argentina', 'Alemania']
    value_list3 = ['nia', 'tan', 'lia']

    packet_loss_label_2 = ttk.Label(column_1_div_1, text = '\nComo desea ordenar las peliculas de Netflix.', font=("Calibri"), justify = 'center')
    packet_loss_label_2.pack(side = 'top')

    #duration_entrybox = ttk.Entry(column_1_div_1)
    #duration_entrybox.pack(side = 'top')

    values_shared_combobox = ttk.Combobox(column_1_div_1)
    values_shared_combobox.pack(side = 'top')

    values_shared_combobox['values'] = value_list
    values_shared_combobox.set(value_list[0])

    packet_loss_label_22 = ttk.Label(column_2_div_1,text = '\nSeleccione el país a buscar.', font=("Calibri"), justify = 'center')
    packet_loss_label_22.pack(side = 'top')

    ##duration_entrybox1 = ttk.Entry(column_2_div_1)
    ##duration_entrybox1.pack(side = 'top')

    values_shared1_combobox = ttk.Combobox(column_2_div_1)
    values_shared1_combobox.pack(side = 'top')

    values_shared1_combobox['values'] = value_list2
    values_shared1_combobox.set(value_list2[0])

    packet_loss_label_23 = ttk.Label( column_3_div_1,text = '\nSeleccione la palabra conteniada a buscar.', font=("Calibri"), justify = 'center')
    packet_loss_label_23.pack(side = 'top')

    #duration_entrybox2 = ttk.Entry(column_3_div_1)
    #duration_entrybox2.pack(side = 'top')

    values_shared2_combobox = ttk.Combobox(column_3_div_1)
    values_shared2_combobox.pack(side = 'top')

    values_shared2_combobox['values'] = value_list3
    values_shared2_combobox.set(value_list3[0])


    
    begin_button = ttk.Button(div_2_top_div_c1, text= 'Iniciar', command=lambda:(rand(values_shared_combobox),Test1(log_box,MySQL_db,mongoDB_collection,cnxn,conn)))
    begin_button.pack(side = 'left')

    begin_button1 = ttk.Button(div_2_top_div_c2, text= 'Iniciar', command=lambda:(rand1(values_shared1_combobox),Test2(log_box2,MySQL_db,mongoDB_collection,cnxn,conn)))
    begin_button1.pack(side = 'left')

    begin_button2 = ttk.Button(div_2_top_div_c3, text= 'Iniciar', command=lambda:(rand2(values_shared2_combobox),Test3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn)))
    begin_button2.pack(side = 'left')

    
    #label_2 = ttk.Label(level2L_1)
    #label_2.pack(side = 'left')

    

    
    stop_button = ttk.Button(div_2_top_div_c1, text= 'Detener', command=lambda:THREAD_STOP(log_box))
    stop_button.pack(side = 'left')

    #label_221 = ttk.Label(level2L_12)
    #label_221.pack(side = 'left')

    
    stop_button1 = ttk.Button(div_2_top_div_c2, text= 'Detener', command=lambda:THREAD_STOP2(log_box2))
    stop_button1.pack(side = 'left')

    
    stop_button2 = ttk.Button(div_2_top_div_c3, text= 'Detener', command=lambda:THREAD_STOP3(log_box3))
    stop_button2.pack(side = 'left')
    
    
    #label_3 = ttk.Label(level2L_1)
    #label_3.pack(side = 'left')
    
    graph_button = ttk.Button(div_2_bottom_c1, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH())
    graph_button.pack(side = 'left')
    
    label_4 = ttk.Label(div_2_bottom_c1)
    label_4.pack(side = 'left')

    graph_button1 = ttk.Button(div_2_bottom_c2, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH2())
    graph_button1.pack(side = 'left')
    
    label_44 = ttk.Label(div_2_bottom_c2)
    label_44.pack(side = 'left')

    graph_button2 = ttk.Button(div_2_bottom_c3, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH3())
    graph_button2.pack(side = 'left')
    
    label_45 = ttk.Label(div_2_bottom_c3)
    label_45.pack(side = 'left')
    
    #live_graph_button = ttk.Button(level2L_1, text= 'Mostrar Grafico en Vivo', command=lambda:GRAPH_THREAD())
    #live_graph_button.pack(side = 'left')
    
    #label_5 = ttk.Label(level2L_1)
    #label_5.pack(side = 'left')
    
    exit_button = ttk.Button(div_2_bottom_c1, text= 'Salir', command=lambda:EXIT_APP(root))
    exit_button.pack(side = 'left')
    
    #label_6 = ttk.Label(level2L_1)
    #label_6.pack(side = 'left')

    exit_button1 = ttk.Button(div_2_bottom_c2, text= 'Salir', command=lambda:EXIT_APP(root))
    exit_button1.pack(side = 'left')

    exit_button2 = ttk.Button(div_2_bottom_c3, text= 'Salir', command=lambda:EXIT_APP(root))
    exit_button2.pack(side = 'left')
    
    #label_66 = ttk.Label(div_2_bottom_c2)
    #label_66.pack(side = 'left')
    
    ################## Frame 2 ##################
    
    label_7 = ttk.Label(general_frame_2, text = '\nlog')
    label_7.pack(side = 'top')
    
    ################## Frame 3 ##################
    
    log_box = scrolledtext.ScrolledText(general_frame_3, wrap="word", height = 30, width = int(1920/45))
    log_box.pack(side = 'left')

    log_box2 = scrolledtext.ScrolledText(general_frame_3, wrap="word", height = 30, width = int(1920/45))
    log_box2.pack(side = 'left')

    log_box3 = scrolledtext.ScrolledText(general_frame_3, wrap="word", height = 30, width = int(1920/45))
    log_box3.pack(side = 'left')

    label_recursos = ttk.Label(general_frame_4, text = 'Recursos')
    label_recursos.pack(side = 'top', pady = 10)

    resources_thread = threading.Thread(name = 'Resources', target = CHECK_RESOURCES, daemon=True, args=(label_recursos, ))
    resources_thread.start()
    
    root.focus_force()
    root.protocol("WM_DELETE_WINDOW", False)  
    root.mainloop()
    
    root.mainloop()
    

if __name__ == '__main__':
    
    scan_interval = 1 # seconds
    
    ani = None
    
    elapsed_time = 0
    
    acc_time = 0
    
    RUNNING = True
    
    plt.style.use('fivethirtyeight')
    #plt.rcParams['animation.html'] = 'jshtml'
    
    #fieldnames = ['Fecha', 'Tiempo_Transcurrido', 'Ping', 'Tiempo_de_Fallo_Acumulado']  # agregar tiempo de corte
    fieldnames = ['Iteracion', 'Hora']
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames2 = ['Iteracion', 'Hora']



    #monitor() 
    
    