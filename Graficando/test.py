# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:46:05 2022

@author: Sebafu
"""

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
#from win32api import GetSystemMetrics
from PIL import ImageTk, Image

fieldnames = ['Iteracion', 'Hora']

#MySQL 로그인 정보
###################################
DB_IP = 'localhost'
DB_ID = "root"
DB_PW = "LS9lm10N11"
###################################
MySQL_db = connect(host=DB_IP, user=DB_ID, password=DB_PW, db='paises', charset='utf8mb4', cursorclass=cursors.DictCursor)


mongoDB_client = MongoClient()
#mongoDB 접속
mongoDB_client = MongoClient('localhost', 27017)
#mongoDB db객체 할당받기
mongoDB_db = mongoDB_client["dbpaises"]
#mongoDB collection객체 할당받기
mongoDB_collection = mongoDB_db["pais"]

f = open('random.txt', 'r')
random = []
for i in range(50):
	random.append(int(f.readline()))



def Mysql_start(logbox):
    global RUNNING
    RUNNING= True
    logbox.insert(tk.END, ' Iniciando...')
    t1= threading.Thread(name = 'ping', target = Mysql, daemon=False, args=(logbox,))
    t1.start()


    
    
    

def Mysql(log_box):
    print("Primer TEST busqueda de datos por indice numerico")
        # MySQL INT Type TEST
    start = time.process_time()
    cont=0
    with MySQL_db.cursor() as cursor:
        sql = "SELECT id_pais, Nombre  FROM pais WHERE id_pais= %s;"
        for num in random:
            if(not RUNNING):
                break            
            cursor.execute(sql, (num,))
            result = cursor.fetchall()
            a=int(num)
            b=(time.process_time() - start)    
            info = {
                'Iteracion': a,
                'Hora' : b
                }
            with open('Data/ping_data.csv', 'a', newline = '') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                csv_writer.writerow(info)
            log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box.see("end") 
            cut_duration = 0
            #elapsed_time+= scan_interval
            time.sleep(scan_interval)
    
def monitor(log_box):
    
    global elapsed_time
    global acc_time
    
    #delta = 0
    
    cut_time = 0
    back_online_time = 0
    
    cut_duration = 0
    cut_detector = False
    
    while RUNNING:
        
        #print(ping)
        
        if cut_detector:
            
            cut_duration = cut_time - back_online_time
            cut_duration = cut_duration.microseconds
            cut_duration = cut_duration * 10**(-3)
            acc_time+= cut_duration
            
            #print(cut_duration)
            
            cut_detector = False
        
       
        #packet_loss = result[6].strip()
        #packet_loss = packet_loss[1:3]
        #msLine = result[-1].strip()
    
        #total_ms = msLine[len(msLine) - 4: len(msLine) - 2]
            
        #if total_ms == 'os':
            
         #   cut_time = datetime.datetime.now()
            
          #  total_ms = 0
           # cut_detector = True
            
        #cut_duration = cut_duration.microseconds
        #cut_duration = cut_duration * 10**(-3)
        #acc_time+= cut_duration

        
        


class GRAPH_LABEL():
    
    def __init__(self):
        
        self.frame = Toplevel()
        
        self.icon = Image.open('Graphs/ping_graph.png')
        self.icon = self.icon.resize((1920 - 50, 1080 - 100))
        self.img = ImageTk.PhotoImage(self.icon)
        
        #self.img = ttk.PhotoImage(file = 'Graphs/test_graph.png')
        self.graph_label = ttk.Label(self.frame, image = self.img)
        self.graph_label.image = self.img
        self.graph_label.pack()
    

def SHOW_GRAPH():

    data = pd.read_csv('Data/ping_data.csv', index_col = None)
    
    #print(data)
    x = data['Iteracion']
    y = data['Hora']
    
    #print(x)
    #print(y)
    
    #print(' Tiempo total de cortes (ms): ', data['Tiempo_de_Fallo_Acumulado_(ms)'].iloc[-1], '\n Cantidad de cortes: ', (data['Ping_(ms)'].values == 0).sum(), '\n Tiempo total de monitoreo (s): ', data['Tiempo_Transcurrido_(s)'].iloc[-1])
    plt.figure(figsize = (50, 15))
    #plt.plot(x, y, label='download', color='r')
    #plt.scatter(x, y)
    
    plt.margins(0)
    plt.plot(x, y, linewidth = 0.5)
    
    plt.xticks(np.arange(0, max(x) + 1, 10.0))
    
    plt.yticks(np.arange(min(y) - 5, max(y) + 5, 5.0))
    
    plt.xlabel('Tiempo Transcurrido (s)')
    plt.ylabel('Ping (ms)')
    plt.title("Ping (www.google.com)")
    #plt.legend()
    plt.savefig('Graphs/ping_graph.png', bbox_inches='tight', dpi = 300)
    
    GRAPH_LABEL()

'''
def SHOW_LIVE_GRAPH():
    
    data = pd.read_csv('Data/ping_data.csv', index_col = None)
    
    x = data['Tiempo_Transcurrido_(s)']
    y = data['Ping_(ms)']
    
    plt.margins(0)
    
    plt.cla()
    #plt.figure(figsize = (50, 15))
    plt.plot(x, y, linewidth = 0.5)
    
    plt.xticks(np.arange(0, max(x) + 1, 10.0))
    plt.yticks(np.arange(min(y) - 5, max(y) + 5, 5.0))
    
    plt.xlabel('Tiempo Transcurrido (s)')
    plt.ylabel('Ping (ms)')
    plt.title("Ping (www.google.com)")
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
'''

def SHOW_LIVE_GRAPH(ax, right_frame, fig):
        
    data = pd.read_csv('Data/ping_data.csv', index_col = None)
    
    x = data['Iteracion']
    y = data['Ping_(ms)']
    
    ax.clear()
    ax.plot(x, y, linewidth = 0.5)
    
    plt.xticks(np.arange(0, max(x) + 1, 10.0))
    plt.yticks(np.arange(min(y) - 5, max(y) + 5, 5.0))
    
    plot = FigureCanvasTkAgg(fig, right_frame) 
    plot.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    plt.xlabel('Tiempo Transcurrido (s)')
    plt.ylabel('Ping (ms)')
    plt.title("Ping (www.google.com)")
    plt.tight_layout()
    



def INITIALIZE_LIVE_GRAPH():
    
    global ani
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    ani = FuncAnimation(fig, SHOW_LIVE_GRAPH, fargs=(ax),interval=1000)
    
    fig.show()

def THREAD_STOP(log_box):
    global RUNNING
    RUNNING=False

    
def GRAPH_THREAD():
    
    if RUNNING:
    
        t2 = threading.Thread(name = 'pinggraph', target = INITIALIZE_LIVE_GRAPH, daemon=False)
        
        t2.start()
    
def EXIT_APP(root):
    
    global RUNNING
    
    if RUNNING:
        
        RUNNING = False
    
    root.destroy()
    
            
def GUI():
    
    root = Tk()
    root.title("Connection monitor")
    #root.geometry('300x300')
    
    ########## Frame levels ##############
    
    ##### Level 1 #####
    
    left_frame = ttk.Frame(root)
    left_frame.pack(side = 'left')
    
    right_frame = ttk.Frame(root)
    right_frame.pack(side = 'right')
    
    ##### Level 2 Left #####
    
    level2L_1 = ttk.Frame(left_frame)
    level2L_1.pack(side = 'top')
    
    level2L_2 = ttk.Frame(left_frame)
    level2L_2.pack(side = 'top')
    
    level2L_3 = ttk.Frame(left_frame)
    level2L_3.pack(side = 'top')
    
    ##### Level 2 Right #####
    
    level2R_1 = ttk.Frame(left_frame)
    level2R_1.pack(side = 'top')
    
    level2R_2 = ttk.Frame(left_frame)
    level2R_2.pack(side = 'top')
    
    ################## Frame 1 ##########################
    
    label_1 = ttk.Label(level2L_1)
    label_1.pack(side = 'left')
    
    begin_button = ttk.Button(level2L_1, text= 'Iniciar', command=lambda:Mysql_start(log_box))
    begin_button.pack(side = 'left')
    
    label_2 = ttk.Label(level2L_1)
    label_2.pack(side = 'left')
    
    stop_button = ttk.Button(level2L_1, text= 'Detener', command=lambda:THREAD_STOP(log_box))
    stop_button.pack(side = 'left')
    
    label_3 = ttk.Label(level2L_1)
    label_3.pack(side = 'left')
    
    graph_button = ttk.Button(level2L_1, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH())
    graph_button.pack(side = 'left')
    
    label_4 = ttk.Label(level2L_1)
    label_4.pack(side = 'left')
    
    #live_graph_button = ttk.Button(level2L_1, text= 'Mostrar Grafico en Vivo', command=lambda:GRAPH_THREAD())
    #live_graph_button.pack(side = 'left')
    
    label_5 = ttk.Label(level2L_1)
    label_5.pack(side = 'left')
    
    exit_button = ttk.Button(level2L_1, text= 'Salir', command=lambda:EXIT_APP(root))
    exit_button.pack(side = 'left')
    
    label_6 = ttk.Label(level2L_1)
    label_6.pack(side = 'left')
    
    ################## Frame 2 ##################
    
    label_7 = ttk.Label(level2L_2, text = 'log')
    label_7.pack(side = 'top')
    
    ################## Frame 3 ##################
    
    log_box = scrolledtext.ScrolledText(level2L_3, wrap="word", height = 1920, width = 1080)
    log_box.pack(side = 'top')
    
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
    
    if not os.path.exists('Data/ping_data.csv'):
    
        with open('Data/ping_data.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    
    #monitor() 
    GUI()
 