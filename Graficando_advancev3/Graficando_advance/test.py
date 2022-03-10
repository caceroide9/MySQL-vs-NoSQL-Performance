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



def rand(entry_box):
    global random
    random=int(entry_box.get())
      

def rand1(entry_box2):
    global topic_str
    topic_str=entry_box2.get()

def rand2(entry_box3):
    global topic
    topic=entry_box3.get()
    print(topic)

def Test3(log_box3,MySQL_db,mongoDB_collection):
    global RUNNING
    RUNNING= True
    log_box3.insert(tk.END, ' Iniciando...')
    t3= threading.Thread(name = 'ping', target = TESTT3, daemon=False, args=(log_box3,MySQL_db,mongoDB_collection))
    t3.start()


def Test1(logbox,MySQL_db,mongoDB_collection):
    global RUNNING
    RUNNING= True
    logbox.insert(tk.END, ' Iniciando...')
    t1= threading.Thread(name = 'ping', target = TESTT1, daemon=False, args=(logbox,MySQL_db,mongoDB_collection))
    t1.start()
   

def Test2(log_box2,MySQL_db,mongoDB_collection):
    global RUNNING
    RUNNING= True
    log_box2.insert(tk.END, ' Iniciando...')
    t2= threading.Thread(name = 'ping', target = TESTT2, daemon=False, args=(log_box2,MySQL_db,mongoDB_collection))
    t2.start()

def TESTT3(log_box3,MySQL_db,mongoDB_collection):
    
    global start3
    start3 = time.process_time()
    log_box3.insert(tk.END, ' TEST 2 MongoDB...')

    start = time.time()
    
    for topic_one in topic:
        result = mongoDB_collection.find({"Nombre": {'$regex': topic}})
    a=result
    b= time.process_time() - start3
    info1 = {
        'Iteracion': a,
        'Hora' : b,
        }
    with open('Data/MongoTest3.csv', 'a', newline = '') as csv_file:
        fieldnames2 = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
        csv_writer.writerow(info1)
        log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box3.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)

    global start4
    log_box3.insert(tk.END, ' \nTEST 2 MySQL...')
    start4 = time.process_time()
    with MySQL_db.cursor() as cursor:
        sql = "SELECT count(*) AS cnt FROM pais WHERE Nombre LIKE %s"
        for topic_one in topic:
            temp_topic = '%' + topic_one + '%'
            cursor.execute(sql, (temp_topic,))
            result = cursor.fetchone()
    a=topic_one
    b=time.process_time() - start4
    info = {
        'Iteracion': a,
        'Hora' : b,}
    with open('Data/MySQLTEST3.csv', 'a', newline = '') as csv_file:
        fieldnames2 = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames2)
        csv_writer.writerow(info)
        log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box3.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)



	
		
def TESTT2(log_box2,MySQL_db,mongoDB_collection):
    global start3
    cont =1
    cont1 =1
    start3 = time.process_time()
    log_box2.insert(tk.END, ' TEST 2 MongoDB...')
    result = list(mongoDB_collection.find({'Nombre': topic_str}))
    a=cont
    b= time.process_time() - start3
    info1 = {
        'Iteracion': a,
        'Hora' : b,
        }
    with open('Data/MongoTest2.csv', 'a', newline = '') as csv_file:
        fieldnames1 = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
        csv_writer.writerow(info1)
        log_box2.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box2.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)

    global start4
    log_box2.insert(tk.END, ' \nTEST 2 MySQL...')
    start4 = time.process_time()
    with MySQL_db.cursor() as cursor:
        sql = "SELECT Nombre FROM pais WHERE Nombre=%s;"
        cursor.execute(sql, (topic_str,))
        result = cursor.fetchall()
    a=cont1
    b=time.process_time() - start4
    info = {
        'Iteracion': a,
        'Hora' : b,}
    with open('Data/MySQLTEST2.csv', 'a', newline = '') as csv_file:
        fieldnames1 = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
        csv_writer.writerow(info)
        log_box2.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box2.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)
    
def TESTT1(log_box,MySQL_db,mongoDB_collection):
    global start
    log_box.insert(tk.END, ' TEST 1 MongoDB...')
    start = time.process_time()
    for num in range(random):
        if(not RUNNING):
                break
        result = list(mongoDB_collection.find({'id_pais': num}))
        a=int(num)
        b= time.process_time() - start
        info1 = {
                'Iteracion': a,
                 'Hora' : b,
            }
        with open('Data/MongoTest1.csv', 'a', newline = '') as csv_file:
            fieldnames1 = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writerow(info1)
            log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
     
    global start1
    log_box.insert(tk.END, ' \nTEST 1 MySQL...')
    start1 = time.process_time()
    with MySQL_db.cursor() as cursor:
        sql = "SELECT id_pais, Nombre  FROM pais WHERE id_pais= %s;"
        for num in range (random):    
            if(not RUNNING):
                break 
            cursor.execute(sql, (num,))
            result = cursor.fetchall()
            a=int(num)
            b=time.process_time()- start1
            info = {
                'Iteracion': a,
                 'Hora' : b,
            }
            with open('Data/MySQLTes1.csv', 'a', newline = '') as csv_file:
                fieldnames = ['Iteracion', 'Hora']
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                csv_writer.writerow(info)
                log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
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
        self.icon = Image.open('Graphs/MySQLTes1.png')
        self.icon = self.icon.resize((1920 - 50, 1080 - 100))
        self.img = ImageTk.PhotoImage(self.icon)
        self.graph_label = ttk.Label(self.frame, image = self.img)
        self.graph_label.image = self.img
        self.graph_label.pack()
    

def SHOW_GRAPH():

    data = pd.read_csv('Data/MySQLTes1.csv', index_col = None)
    dataq = pd.read_csv('Data/MongoTest1.csv', index_col = None)
    x = data['Iteracion']
    y = data['Hora']
    y1 = dataq['Hora']
    plt.figure(figsize = (20, 15))
    plt.margins(0)
    plt.plot(x, y,y1, linewidth = 0.5)
    plt.xticks(np.arange(0, max(x) + 1, 5.0))
    plt.yticks(np.arange(min(y) - 5, max(y) + 5, 0.10))
    plt.xlabel('Tiempo Transcurrido (s)')
    plt.ylabel('Ping (ms)')
    plt.title("Ping (www.google.com)")
    #plt.legend()
    plt.savefig('Graphs/MySQLTes1.png', bbox_inches='tight', dpi = 300)
    GRAPH_LABEL()


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
    
            
def GUI(MySQL_db,mongoDB_collection):
    
    root = Tk()
    root.title("Connection monitor")
    
    #root.geometry('300x300')
    
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

    packet_loss_label_2 = ttk.Label(column_1_div_1, text = '\nIngrese datos a buscar.', font=("Calibri"), justify = 'center')
    packet_loss_label_2.pack(side = 'top')

    duration_entrybox = ttk.Entry(column_1_div_1)
    duration_entrybox.pack(side = 'top')

    packet_loss_label_22 = ttk.Label(column_2_div_1,text = '\nIngrese cantidad\nde paquetesss.', font=("Calibri"), justify = 'center')
    packet_loss_label_22.pack(side = 'top')

    duration_entrybox1 = ttk.Entry(column_2_div_1)
    duration_entrybox1.pack(side = 'top')

    packet_loss_label_23 = ttk.Label( column_3_div_1,text = '\nIngrese cantidad\nde paquetesss.', font=("Calibri"), justify = 'center')
    packet_loss_label_23.pack(side = 'top')

    duration_entrybox2 = ttk.Entry(column_3_div_1)
    duration_entrybox2.pack(side = 'top')


    
    begin_button = ttk.Button(div_2_top_div_c1, text= 'Iniciar', command=lambda:(rand(duration_entrybox),Test1(log_box,MySQL_db,mongoDB_collection)))
    begin_button.pack(side = 'left')

    begin_button1 = ttk.Button(div_2_top_div_c2, text= 'Iniciar1', command=lambda:(rand1(duration_entrybox1),Test2(log_box2,MySQL_db,mongoDB_collection)))
    begin_button1.pack(side = 'left')

    begin_button2 = ttk.Button(column_3_div_1, text= 'Iniciar2', command=lambda:(rand2(duration_entrybox2),Test3(log_box3,MySQL_db,mongoDB_collection)))
    begin_button2.pack(side = 'top')

    
    #label_2 = ttk.Label(level2L_1)
    #label_2.pack(side = 'left')

    

    
    stop_button = ttk.Button(div_2_top_div_c1, text= 'Detener', command=lambda:THREAD_STOP(log_box))
    stop_button.pack(side = 'left')

    #label_221 = ttk.Label(level2L_12)
    #label_221.pack(side = 'left')

    
    stop_button1 = ttk.Button(div_2_top_div_c2, text= 'Detener', command=lambda:THREAD_STOP(log_box2))
    stop_button1.pack(side = 'left')

    

    
    
    #label_3 = ttk.Label(level2L_1)
    #label_3.pack(side = 'left')
    
    graph_button = ttk.Button(div_2_bottom_c1, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH())
    graph_button.pack(side = 'left')
    
    label_4 = ttk.Label(div_2_bottom_c1)
    label_4.pack(side = 'left')

    graph_button1 = ttk.Button(div_2_bottom_c2, text= 'Mostrar Grafico', command=lambda:SHOW_GRAPH())
    graph_button1.pack(side = 'left')
    
    label_44 = ttk.Label(div_2_bottom_c2)
    label_44.pack(side = 'left')
    
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
    
    #label_66 = ttk.Label(div_2_bottom_c2)
    #label_66.pack(side = 'left')
    
    ################## Frame 2 ##################
    
    label_7 = ttk.Label(general_frame_2, text = 'log')
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

    
    if not os.path.exists('Data/MySQLTes1.csv'):
    
        with open('Data/MySQLTes1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()

    if not os.path.exists('Data/MongoTest1.csv'):
    
        with open('Data/MongoTest1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    
    #monitor() 
    