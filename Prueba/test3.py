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



def rand(entry_box):
    global random
    random=int(entry_box.get())
      

def rand1(entry_box2):
    global topic_str
    topic_str=entry_box2.get()

def rand2(entry_box3):
    global topic
    topic=entry_box3.get()
    

def Test3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3):
    global RUNNING3
    RUNNING3= True
    log_box3.insert(tk.END, ' Iniciando...')
    t3= threading.Thread(name = 'ping', target = TESTT3, daemon=False, args=(log_box3,MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3))
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

def TESTT3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3):
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames = ['Iteracion', 'Hora']
    if not os.path.exists('Data/Parte_3_MySQL_Test_3.csv'):
    
        with open('Data/Parte_3_MySQL_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte_3_MySQL_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/Parte_3_Mongo_Test_3.csv'):
    
        with open('Data/Parte_3_Mongo_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_Mongo_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/Parte_3_SQLServerTest_3.csv'):
    
        with open('Data/Parte_3_SQLServerTest_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_SQLServerTest_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()


    if not os.path.exists('Data/Parte_3_Postgres_Test_3.csv'):
    
        with open('Data/Parte_3_Postgres_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte_3_Postgres_Test_3.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    
    
    
    global start69
    start69=0

    log_box3.insert(tk.END, ' TEST 3 MongoDB...')
    if(topic=='Region'):
        mongoDB_collection_3.drop()
        start69=time.process_time() + start69
        a=1
        b= start69
        info1 = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_Mongo_Test_3.csv', 'a', newline = '') as csv_file:
          csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
          csv_writer.writerow(info1)
          log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
          log_box3.see("end") 
          cut_duration = 0
          scan_interval = 1
          time.sleep(scan_interval)
        mylist3=[{
  "id": 1,
  "nombre": "Tarapacá",
  "ISO_3166_2_CL": "CL-TA"
},{
  "id": 2,
  "nombre": "Antofagasta",
  "ISO_3166_2_CL": "CL-AN"
},{
  "id": 3,
  "nombre": "Atacama",
  "ISO_3166_2_CL": "CL-AT"
},{
  "id": 4,
  "nombre": "Coquimbo",
  "ISO_3166_2_CL": "CL-CO"
},{
  "id": 5,
  "nombre": "Valparaíso",
  "ISO_3166_2_CL": "CL-VS"
},{
  "id": 6,
  "nombre": "Región del Libertador Gral. Bernardo O’Higgins",
  "ISO_3166_2_CL": "CL-LI"
},{
  "id": 7,
  "nombre": "Región del Maule",
  "ISO_3166_2_CL": "CL-ML"
},{
  "id": 8,
  "nombre": "Región del Biobío",
  "ISO_3166_2_CL": "CL-BI"
},{
  "id": 9,
  "nombre": "Región de la Araucanía",
  "ISO_3166_2_CL": "CL-AR"
},{
  "id": 10,
  "nombre": "Región de Los Lagos",
  "ISO_3166_2_CL": "CL-LL"
},{
  "id": 11,
  "nombre": "Región Aisén del Gral. Carlos Ibáñez del Campo",
  "ISO_3166_2_CL": "CL-AI"
},{
  "id": 12,
  "nombre": "Región de Magallanes y de la Antártica Chilena",
  "ISO_3166_2_CL": "CL-MA"
},{
  "id": 13,
  "nombre": "Región Metropolitana de Santiago",
  "ISO_3166_2_CL": "CL-RM"
},{
  "id": 14,
  "nombre": "Región de Los Ríos",
  "ISO_3166_2_CL": "CL-LR"
},{
  "id": 15,
  "nombre": "Arica y Parinacota",
  "ISO_3166_2_CL": "CL-AP"
}]
        list3=[]
        for i in range(len(mylist3)):
            list3.append(mylist3[i])  
        mongoDB_collection_3.insert_many(list3)
        

    elif(topic=='Comuna'):
        mongoDB_collection.drop()
        start69=time.process_time() + start69
        a=1
        b= start69
        info1 = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_Mongo_Test_3.csv', 'a', newline = '') as csv_file:
          csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
          csv_writer.writerow(info1)
          log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
          log_box3.see("end") 
          cut_duration = 0
          scan_interval = 1
          time.sleep(scan_interval)
        mylist1 = [{
  "id": 1,
  "nombre": "Iquique",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3e')"
},{
  "id": 2,
  "nombre": "Alto Hospicio",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3e')"
},{
  "id": 3,
  "nombre": "Pozo Almonte",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3f')"
},{
  "id": 4,
  "nombre": "Cami�a",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3f')"
},{
  "id": 5,
  "nombre": "Colchane",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3f')"
},{
  "id": 6,
  "nombre": "Huara",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3f')"
},{
  "id": 7,
  "nombre": "Pica",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3f')"
},{
  "id": 8,
  "nombre": "Antofagasta",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb40')"
},{
  "id": 9,
  "nombre": "Mejillones",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb40')"
},{
  "id": 10,
  "nombre": "Sierra Gorda",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb40')"
},{
  "id": 11,
  "nombre": "Taltal",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb40')"
},{
  "id": 12,
  "nombre": "Calama",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb41')"
},{
  "id": 13,
  "nombre": "Ollag�e",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb41')"
},{
  "id": 14,
  "nombre": "San Pedro de Atacama",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb41')"
},{
  "id": 15,
  "nombre": "Tocopilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb42')"
},{
  "id": 16,
  "nombre": "Mar��a Elena",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb42')"
},{
  "id": 17,
  "nombre": "Copiap�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb43')"
},{
  "id": 18,
  "nombre": "Caldera",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb43')"
},{
  "id": 19,
  "nombre": "Tierra Amarilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb43')"
},{
  "id": 20,
  "nombre": "Cha�aral",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb44')"
},{
  "id": 21,
  "nombre": "Diego de Almagro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb44')"
},{
  "id": 22,
  "nombre": "Vallenar",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb45')"
},{
  "id": 23,
  "nombre": "Alto del Carmen",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb45')"
},{
  "id": 24,
  "nombre": "Freirina",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb45')"
},{
  "id": 25,
  "nombre": "Huasco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb45')"
},{
  "id": 26,
  "nombre": "La Serena",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 27,
  "nombre": "Coquimbo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 28,
  "nombre": "Andacollo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 29,
  "nombre": "La Higuera",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 30,
  "nombre": "Paihuano",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 31,
  "nombre": "Vicu�a",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb46')"
},{
  "id": 32,
  "nombre": "Illapel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb47')"
},{
  "id": 33,
  "nombre": "Canela",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb47')"
},{
  "id": 34,
  "nombre": "Los Vilos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb47')"
},{
  "id": 35,
  "nombre": "Salamanca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb47')"
},{
  "id": 36,
  "nombre": "Ovalle",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb48')"
},{
  "id": 37,
  "nombre": "Combarbal�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb48')"
},{
  "id": 38,
  "nombre": "Monte Patria",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb48')"
},{
  "id": 39,
  "nombre": "Punitaqui",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb48')"
},{
  "id": 40,
  "nombre": "R�o Hurtado",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb48')"
},{
  "id": 41,
  "nombre": "Valpara�so",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 42,
  "nombre": "Casablanca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 43,
  "nombre": "Conc�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 44,
  "nombre": "Juan Fern�ndez",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 45,
  "nombre": "Puchuncav�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 46,
  "nombre": "Quintero",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 47,
  "nombre": "Vi�a del Mar",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb49')"
},{
  "id": 48,
  "nombre": "Isla de Pascua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4a')"
},{
  "id": 49,
  "nombre": "Los Andes",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4b')"
},{
  "id": 50,
  "nombre": "Calle Larga",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4b')"
},{
  "id": 51,
  "nombre": "Rinconada",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4b')"
},{
  "id": 52,
  "nombre": "San Esteban",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4b')"
},{
  "id": 53,
  "nombre": "La Ligua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4c')"
},{
  "id": 54,
  "nombre": "Cabildo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4c')"
},{
  "id": 55,
  "nombre": "Papudo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4c')"
},{
  "id": 56,
  "nombre": "Petorca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4c')"
},{
  "id": 57,
  "nombre": "Zapallar",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4c')"
},{
  "id": 58,
  "nombre": "Quillota",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4d')"
},{
  "id": 59,
  "nombre": "La Calera",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4d')"
},{
  "id": 60,
  "nombre": "Hijuelas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4d')"
},{
  "id": 61,
  "nombre": "La Cruz",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4d')"
},{
  "id": 62,
  "nombre": "Nogales",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4d')"
},{
  "id": 63,
  "nombre": "San Antonio",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 64,
  "nombre": "Algarrobo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 65,
  "nombre": "Cartagena",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 66,
  "nombre": "El Quisco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 67,
  "nombre": "El Tabo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 68,
  "nombre": "Santo Domingo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4e')"
},{
  "id": 69,
  "nombre": "San Felipe",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 70,
  "nombre": "Catemu",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 71,
  "nombre": "Llay Llay",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 72,
  "nombre": "Panquehue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 73,
  "nombre": "Putaendo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 74,
  "nombre": "Santa Mar�a",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb4f')"
},{
  "id": 75,
  "nombre": "Quilpu�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb50')"
},{
  "id": 76,
  "nombre": "Limache",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb50')"
},{
  "id": 77,
  "nombre": "Olmu�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb50')"
},{
  "id": 78,
  "nombre": "Villa Alemana",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb50')"
},{
  "id": 79,
  "nombre": "Rancagua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 80,
  "nombre": "Codegua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 81,
  "nombre": "Coinco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 82,
  "nombre": "Coltauco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 83,
  "nombre": "Do�ihue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 84,
  "nombre": "Graneros",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 85,
  "nombre": "Las Cabras",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 86,
  "nombre": "Machal�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 87,
  "nombre": "Malloa",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 88,
  "nombre": "Mostazal",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 89,
  "nombre": "Olivar",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 90,
  "nombre": "Peumo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 91,
  "nombre": "Pichidegua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 92,
  "nombre": "Quinta de Tilcoco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 93,
  "nombre": "Rengo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 94,
  "nombre": "Requ�noa",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 95,
  "nombre": "San Vicente",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb51')"
},{
  "id": 96,
  "nombre": "Pichilemu",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 97,
  "nombre": "La Estrella",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 98,
  "nombre": "Litueche",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 99,
  "nombre": "Marchihue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 100,
  "nombre": "Navidad",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 101,
  "nombre": "Paredones",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb52')"
},{
  "id": 102,
  "nombre": "San Fernando",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 103,
  "nombre": "Ch�pica",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 104,
  "nombre": "Chimbarongo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 105,
  "nombre": "Lolol",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 106,
  "nombre": "Nancagua",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 107,
  "nombre": "Palmilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 108,
  "nombre": "Peralillo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 109,
  "nombre": "Placilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 110,
  "nombre": "Pumanque",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 111,
  "nombre": "Santa Cruz",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb53')"
},{
  "id": 112,
  "nombre": "Talca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 113,
  "nombre": "Constituci�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 114,
  "nombre": "Curepto",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 115,
  "nombre": "Empedrado",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 116,
  "nombre": "Maule",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 117,
  "nombre": "Pelarco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 118,
  "nombre": "Pencahue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 119,
  "nombre": "R�o Claro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 120,
  "nombre": "San Clemente",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 121,
  "nombre": "San Rafael",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb54')"
},{
  "id": 122,
  "nombre": "Cauquenes",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb55')"
},{
  "id": 123,
  "nombre": "Chanco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb55')"
},{
  "id": 124,
  "nombre": "Pelluhue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb55')"
},{
  "id": 125,
  "nombre": "Curic�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 126,
  "nombre": "Huala��",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 127,
  "nombre": "Licant�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 128,
  "nombre": "Molina",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 129,
  "nombre": "Rauco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 130,
  "nombre": "Romeral",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 131,
  "nombre": "Sagrada Familia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 132,
  "nombre": "Teno",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 133,
  "nombre": "Vichuqu�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb56')"
},{
  "id": 134,
  "nombre": "Linares",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 135,
  "nombre": "Colb�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 136,
  "nombre": "Longav�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 137,
  "nombre": "Parral",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 138,
  "nombre": "Retiro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 139,
  "nombre": "San Javier",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 140,
  "nombre": "Villa Alegre",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 141,
  "nombre": "Yerbas Buenas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb57')"
},{
  "id": 142,
  "nombre": "Concepci�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 143,
  "nombre": "Coronel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 144,
  "nombre": "Chiguayante",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 145,
  "nombre": "Florida",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 146,
  "nombre": "Hualqui",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 147,
  "nombre": "Lota",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 148,
  "nombre": "Penco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 149,
  "nombre": "San Pedro de la Paz",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 150,
  "nombre": "Santa Juana",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 151,
  "nombre": "Talcahuano",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 152,
  "nombre": "Tom�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 153,
  "nombre": "Hualp�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb58')"
},{
  "id": 154,
  "nombre": "Lebu",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 155,
  "nombre": "Arauco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 156,
  "nombre": "Ca�ete",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 157,
  "nombre": "Contulmo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 158,
  "nombre": "Curanilahue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 159,
  "nombre": "Los �lamos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 160,
  "nombre": "Tir�a",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb59')"
},{
  "id": 161,
  "nombre": "Los �ngeles",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 162,
  "nombre": "Antuco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 163,
  "nombre": "Cabrero",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 164,
  "nombre": "Laja",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 165,
  "nombre": "Mulch�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 166,
  "nombre": "Nacimiento",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 167,
  "nombre": "Negrete",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 168,
  "nombre": "Quilaco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 169,
  "nombre": "Quilleco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 170,
  "nombre": "San Rosendo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 171,
  "nombre": "Santa B�rbara",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 172,
  "nombre": "Tucapel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 173,
  "nombre": "Yumbel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 174,
  "nombre": "Alto Biob�o",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5a')"
},{
  "id": 175,
  "nombre": "Chill�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 176,
  "nombre": "Bulnes",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 177,
  "nombre": "Cobquecura",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 178,
  "nombre": "Coelemu",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 179,
  "nombre": "Coihueco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 180,
  "nombre": "Chill�n Viejo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 181,
  "nombre": "El Carmen",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 182,
  "nombre": "Ninhue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 183,
  "nombre": "�iqu�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 184,
  "nombre": "Pemuco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 185,
  "nombre": "Pinto",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 186,
  "nombre": "Portezuelo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 187,
  "nombre": "Quill�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 188,
  "nombre": "Quirihue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 189,
  "nombre": "R�nquil",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 190,
  "nombre": "San Carlos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 191,
  "nombre": "San Fabi�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 192,
  "nombre": "San Ignacio",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 193,
  "nombre": "San Nicol�s",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 194,
  "nombre": "Treguaco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 195,
  "nombre": "Yungay",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5b')"
},{
  "id": 196,
  "nombre": "Temuco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 197,
  "nombre": "Carahue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 198,
  "nombre": "Cunco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 199,
  "nombre": "Curarrehue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 200,
  "nombre": "Freire",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 201,
  "nombre": "Galvarino",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 202,
  "nombre": "Gorbea",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 203,
  "nombre": "Lautaro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 204,
  "nombre": "Loncoche",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 205,
  "nombre": "Melipeuco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 206,
  "nombre": "Nueva Imperial",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 207,
  "nombre": "Padre las Casas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 208,
  "nombre": "Perquenco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 209,
  "nombre": "Pitrufqu�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 210,
  "nombre": "Puc�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 211,
  "nombre": "Saavedra",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 212,
  "nombre": "Teodoro Schmidt",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 213,
  "nombre": "Tolt�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 214,
  "nombre": "Vilc�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 215,
  "nombre": "Villarrica",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 216,
  "nombre": "Cholchol",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5c')"
},{
  "id": 217,
  "nombre": "Angol",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 218,
  "nombre": "Collipulli",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 219,
  "nombre": "Curacaut�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 220,
  "nombre": "Ercilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 221,
  "nombre": "Lonquimay",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 222,
  "nombre": "Los Sauces",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 223,
  "nombre": "Lumaco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 224,
  "nombre": "Pur�nn",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 225,
  "nombre": "Renaico",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 226,
  "nombre": "Traigu�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 227,
  "nombre": "Victoria",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5d')"
},{
  "id": 228,
  "nombre": "Puerto Montt",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 229,
  "nombre": "Calbuco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 230,
  "nombre": "Cocham�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 231,
  "nombre": "Fresia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 232,
  "nombre": "Frutillar",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 233,
  "nombre": "Los Muermos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 234,
  "nombre": "Llanquihue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 235,
  "nombre": "Maull�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 236,
  "nombre": "Puerto Varas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb60')"
},{
  "id": 237,
  "nombre": "Castro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 238,
  "nombre": "Ancud",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 239,
  "nombre": "Chonchi",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 240,
  "nombre": "Curaco de V�lez",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 241,
  "nombre": "Dalcahue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 242,
  "nombre": "Puqueld�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 243,
  "nombre": "Queil�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 244,
  "nombre": "Quell�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 245,
  "nombre": "Quemchi",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 246,
  "nombre": "Quinchao",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb61')"
},{
  "id": 247,
  "nombre": "Osorno",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 248,
  "nombre": "Puerto Octay",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 249,
  "nombre": "Purranque",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 250,
  "nombre": "Puyehue",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 251,
  "nombre": "R�o Negro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 252,
  "nombre": "San Juan de la Costa",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 253,
  "nombre": "San Pablo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb62')"
},{
  "id": 254,
  "nombre": "Chait�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb63')"
},{
  "id": 255,
  "nombre": "Futaleuf�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb63')"
},{
  "id": 256,
  "nombre": "Hualaihu�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb63')"
},{
  "id": 257,
  "nombre": "Palena",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb63')"
},{
  "id": 258,
  "nombre": "Coyhaique",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb64')"
},{
  "id": 259,
  "nombre": "Lago Verde",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb64')"
},{
  "id": 260,
  "nombre": "Ays�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb65')"
},{
  "id": 261,
  "nombre": "Cisnes",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb65')"
},{
  "id": 262,
  "nombre": "Guaitecas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb65')"
},{
  "id": 263,
  "nombre": "Cochrane",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb66')"
},{
  "id": 264,
  "nombre": "O'Higgins",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb66')"
},{
  "id": 265,
  "nombre": "Tortel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb66')"
},{
  "id": 266,
  "nombre": "Chile Chico",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb67')"
},{
  "id": 267,
  "nombre": "R�o Ib��ez",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb67')"
},{
  "id": 268,
  "nombre": "Punta Arenas",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb68')"
},{
  "id": 269,
  "nombre": "Laguna Blanca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb68')"
},{
  "id": 270,
  "nombre": "R��o Verde",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb68')"
},{
  "id": 271,
  "nombre": "San Gregorio",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb68')"
},{
  "id": 272,
  "nombre": "Cabo de Hornos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb69')"
},{
  "id": 273,
  "nombre": "Ant�rtica",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb69')"
},{
  "id": 274,
  "nombre": "Porvenir",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6a')"
},{
  "id": 275,
  "nombre": "Primavera",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6a')"
},{
  "id": 276,
  "nombre": "Timaukel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6a')"
},{
  "id": 277,
  "nombre": "Natales",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6b')"
},{
  "id": 278,
  "nombre": "Torres del Paine",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6b')"
},{
  "id": 279,
  "nombre": "Santiago",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 280,
  "nombre": "Cerrillos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 281,
  "nombre": "Cerro Navia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 282,
  "nombre": "Conchal�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 283,
  "nombre": "El Bosque",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 284,
  "nombre": "Estaci�n Central",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 285,
  "nombre": "Huechuraba",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 286,
  "nombre": "Independencia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 287,
  "nombre": "La Cisterna",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 288,
  "nombre": "La Florida",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 289,
  "nombre": "La Granja",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 290,
  "nombre": "La Pintana",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 291,
  "nombre": "La Reina",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 292,
  "nombre": "Las Condes",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 293,
  "nombre": "Lo Barnechea",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 294,
  "nombre": "Lo Espejo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 295,
  "nombre": "Lo Prado",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 296,
  "nombre": "Macul",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 297,
  "nombre": "Maip�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 298,
  "nombre": "�u�oa",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 299,
  "nombre": "Pedro Aguirre Cerda",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 300,
  "nombre": "Pe�alol�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 301,
  "nombre": "Providencia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 302,
  "nombre": "Pudahuel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 303,
  "nombre": "Quilicura",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 304,
  "nombre": "Quinta Normal",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 305,
  "nombre": "Recoleta",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 306,
  "nombre": "Renca",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 307,
  "nombre": "San Joaqu�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 308,
  "nombre": "San Miguel",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 309,
  "nombre": "San Ram�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 310,
  "nombre": "Vitacura",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6c')"
},{
  "id": 311,
  "nombre": "Puente Alto",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6d')"
},{
  "id": 312,
  "nombre": "Pirque",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6d')"
},{
  "id": 313,
  "nombre": "San Jos� de Maipo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6d')"
},{
  "id": 314,
  "nombre": "Colina",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6e')"
},{
  "id": 315,
  "nombre": "Lampa",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6e')"
},{
  "id": 316,
  "nombre": "Tiltil",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6e')"
},{
  "id": 317,
  "nombre": "San Bernardo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6f')"
},{
  "id": 318,
  "nombre": "Buin",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6f')"
},{
  "id": 319,
  "nombre": "Calera de Tango",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6f')"
},{
  "id": 320,
  "nombre": "Paine",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb6f')"
},{
  "id": 321,
  "nombre": "Melipilla",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb70')"
},{
  "id": 322,
  "nombre": "Alhu�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb70')"
},{
  "id": 323,
  "nombre": "Curacav�",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb70')"
},{
  "id": 324,
  "nombre": "Mar�a Pinto",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb70')"
},{
  "id": 325,
  "nombre": "San Pedro",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb70')"
},{
  "id": 326,
  "nombre": "Talagante",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb71')"
},{
  "id": 327,
  "nombre": "El Monte",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb71')"
},{
  "id": 328,
  "nombre": "Isla de Maipo",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb71')"
},{
  "id": 329,
  "nombre": "Padre Hurtado",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb71')"
},{
  "id": 330,
  "nombre": "Pe�aflor",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb71')"
},{
  "id": 331,
  "nombre": "Valdivia",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 332,
  "nombre": "Corral",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 333,
  "nombre": "Lanco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 334,
  "nombre": "Los Lagos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 335,
  "nombre": "M�fil",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 336,
  "nombre": "Mariquina",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 337,
  "nombre": "Paillaco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 338,
  "nombre": "Panguipulli",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5e')"
},{
  "id": 339,
  "nombre": "La Uni�n",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5f')"
},{
  "id": 340,
  "nombre": "Futrono",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5f')"
},{
  "id": 341,
  "nombre": "Lago Ranco",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5f')"
},{
  "id": 342,
  "nombre": "R�o Bueno",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb5f')"
},{
  "id": 343,
  "nombre": "Arica",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3c')"
},{
  "id": 344,
  "nombre": "Camarones",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3c')"
},{
  "id": 345,
  "nombre": "Putre",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3d')"
},{
  "id": 346,
  "nombre": "General Lagos",
  "idProvincia": "ObjectId('628547b84f19e1ad589feb3d')"
}]
        list1=[]
        print()
        for i in range(len(mylist1)):
            list1.append(mylist1[i])  
        mongoDB_collection.insert_many(list1)

    else:
        mongoDB_collection_2.drop()
        start69=time.process_time() + start69
        a=1
        b= start69
        info1 = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_Mongo_Test_3.csv', 'a', newline = '') as csv_file:
          csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
          csv_writer.writerow(info1)
          log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
          log_box3.see("end") 
          cut_duration = 0
          scan_interval = 1
          time.sleep(scan_interval)
        mylist2 = [{
  "id": 1,
  "nombre": "Arica",
  "idRegion": 15,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb39')"
},{
  "id": 2,
  "nombre": "Parinacota",
  "idRegion": 15,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb39')"
},{
  "id": 3,
  "nombre": "Iquique",
  "idRegion": 1,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2b')"
},{
  "id": 4,
  "nombre": "Tamarugal",
  "idRegion": 1,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2b')"
},{
  "id": 5,
  "nombre": "Antofagasta",
  "idRegion": 2,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2c')"
},{
  "id": 6,
  "nombre": "El Loa",
  "idRegion": 2,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2c')"
},{
  "id": 7,
  "nombre": "Tocopilla",
  "idRegion": 2,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2c')"
},{
  "id": 8,
  "nombre": "Copiap�",
  "idRegion": 3,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2d')"
},{
  "id": 9,
  "nombre": "Cha�aral",
  "idRegion": 3,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2d')"
},{
  "id": 10,
  "nombre": "Huasco",
  "idRegion": 3,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2d')"
},{
  "id": 11,
  "nombre": "Elqui",
  "idRegion": 4,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2e')"
},{
  "id": 12,
  "nombre": "Choapa",
  "idRegion": 4,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2e')"
},{
  "id": 13,
  "nombre": "Limar�",
  "idRegion": 4,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2e')"
},{
  "id": 14,
  "nombre": "Valpara�so",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 15,
  "nombre": "Isla de Pascua",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 16,
  "nombre": "Los Andes",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 17,
  "nombre": "Petorca",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 18,
  "nombre": "Quillota",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 19,
  "nombre": "San Antonio",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 20,
  "nombre": "San Felipe de Aconcagua",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 21,
  "nombre": "Marga Marga",
  "idRegion": 5,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb2f')"
},{
  "id": 22,
  "nombre": "Cachapoal",
  "idRegion": 6,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb30')"
},{
  "id": 23,
  "nombre": "Cardenal Caro",
  "idRegion": 6,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb30')"
},{
  "id": 24,
  "nombre": "Colchagua",
  "idRegion": 6,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb30')"
},{
  "id": 25,
  "nombre": "Talca",
  "idRegion": 7,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb31')"
},{
  "id": 26,
  "nombre": "Cauquenes",
  "idRegion": 7,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb31')"
},{
  "id": 27,
  "nombre": "Curic�",
  "idRegion": 7,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb31')"
},{
  "id": 28,
  "nombre": "Linares",
  "idRegion": 7,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb31')"
},{
  "id": 29,
  "nombre": "Concepci�n",
  "idRegion": 8,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb32')"
},{
  "id": 30,
  "nombre": "Arauco",
  "idRegion": 8,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb32')"
},{
  "id": 31,
  "nombre": "Biob�o",
  "idRegion": 8,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb32')"
},{
  "id": 32,
  "nombre": "�uble",
  "idRegion": 8,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb32')"
},{
  "id": 33,
  "nombre": "Caut�n",
  "idRegion": 9,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb33')"
},{
  "id": 34,
  "nombre": "Malleco",
  "idRegion": 9,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb33')"
},{
  "id": 35,
  "nombre": "Valdivia",
  "idRegion": 14,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb38')"
},{
  "id": 36,
  "nombre": "Ranco",
  "idRegion": 14,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb38')"
},{
  "id": 37,
  "nombre": "Llanquihue",
  "idRegion": 10,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb34')"
},{
  "id": 38,
  "nombre": "Chilo�",
  "idRegion": 10,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb34')"
},{
  "id": 39,
  "nombre": "Osorno",
  "idRegion": 10,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb34')"
},{
  "id": 40,
  "nombre": "Palena",
  "idRegion": 10,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb34')"
},{
  "id": 41,
  "nombre": "Coihaique",
  "idRegion": 11,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb35')"
},{
  "id": 42,
  "nombre": "Ais�n",
  "idRegion": 11,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb35')"
},{
  "id": 43,
  "nombre": "Capit�n Prat",
  "idRegion": 11,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb35')"
},{
  "id": 44,
  "nombre": "General Carrera",
  "idRegion": 11,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb35')"
},{
  "id": 45,
  "nombre": "Magallanes",
  "idRegion": 12,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb36')"
},{
  "id": 46,
  "nombre": "Ant�rtica Chilena",
  "idRegion": 12,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb36')"
},{
  "id": 47,
  "nombre": "Tierra del Fuego",
  "idRegion": 12,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb36')"
},{
  "id": 48,
  "nombre": "�ltima Esperanza",
  "idRegion": 12,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb36')"
},{
  "id": 49,
  "nombre": "Santiago",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
},{
  "id": 50,
  "nombre": "Cordillera",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
},{
  "id": 51,
  "nombre": "Chacabuco",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
},{
  "id": 52,
  "nombre": "Maipo",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
},{
  "id": 53,
  "nombre": "Melipilla",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
},{
  "id": 54,
  "nombre": "Talagante",
  "idRegion": 13,
  "idRegion_Object": "ObjectId('6285429d4f19e1ad589feb37')"
}]
        list2=[]
        for i in range(len(mylist2)):
            list2.append(mylist2[i])  
        mongoDB_collection_2.insert_many(list2)

    global start70
    start70=0
    log_box3.insert(tk.END, ' TEST 3 MySQL...')
    if(topic=='Region'):
      val1 = [("1","TarapacÃ¡","CL-TA"),
("2","Antofagasta","CL-AN"),
("3","Atacama","CL-AT"),
("4","Coquimbo","CL-CO"),
("5","ValparaÃ­so","CL-VS"),
("6","RegiÃ³n del Libertador Gral. Bernardo Oâ€™Higgins","CL-LI"),
("7","RegiÃ³n del Maule","CL-ML"),
("8","RegiÃ³n del BiobÃ­o","CL-BI"),
("9","RegiÃ³n de la AraucanÃ­a","CL-AR"),
("10","RegiÃ³n de Los Lagos","CL-LL"),
("11","RegiÃ³n AisÃ©n del Gral. Carlos IbÃ¡Ã±ez del Campo","CL-AI"),
("12","RegiÃ³n de Magallanes y de la AntÃ¡rtica Chilena","CL-MA"),
("13","RegiÃ³n Metropolitana de Santiago","CL-RM"),
("14","RegiÃ³n de Los RÃ­os","CL-LR"),
("15","Arica y Parinacota","CL-AP")
]
      with MySQL_db.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE tbl_region_v2")
        start70=time.process_time() + start70
        a=1
        b=start70
        info = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_MySQL_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sql = "INSERT INTO tbl_region_v2 (id, name, ISO_3166_2_CL) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val1)):
            list.append(val1[i])
        
        cursor.executemany(sql, list)
        MySQL_db.commit()

    elif(topic=='Comuna'):
      val2 = [("1","Iquique","3"),
("2","Alto Hospicio","3"),
("3","Pozo Almonte","4"),
("4","CamiÃ±a","4"),
("5","Colchane","4"),
("6","Huara","4"),
("7","Pica","4"),
("8","Antofagasta","5"),
("9","Mejillones","5"),
("10","Sierra Gorda","5"),
("11","Taltal","5"),
("12","Calama","6"),
("13","OllagÃ¼e","6"),
("14","San Pedro de Atacama","6"),
("15","Tocopilla","7"),
("16","MarÃ­a Elena","7"),
("17","CopiapÃ³","8"),
("18","Caldera","8"),
("19","Tierra Amarilla","8"),
("20","ChaÃ±aral","9"),
("21","Diego de Almagro","9"),
("22","Vallenar","10"),
("23","Alto del Carmen","10"),
("24","Freirina","10"),
("25","Huasco","10"),
("26","La Serena","11"),
("27","Coquimbo","11"),
("28","Andacollo","11"),
("29","La Higuera","11"),
("30","Paihuano","11"),
("31","VicuÃ±a","11"),
("32","Illapel","12"),
("33","Canela","12"),
("34","Los Vilos","12"),
("35","Salamanca","12"),
("36","Ovalle","13"),
("37","CombarbalÃ¡","13"),
("38","Monte Patria","13"),
("39","Punitaqui","13"),
("40","RÃ­o Hurtado","13"),
("41","ValparaÃ­so","14"),
("42","Casablanca","14"),
("43","ConcÃ³n","14"),
("44","Juan FernÃ¡ndez","14"),
("45","PuchuncavÃ­","14"),
("46","Quintero","14"),
("47","ViÃ±a del Mar","14"),
("48","Isla de Pascua","15"),
("49","Los Andes","16"),
("50","Calle Larga","16"),
("51","Rinconada","16"),
("52","San Esteban","16"),
("53","La Ligua","17"),
("54","Cabildo","17"),
("55","Papudo","17"),
("56","Petorca","17"),
("57","Zapallar","17"),
("58","Quillota","18"),
("59","La Calera","18"),
("60","Hijuelas","18"),
("61","La Cruz","18"),
("62","Nogales","18"),
("63","San Antonio","19"),
("64","Algarrobo","19"),
("65","Cartagena","19"),
("66","El Quisco","19"),
("67","El Tabo","19"),
("68","Santo Domingo","19"),
("69","San Felipe","20"),
("70","Catemu","20"),
("71","Llay Llay","20"),
("72","Panquehue","20"),
("73","Putaendo","20"),
("74","Santa MarÃ­a","20"),
("75","QuilpuÃ©","21"),
("76","Limache","21"),
("77","OlmuÃ©","21"),
("78","Villa Alemana","21"),
("79","Rancagua","22"),
("80","Codegua","22"),
("81","Coinco","22"),
("82","Coltauco","22"),
("83","DoÃ±ihue","22"),
("84","Graneros","22"),
("85","Las Cabras","22"),
("86","MachalÃ­","22"),
("87","Malloa","22"),
("88","Mostazal","22"),
("89","Olivar","22"),
("90","Peumo","22"),
("91","Pichidegua","22"),
("92","Quinta de Tilcoco","22"),
("93","Rengo","22"),
("94","RequÃ­noa","22"),
("95","San Vicente","22"),
("96","Pichilemu","23"),
("97","La Estrella","23"),
("98","Litueche","23"),
("99","Marchihue","23"),
("100","Navidad","23"),
("101","Paredones","23"),
("102","San Fernando","24"),
("103","ChÃ©pica","24"),
("104","Chimbarongo","24"),
("105","Lolol","24"),
("106","Nancagua","24"),
("107","Palmilla","24"),
("108","Peralillo","24"),
("109","Placilla","24"),
("110","Pumanque","24"),
("111","Santa Cruz","24"),
("112","Talca","25"),
("113","ConstituciÃ³n","25"),
("114","Curepto","25"),
("115","Empedrado","25"),
("116","Maule","25"),
("117","Pelarco","25"),
("118","Pencahue","25"),
("119","RÃ­o Claro","25"),
("120","San Clemente","25"),
("121","San Rafael","25"),
("122","Cauquenes","26"),
("123","Chanco","26"),
("124","Pelluhue","26"),
("125","CuricÃ³","27"),
("126","HualaÃ±Ã©","27"),
("127","LicantÃ©n","27"),
("128","Molina","27"),
("129","Rauco","27"),
("130","Romeral","27"),
("131","Sagrada Familia","27"),
("132","Teno","27"),
("133","VichuquÃ©n","27"),
("134","Linares","28"),
("135","ColbÃºn","28"),
("136","LongavÃ­","28"),
("137","Parral","28"),
("138","Retiro","28"),
("139","San Javier","28"),
("140","Villa Alegre","28"),
("141","Yerbas Buenas","28"),
("142","ConcepciÃ³n","29"),
("143","Coronel","29"),
("144","Chiguayante","29"),
("145","Florida","29"),
("146","Hualqui","29"),
("147","Lota","29"),
("148","Penco","29"),
("149","San Pedro de la Paz","29"),
("150","Santa Juana","29"),
("151","Talcahuano","29"),
("152","TomÃ©","29"),
("153","HualpÃ©n","29"),
("154","Lebu","30"),
("155","Arauco","30"),
("156","CaÃ±ete","30"),
("157","Contulmo","30"),
("158","Curanilahue","30"),
("159","Los Ãlamos","30"),
("160","TirÃºa","30"),
("161","Los Ãngeles","31"),
("162","Antuco","31"),
("163","Cabrero","31"),
("164","Laja","31"),
("165","MulchÃ©n","31"),
("166","Nacimiento","31"),
("167","Negrete","31"),
("168","Quilaco","31"),
("169","Quilleco","31"),
("170","San Rosendo","31"),
("171","Santa BÃ¡rbara","31"),
("172","Tucapel","31"),
("173","Yumbel","31"),
("174","Alto BiobÃ­o","31"),
("175","ChillÃ¡n","32"),
("176","Bulnes","32"),
("177","Cobquecura","32"),
("178","Coelemu","32"),
("179","Coihueco","32"),
("180","ChillÃ¡n Viejo","32"),
("181","El Carmen","32"),
("182","Ninhue","32"),
("183","Ã‘iquÃ©n","32"),
("184","Pemuco","32"),
("185","Pinto","32"),
("186","Portezuelo","32"),
("187","QuillÃ³n","32"),
("188","Quirihue","32"),
("189","RÃ¡nquil","32"),
("190","San Carlos","32"),
("191","San FabiÃ¡n","32"),
("192","San Ignacio","32"),
("193","San NicolÃ¡s","32"),
("194","Treguaco","32"),
("195","Yungay","32"),
("196","Temuco","33"),
("197","Carahue","33"),
("198","Cunco","33"),
("199","Curarrehue","33"),
("200","Freire","33"),
("201","Galvarino","33"),
("202","Gorbea","33"),
("203","Lautaro","33"),
("204","Loncoche","33"),
("205","Melipeuco","33"),
("206","Nueva Imperial","33"),
("207","Padre las Casas","33"),
("208","Perquenco","33"),
("209","PitrufquÃ©n","33"),
("210","PucÃ³n","33"),
("211","Saavedra","33"),
("212","Teodoro Schmidt","33"),
("213","ToltÃ©n","33"),
("214","VilcÃºn","33"),
("215","Villarrica","33"),
("216","Cholchol","33"),
("217","Angol","34"),
("218","Collipulli","34"),
("219","CuracautÃ­n","34"),
("220","Ercilla","34"),
("221","Lonquimay","34"),
("222","Los Sauces","34"),
("223","Lumaco","34"),
("224","PurÃ©n","34"),
("225","Renaico","34"),
("226","TraiguÃ©n","34"),
("227","Victoria","34"),
("228","Puerto Montt","37"),
("229","Calbuco","37"),
("230","CochamÃ³","37"),
("231","Fresia","37"),
("232","Frutillar","37"),
("233","Los Muermos","37"),
("234","Llanquihue","37"),
("235","MaullÃ­n","37"),
("236","Puerto Varas","37"),
("237","Castro","38"),
("238","Ancud","38"),
("239","Chonchi","38"),
("240","Curaco de VÃ©lez","38"),
("241","Dalcahue","38"),
("242","PuqueldÃ³n","38"),
("243","QueilÃ©n","38"),
("244","QuellÃ³n","38"),
("245","Quemchi","38"),
("246","Quinchao","38"),
("247","Osorno","39"),
("248","Puerto Octay","39"),
("249","Purranque","39"),
("250","Puyehue","39"),
("251","RÃ­o Negro","39"),
("252","San Juan de la Costa","39"),
("253","San Pablo","39"),
("254","ChaitÃ©n","40"),
("255","FutaleufÃº","40"),
("256","HualaihuÃ©","40"),
("257","Palena","40"),
("258","Coyhaique","41"),
("259","Lago Verde","41"),
("260","AysÃ©n","42"),
("261","Cisnes","42"),
("262","Guaitecas","42"),
("263","Cochrane","43"),
("264","O'Higgins","43"),
("265","Tortel","43"),
("266","Chile Chico","44"),
("267","RÃ­o IbÃ¡Ã±ez","44"),
("268","Punta Arenas","45"),
("269","Laguna Blanca","45"),
("270","RÃ­o Verde","45"),
("271","San Gregorio","45"),
("272","Cabo de Hornos","46"),
("273","AntÃ¡rtica","46"),
("274","Porvenir","47"),
("275","Primavera","47"),
("276","Timaukel","47"),
("277","Natales","48"),
("278","Torres del Paine","48"),
("279","Santiago","49"),
("280","Cerrillos","49"),
("281","Cerro Navia","49"),
("282","ConchalÃ­","49"),
("283","El Bosque","49"),
("284","EstaciÃ³n Central","49"),
("285","Huechuraba","49"),
("286","Independencia","49"),
("287","La Cisterna","49"),
("288","La Florida","49"),
("289","La Granja","49"),
("290","La Pintana","49"),
("291","La Reina","49"),
("292","Las Condes","49"),
("293","Lo Barnechea","49"),
("294","Lo Espejo","49"),
("295","Lo Prado","49"),
("296","Macul","49"),
("297","MaipÃº","49"),
("298","Ã‘uÃ±oa","49"),
("299","Pedro Aguirre Cerda","49"),
("300","PeÃ±alolÃ©n","49"),
("301","Providencia","49"),
("302","Pudahuel","49"),
("303","Quilicura","49"),
("304","Quinta Normal","49"),
("305","Recoleta","49"),
("306","Renca","49"),
("307","San JoaquÃ­n","49"),
("308","San Miguel","49"),
("309","San RamÃ³n","49"),
("310","Vitacura","49"),
("311","Puente Alto","50"),
("312","Pirque","50"),
("313","San JosÃ© de Maipo","50"),
("314","Colina","51"),
("315","Lampa","51"),
("316","Tiltil","51"),
("317","San Bernardo","52"),
("318","Buin","52"),
("319","Calera de Tango","52"),
("320","Paine","52"),
("321","Melipilla","53"),
("322","AlhuÃ©","53"),
("323","CuracavÃ­","53"),
("324","MarÃ­a Pinto","53"),
("325","San Pedro","53"),
("326","Talagante","54"),
("327","El Monte","54"),
("328","Isla de Maipo","54"),
("329","Padre Hurtado","54"),
("330","PeÃ±aflor","54"),
("331","Valdivia","35"),
("332","Corral","35"),
("333","Lanco","35"),
("334","Los Lagos","35"),
("335","MÃ¡fil","35"),
("336","Mariquina","35"),
("337","Paillaco","35"),
("338","Panguipulli","35"),
("339","La UniÃ³n","36"),
("340","Futrono","36"),
("341","Lago Ranco","36"),
("342","RÃ­o Bueno","36"),
("343","Arica","1"),
("344","Camarones","1"),
("345","Putre","2"),
("346","General Lagos","2")
]
      with MySQL_db.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE tbl_comuna")
        start70=time.process_time() + start70
        a=1
        b=start70
        info = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_MySQL_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sql = "INSERT INTO tbl_comuna (id, nombre, idProvincia) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val2)):
            list.append(val2[i])
        
        cursor.executemany(sql, list)
        MySQL_db.commit()
    
    else:
      with MySQL_db.cursor() as cursor:
        val3 = [("1","Arica","15"),
("2","Parinacota","15"),
("3","Iquique","1"),
("4","Tamarugal","1"),
("5","Antofagasta","2"),
("6","El Loa","2"),
("7","Tocopilla","2"),
("8","CopiapÃ³","3"),
("9","ChaÃ±aral","3"),
("10","Huasco","3"),
("11","Elqui","4"),
("12","Choapa","4"),
("13","LimarÃ­","4"),
("14","ValparaÃ­so","5"),
("15","Isla de Pascua","5"),
("16","Los Andes","5"),
("17","Petorca","5"),
("18","Quillota","5"),
("19","San Antonio","5"),
("20","San Felipe de Aconcagua","5"),
("21","Marga Marga","5"),
("22","Cachapoal","6"),
("23","Cardenal Caro","6"),
("24","Colchagua","6"),
("25","Talca","7"),
("26","Cauquenes","7"),
("27","CuricÃ³","7"),
("28","Linares","7"),
("29","ConcepciÃ³n","8"),
("30","Arauco","8"),
("31","BiobÃ­o","8"),
("32","Ã‘uble","8"),
("33","CautÃ­n","9"),
("34","Malleco","9"),
("35","Valdivia","14"),
("36","Ranco","14"),
("37","Llanquihue","10"),
("38","ChiloÃ©","10"),
("39","Osorno","10"),
("40","Palena","10"),
("41","Coihaique","11"),
("42","AisÃ©n","11"),
("43","CapitÃ¡n Prat","11"),
("44","General Carrera","11"),
("45","Magallanes","12"),
("46","AntÃ¡rtica Chilena","12"),
("47","Tierra del Fuego","12"),
("48","Ãšltima Esperanza","12"),
("49","Santiago","13"),
("50","Cordillera","13"),
("51","Chacabuco","13"),
("52","Maipo","13"),
("53","Melipilla","13"),
("54","Talagante","13")
]
        cursor.execute("TRUNCATE TABLE tbl_provincia_v2")
        start70=time.process_time() + start70
        a=1
        b=start70
        info = {
            'Iteracion': a,
            'Hora' : b,
            }
        with open('Data/Parte_3_MySQL_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sql = "INSERT INTO tbl_provincia_v2 (id, nombre, idRegion) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val3)):
            list.append(val3[i])
        
        cursor.executemany(sql, list)
        MySQL_db.commit()

    global start71
    start71=0
    log_box3.insert(tk.END, ' \nTEST 3 SQL Server...')
    if(topic=='Comuna'):
      with cnxn.cursor() as cursor:
        val2 = [("1","Iquique","3"),
("2","Alto Hospicio","3"),
("3","Pozo Almonte","4"),
("4","CamiÃ±a","4"),
("5","Colchane","4"),
("6","Huara","4"),
("7","Pica","4"),
("8","Antofagasta","5"),
("9","Mejillones","5"),
("10","Sierra Gorda","5"),
("11","Taltal","5"),
("12","Calama","6"),
("13","OllagÃ¼e","6"),
("14","San Pedro de Atacama","6"),
("15","Tocopilla","7"),
("16","MarÃ­a Elena","7"),
("17","CopiapÃ³","8"),
("18","Caldera","8"),
("19","Tierra Amarilla","8"),
("20","ChaÃ±aral","9"),
("21","Diego de Almagro","9"),
("22","Vallenar","10"),
("23","Alto del Carmen","10"),
("24","Freirina","10"),
("25","Huasco","10"),
("26","La Serena","11"),
("27","Coquimbo","11"),
("28","Andacollo","11"),
("29","La Higuera","11"),
("30","Paihuano","11"),
("31","VicuÃ±a","11"),
("32","Illapel","12"),
("33","Canela","12"),
("34","Los Vilos","12"),
("35","Salamanca","12"),
("36","Ovalle","13"),
("37","CombarbalÃ¡","13"),
("38","Monte Patria","13"),
("39","Punitaqui","13"),
("40","RÃ­o Hurtado","13"),
("41","ValparaÃ­so","14"),
("42","Casablanca","14"),
("43","ConcÃ³n","14"),
("44","Juan FernÃ¡ndez","14"),
("45","PuchuncavÃ­","14"),
("46","Quintero","14"),
("47","ViÃ±a del Mar","14"),
("48","Isla de Pascua","15"),
("49","Los Andes","16"),
("50","Calle Larga","16"),
("51","Rinconada","16"),
("52","San Esteban","16"),
("53","La Ligua","17"),
("54","Cabildo","17"),
("55","Papudo","17"),
("56","Petorca","17"),
("57","Zapallar","17"),
("58","Quillota","18"),
("59","La Calera","18"),
("60","Hijuelas","18"),
("61","La Cruz","18"),
("62","Nogales","18"),
("63","San Antonio","19"),
("64","Algarrobo","19"),
("65","Cartagena","19"),
("66","El Quisco","19"),
("67","El Tabo","19"),
("68","Santo Domingo","19"),
("69","San Felipe","20"),
("70","Catemu","20"),
("71","Llay Llay","20"),
("72","Panquehue","20"),
("73","Putaendo","20"),
("74","Santa MarÃ­a","20"),
("75","QuilpuÃ©","21"),
("76","Limache","21"),
("77","OlmuÃ©","21"),
("78","Villa Alemana","21"),
("79","Rancagua","22"),
("80","Codegua","22"),
("81","Coinco","22"),
("82","Coltauco","22"),
("83","DoÃ±ihue","22"),
("84","Graneros","22"),
("85","Las Cabras","22"),
("86","MachalÃ­","22"),
("87","Malloa","22"),
("88","Mostazal","22"),
("89","Olivar","22"),
("90","Peumo","22"),
("91","Pichidegua","22"),
("92","Quinta de Tilcoco","22"),
("93","Rengo","22"),
("94","RequÃ­noa","22"),
("95","San Vicente","22"),
("96","Pichilemu","23"),
("97","La Estrella","23"),
("98","Litueche","23"),
("99","Marchihue","23"),
("100","Navidad","23"),
("101","Paredones","23"),
("102","San Fernando","24"),
("103","ChÃ©pica","24"),
("104","Chimbarongo","24"),
("105","Lolol","24"),
("106","Nancagua","24"),
("107","Palmilla","24"),
("108","Peralillo","24"),
("109","Placilla","24"),
("110","Pumanque","24"),
("111","Santa Cruz","24"),
("112","Talca","25"),
("113","ConstituciÃ³n","25"),
("114","Curepto","25"),
("115","Empedrado","25"),
("116","Maule","25"),
("117","Pelarco","25"),
("118","Pencahue","25"),
("119","RÃ­o Claro","25"),
("120","San Clemente","25"),
("121","San Rafael","25"),
("122","Cauquenes","26"),
("123","Chanco","26"),
("124","Pelluhue","26"),
("125","CuricÃ³","27"),
("126","HualaÃ±Ã©","27"),
("127","LicantÃ©n","27"),
("128","Molina","27"),
("129","Rauco","27"),
("130","Romeral","27"),
("131","Sagrada Familia","27"),
("132","Teno","27"),
("133","VichuquÃ©n","27"),
("134","Linares","28"),
("135","ColbÃºn","28"),
("136","LongavÃ­","28"),
("137","Parral","28"),
("138","Retiro","28"),
("139","San Javier","28"),
("140","Villa Alegre","28"),
("141","Yerbas Buenas","28"),
("142","ConcepciÃ³n","29"),
("143","Coronel","29"),
("144","Chiguayante","29"),
("145","Florida","29"),
("146","Hualqui","29"),
("147","Lota","29"),
("148","Penco","29"),
("149","San Pedro de la Paz","29"),
("150","Santa Juana","29"),
("151","Talcahuano","29"),
("152","TomÃ©","29"),
("153","HualpÃ©n","29"),
("154","Lebu","30"),
("155","Arauco","30"),
("156","CaÃ±ete","30"),
("157","Contulmo","30"),
("158","Curanilahue","30"),
("159","Los Ãlamos","30"),
("160","TirÃºa","30"),
("161","Los Ãngeles","31"),
("162","Antuco","31"),
("163","Cabrero","31"),
("164","Laja","31"),
("165","MulchÃ©n","31"),
("166","Nacimiento","31"),
("167","Negrete","31"),
("168","Quilaco","31"),
("169","Quilleco","31"),
("170","San Rosendo","31"),
("171","Santa BÃ¡rbara","31"),
("172","Tucapel","31"),
("173","Yumbel","31"),
("174","Alto BiobÃ­o","31"),
("175","ChillÃ¡n","32"),
("176","Bulnes","32"),
("177","Cobquecura","32"),
("178","Coelemu","32"),
("179","Coihueco","32"),
("180","ChillÃ¡n Viejo","32"),
("181","El Carmen","32"),
("182","Ninhue","32"),
("183","Ã‘iquÃ©n","32"),
("184","Pemuco","32"),
("185","Pinto","32"),
("186","Portezuelo","32"),
("187","QuillÃ³n","32"),
("188","Quirihue","32"),
("189","RÃ¡nquil","32"),
("190","San Carlos","32"),
("191","San FabiÃ¡n","32"),
("192","San Ignacio","32"),
("193","San NicolÃ¡s","32"),
("194","Treguaco","32"),
("195","Yungay","32"),
("196","Temuco","33"),
("197","Carahue","33"),
("198","Cunco","33"),
("199","Curarrehue","33"),
("200","Freire","33"),
("201","Galvarino","33"),
("202","Gorbea","33"),
("203","Lautaro","33"),
("204","Loncoche","33"),
("205","Melipeuco","33"),
("206","Nueva Imperial","33"),
("207","Padre las Casas","33"),
("208","Perquenco","33"),
("209","PitrufquÃ©n","33"),
("210","PucÃ³n","33"),
("211","Saavedra","33"),
("212","Teodoro Schmidt","33"),
("213","ToltÃ©n","33"),
("214","VilcÃºn","33"),
("215","Villarrica","33"),
("216","Cholchol","33"),
("217","Angol","34"),
("218","Collipulli","34"),
("219","CuracautÃ­n","34"),
("220","Ercilla","34"),
("221","Lonquimay","34"),
("222","Los Sauces","34"),
("223","Lumaco","34"),
("224","PurÃ©n","34"),
("225","Renaico","34"),
("226","TraiguÃ©n","34"),
("227","Victoria","34"),
("228","Puerto Montt","37"),
("229","Calbuco","37"),
("230","CochamÃ³","37"),
("231","Fresia","37"),
("232","Frutillar","37"),
("233","Los Muermos","37"),
("234","Llanquihue","37"),
("235","MaullÃ­n","37"),
("236","Puerto Varas","37"),
("237","Castro","38"),
("238","Ancud","38"),
("239","Chonchi","38"),
("240","Curaco de VÃ©lez","38"),
("241","Dalcahue","38"),
("242","PuqueldÃ³n","38"),
("243","QueilÃ©n","38"),
("244","QuellÃ³n","38"),
("245","Quemchi","38"),
("246","Quinchao","38"),
("247","Osorno","39"),
("248","Puerto Octay","39"),
("249","Purranque","39"),
("250","Puyehue","39"),
("251","RÃ­o Negro","39"),
("252","San Juan de la Costa","39"),
("253","San Pablo","39"),
("254","ChaitÃ©n","40"),
("255","FutaleufÃº","40"),
("256","HualaihuÃ©","40"),
("257","Palena","40"),
("258","Coyhaique","41"),
("259","Lago Verde","41"),
("260","AysÃ©n","42"),
("261","Cisnes","42"),
("262","Guaitecas","42"),
("263","Cochrane","43"),
("264","O'Higgins","43"),
("265","Tortel","43"),
("266","Chile Chico","44"),
("267","RÃ­o IbÃ¡Ã±ez","44"),
("268","Punta Arenas","45"),
("269","Laguna Blanca","45"),
("270","RÃ­o Verde","45"),
("271","San Gregorio","45"),
("272","Cabo de Hornos","46"),
("273","AntÃ¡rtica","46"),
("274","Porvenir","47"),
("275","Primavera","47"),
("276","Timaukel","47"),
("277","Natales","48"),
("278","Torres del Paine","48"),
("279","Santiago","49"),
("280","Cerrillos","49"),
("281","Cerro Navia","49"),
("282","ConchalÃ­","49"),
("283","El Bosque","49"),
("284","EstaciÃ³n Central","49"),
("285","Huechuraba","49"),
("286","Independencia","49"),
("287","La Cisterna","49"),
("288","La Florida","49"),
("289","La Granja","49"),
("290","La Pintana","49"),
("291","La Reina","49"),
("292","Las Condes","49"),
("293","Lo Barnechea","49"),
("294","Lo Espejo","49"),
("295","Lo Prado","49"),
("296","Macul","49"),
("297","MaipÃº","49"),
("298","Ã‘uÃ±oa","49"),
("299","Pedro Aguirre Cerda","49"),
("300","PeÃ±alolÃ©n","49"),
("301","Providencia","49"),
("302","Pudahuel","49"),
("303","Quilicura","49"),
("304","Quinta Normal","49"),
("305","Recoleta","49"),
("306","Renca","49"),
("307","San JoaquÃ­n","49"),
("308","San Miguel","49"),
("309","San RamÃ³n","49"),
("310","Vitacura","49"),
("311","Puente Alto","50"),
("312","Pirque","50"),
("313","San JosÃ© de Maipo","50"),
("314","Colina","51"),
("315","Lampa","51"),
("316","Tiltil","51"),
("317","San Bernardo","52"),
("318","Buin","52"),
("319","Calera de Tango","52"),
("320","Paine","52"),
("321","Melipilla","53"),
("322","AlhuÃ©","53"),
("323","CuracavÃ­","53"),
("324","MarÃ­a Pinto","53"),
("325","San Pedro","53"),
("326","Talagante","54"),
("327","El Monte","54"),
("328","Isla de Maipo","54"),
("329","Padre Hurtado","54"),
("330","PeÃ±aflor","54"),
("331","Valdivia","35"),
("332","Corral","35"),
("333","Lanco","35"),
("334","Los Lagos","35"),
("335","MÃ¡fil","35"),
("336","Mariquina","35"),
("337","Paillaco","35"),
("338","Panguipulli","35"),
("339","La UniÃ³n","36"),
("340","Futrono","36"),
("341","Lago Ranco","36"),
("342","RÃ­o Bueno","36"),
("343","Arica","1"),
("344","Camarones","1"),
("345","Putre","2"),
("346","General Lagos","2")
]
        cursor.execute("TRUNCATE TABLE tbl_comuna")
        start71=time.process_time() + start71
        a2=1
        b2=start71
        info3 = {
            'Iteracion': a2,
            'Hora' : b2,
            }
        with open('Data/Parte_3_SQLServerTest_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info3)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a2}, Hora: {b2}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqls = "INSERT INTO tbl_comuna (id, nombre, idProvincia ) VALUES (?, ?, ?)"
        list=[]
        for i in range(len(val2)):
          list.append(val2[i])
        cursor.executemany(sqls, list)
        cnxn.commit()
    
    
    elif(topic=='Region'):
      with cnxn.cursor() as cursor:
        val1 = [("1","TarapacÃ¡","CL-TA"),
("2","Antofagasta","CL-AN"),
("3","Atacama","CL-AT"),
("4","Coquimbo","CL-CO"),
("5","ValparaÃ­so","CL-VS"),
("6","RegiÃ³n del Libertador Gral. Bernardo Oâ€™Higgins","CL-LI"),
("7","RegiÃ³n del Maule","CL-ML"),
("8","RegiÃ³n del BiobÃ­o","CL-BI"),
("9","RegiÃ³n de la AraucanÃ­a","CL-AR"),
("10","RegiÃ³n de Los Lagos","CL-LL"),
("11","RegiÃ³n AisÃ©n del Gral. Carlos IbÃ¡Ã±ez del Campo","CL-AI"),
("12","RegiÃ³n de Magallanes y de la AntÃ¡rtica Chilena","CL-MA"),
("13","RegiÃ³n Metropolitana de Santiago","CL-RM"),
("14","RegiÃ³n de Los RÃ­os","CL-LR"),
("15","Arica y Parinacota","CL-AP")
]
        cursor.execute("TRUNCATE TABLE tbl_region_v2")
        start71=time.process_time() + start71
        a2=1
        b2=start71
        info3 = {
            'Iteracion': a2,
            'Hora' : b2,
            }
        with open('Data/Parte_3_SQLServerTest_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info3)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a2}, Hora: {b2}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqls = "INSERT INTO tbl_region_v2 (id, nombre, ISO_3166_2_CL) VALUES (?, ?, ?)"
        list=[]
        for i in range(len(val1)):
          list.append(val1[i])
        cursor.executemany(sqls, list)
        cnxn.commit()

    else:
      with cnxn.cursor() as cursor:
        val3 = [("1","Arica","15"),
("2","Parinacota","15"),
("3","Iquique","1"),
("4","Tamarugal","1"),
("5","Antofagasta","2"),
("6","El Loa","2"),
("7","Tocopilla","2"),
("8","CopiapÃ³","3"),
("9","ChaÃ±aral","3"),
("10","Huasco","3"),
("11","Elqui","4"),
("12","Choapa","4"),
("13","LimarÃ­","4"),
("14","ValparaÃ­so","5"),
("15","Isla de Pascua","5"),
("16","Los Andes","5"),
("17","Petorca","5"),
("18","Quillota","5"),
("19","San Antonio","5"),
("20","San Felipe de Aconcagua","5"),
("21","Marga Marga","5"),
("22","Cachapoal","6"),
("23","Cardenal Caro","6"),
("24","Colchagua","6"),
("25","Talca","7"),
("26","Cauquenes","7"),
("27","CuricÃ³","7"),
("28","Linares","7"),
("29","ConcepciÃ³n","8"),
("30","Arauco","8"),
("31","BiobÃ­o","8"),
("32","Ã‘uble","8"),
("33","CautÃ­n","9"),
("34","Malleco","9"),
("35","Valdivia","14"),
("36","Ranco","14"),
("37","Llanquihue","10"),
("38","ChiloÃ©","10"),
("39","Osorno","10"),
("40","Palena","10"),
("41","Coihaique","11"),
("42","AisÃ©n","11"),
("43","CapitÃ¡n Prat","11"),
("44","General Carrera","11"),
("45","Magallanes","12"),
("46","AntÃ¡rtica Chilena","12"),
("47","Tierra del Fuego","12"),
("48","Ãšltima Esperanza","12"),
("49","Santiago","13"),
("50","Cordillera","13"),
("51","Chacabuco","13"),
("52","Maipo","13"),
("53","Melipilla","13"),
("54","Talagante","13")
]

        cursor.execute("TRUNCATE TABLE tbl_provincia_v2")
        start71=time.process_time() + start71
        a2=1
        b2=start71
        info3 = {
            'Iteracion': a2,
            'Hora' : b2,
            }
        with open('Data/Parte_3_SQLServerTest_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info3)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a2}, Hora: {b2}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqls = "INSERT INTO tbl_provincia_v2 (id, nombre, idRegion) VALUES (?, ?, ?)"
        list=[]
        for i in range(len(val3)):
          list.append(val3[i])
        cursor.executemany(sqls, list)
        cnxn.commit()

    global start81
    start81=0
    log_box3.insert(tk.END, ' \nTEST 3 PostgreSQL...')
    if(topic=='Comuna'):
      with conn.cursor() as cursor:
        val2 = [("1","Iquique","3"),
("2","Alto Hospicio","3"),
("3","Pozo Almonte","4"),
("4","CamiÃ±a","4"),
("5","Colchane","4"),
("6","Huara","4"),
("7","Pica","4"),
("8","Antofagasta","5"),
("9","Mejillones","5"),
("10","Sierra Gorda","5"),
("11","Taltal","5"),
("12","Calama","6"),
("13","OllagÃ¼e","6"),
("14","San Pedro de Atacama","6"),
("15","Tocopilla","7"),
("16","MarÃ­a Elena","7"),
("17","CopiapÃ³","8"),
("18","Caldera","8"),
("19","Tierra Amarilla","8"),
("20","ChaÃ±aral","9"),
("21","Diego de Almagro","9"),
("22","Vallenar","10"),
("23","Alto del Carmen","10"),
("24","Freirina","10"),
("25","Huasco","10"),
("26","La Serena","11"),
("27","Coquimbo","11"),
("28","Andacollo","11"),
("29","La Higuera","11"),
("30","Paihuano","11"),
("31","VicuÃ±a","11"),
("32","Illapel","12"),
("33","Canela","12"),
("34","Los Vilos","12"),
("35","Salamanca","12"),
("36","Ovalle","13"),
("37","CombarbalÃ¡","13"),
("38","Monte Patria","13"),
("39","Punitaqui","13"),
("40","RÃ­o Hurtado","13"),
("41","ValparaÃ­so","14"),
("42","Casablanca","14"),
("43","ConcÃ³n","14"),
("44","Juan FernÃ¡ndez","14"),
("45","PuchuncavÃ­","14"),
("46","Quintero","14"),
("47","ViÃ±a del Mar","14"),
("48","Isla de Pascua","15"),
("49","Los Andes","16"),
("50","Calle Larga","16"),
("51","Rinconada","16"),
("52","San Esteban","16"),
("53","La Ligua","17"),
("54","Cabildo","17"),
("55","Papudo","17"),
("56","Petorca","17"),
("57","Zapallar","17"),
("58","Quillota","18"),
("59","La Calera","18"),
("60","Hijuelas","18"),
("61","La Cruz","18"),
("62","Nogales","18"),
("63","San Antonio","19"),
("64","Algarrobo","19"),
("65","Cartagena","19"),
("66","El Quisco","19"),
("67","El Tabo","19"),
("68","Santo Domingo","19"),
("69","San Felipe","20"),
("70","Catemu","20"),
("71","Llay Llay","20"),
("72","Panquehue","20"),
("73","Putaendo","20"),
("74","Santa MarÃ­a","20"),
("75","QuilpuÃ©","21"),
("76","Limache","21"),
("77","OlmuÃ©","21"),
("78","Villa Alemana","21"),
("79","Rancagua","22"),
("80","Codegua","22"),
("81","Coinco","22"),
("82","Coltauco","22"),
("83","DoÃ±ihue","22"),
("84","Graneros","22"),
("85","Las Cabras","22"),
("86","MachalÃ­","22"),
("87","Malloa","22"),
("88","Mostazal","22"),
("89","Olivar","22"),
("90","Peumo","22"),
("91","Pichidegua","22"),
("92","Quinta de Tilcoco","22"),
("93","Rengo","22"),
("94","RequÃ­noa","22"),
("95","San Vicente","22"),
("96","Pichilemu","23"),
("97","La Estrella","23"),
("98","Litueche","23"),
("99","Marchihue","23"),
("100","Navidad","23"),
("101","Paredones","23"),
("102","San Fernando","24"),
("103","ChÃ©pica","24"),
("104","Chimbarongo","24"),
("105","Lolol","24"),
("106","Nancagua","24"),
("107","Palmilla","24"),
("108","Peralillo","24"),
("109","Placilla","24"),
("110","Pumanque","24"),
("111","Santa Cruz","24"),
("112","Talca","25"),
("113","ConstituciÃ³n","25"),
("114","Curepto","25"),
("115","Empedrado","25"),
("116","Maule","25"),
("117","Pelarco","25"),
("118","Pencahue","25"),
("119","RÃ­o Claro","25"),
("120","San Clemente","25"),
("121","San Rafael","25"),
("122","Cauquenes","26"),
("123","Chanco","26"),
("124","Pelluhue","26"),
("125","CuricÃ³","27"),
("126","HualaÃ±Ã©","27"),
("127","LicantÃ©n","27"),
("128","Molina","27"),
("129","Rauco","27"),
("130","Romeral","27"),
("131","Sagrada Familia","27"),
("132","Teno","27"),
("133","VichuquÃ©n","27"),
("134","Linares","28"),
("135","ColbÃºn","28"),
("136","LongavÃ­","28"),
("137","Parral","28"),
("138","Retiro","28"),
("139","San Javier","28"),
("140","Villa Alegre","28"),
("141","Yerbas Buenas","28"),
("142","ConcepciÃ³n","29"),
("143","Coronel","29"),
("144","Chiguayante","29"),
("145","Florida","29"),
("146","Hualqui","29"),
("147","Lota","29"),
("148","Penco","29"),
("149","San Pedro de la Paz","29"),
("150","Santa Juana","29"),
("151","Talcahuano","29"),
("152","TomÃ©","29"),
("153","HualpÃ©n","29"),
("154","Lebu","30"),
("155","Arauco","30"),
("156","CaÃ±ete","30"),
("157","Contulmo","30"),
("158","Curanilahue","30"),
("159","Los Ãlamos","30"),
("160","TirÃºa","30"),
("161","Los Ãngeles","31"),
("162","Antuco","31"),
("163","Cabrero","31"),
("164","Laja","31"),
("165","MulchÃ©n","31"),
("166","Nacimiento","31"),
("167","Negrete","31"),
("168","Quilaco","31"),
("169","Quilleco","31"),
("170","San Rosendo","31"),
("171","Santa BÃ¡rbara","31"),
("172","Tucapel","31"),
("173","Yumbel","31"),
("174","Alto BiobÃ­o","31"),
("175","ChillÃ¡n","32"),
("176","Bulnes","32"),
("177","Cobquecura","32"),
("178","Coelemu","32"),
("179","Coihueco","32"),
("180","ChillÃ¡n Viejo","32"),
("181","El Carmen","32"),
("182","Ninhue","32"),
("183","Ã‘iquÃ©n","32"),
("184","Pemuco","32"),
("185","Pinto","32"),
("186","Portezuelo","32"),
("187","QuillÃ³n","32"),
("188","Quirihue","32"),
("189","RÃ¡nquil","32"),
("190","San Carlos","32"),
("191","San FabiÃ¡n","32"),
("192","San Ignacio","32"),
("193","San NicolÃ¡s","32"),
("194","Treguaco","32"),
("195","Yungay","32"),
("196","Temuco","33"),
("197","Carahue","33"),
("198","Cunco","33"),
("199","Curarrehue","33"),
("200","Freire","33"),
("201","Galvarino","33"),
("202","Gorbea","33"),
("203","Lautaro","33"),
("204","Loncoche","33"),
("205","Melipeuco","33"),
("206","Nueva Imperial","33"),
("207","Padre las Casas","33"),
("208","Perquenco","33"),
("209","PitrufquÃ©n","33"),
("210","PucÃ³n","33"),
("211","Saavedra","33"),
("212","Teodoro Schmidt","33"),
("213","ToltÃ©n","33"),
("214","VilcÃºn","33"),
("215","Villarrica","33"),
("216","Cholchol","33"),
("217","Angol","34"),
("218","Collipulli","34"),
("219","CuracautÃ­n","34"),
("220","Ercilla","34"),
("221","Lonquimay","34"),
("222","Los Sauces","34"),
("223","Lumaco","34"),
("224","PurÃ©n","34"),
("225","Renaico","34"),
("226","TraiguÃ©n","34"),
("227","Victoria","34"),
("228","Puerto Montt","37"),
("229","Calbuco","37"),
("230","CochamÃ³","37"),
("231","Fresia","37"),
("232","Frutillar","37"),
("233","Los Muermos","37"),
("234","Llanquihue","37"),
("235","MaullÃ­n","37"),
("236","Puerto Varas","37"),
("237","Castro","38"),
("238","Ancud","38"),
("239","Chonchi","38"),
("240","Curaco de VÃ©lez","38"),
("241","Dalcahue","38"),
("242","PuqueldÃ³n","38"),
("243","QueilÃ©n","38"),
("244","QuellÃ³n","38"),
("245","Quemchi","38"),
("246","Quinchao","38"),
("247","Osorno","39"),
("248","Puerto Octay","39"),
("249","Purranque","39"),
("250","Puyehue","39"),
("251","RÃ­o Negro","39"),
("252","San Juan de la Costa","39"),
("253","San Pablo","39"),
("254","ChaitÃ©n","40"),
("255","FutaleufÃº","40"),
("256","HualaihuÃ©","40"),
("257","Palena","40"),
("258","Coyhaique","41"),
("259","Lago Verde","41"),
("260","AysÃ©n","42"),
("261","Cisnes","42"),
("262","Guaitecas","42"),
("263","Cochrane","43"),
("264","O'Higgins","43"),
("265","Tortel","43"),
("266","Chile Chico","44"),
("267","RÃ­o IbÃ¡Ã±ez","44"),
("268","Punta Arenas","45"),
("269","Laguna Blanca","45"),
("270","RÃ­o Verde","45"),
("271","San Gregorio","45"),
("272","Cabo de Hornos","46"),
("273","AntÃ¡rtica","46"),
("274","Porvenir","47"),
("275","Primavera","47"),
("276","Timaukel","47"),
("277","Natales","48"),
("278","Torres del Paine","48"),
("279","Santiago","49"),
("280","Cerrillos","49"),
("281","Cerro Navia","49"),
("282","ConchalÃ­","49"),
("283","El Bosque","49"),
("284","EstaciÃ³n Central","49"),
("285","Huechuraba","49"),
("286","Independencia","49"),
("287","La Cisterna","49"),
("288","La Florida","49"),
("289","La Granja","49"),
("290","La Pintana","49"),
("291","La Reina","49"),
("292","Las Condes","49"),
("293","Lo Barnechea","49"),
("294","Lo Espejo","49"),
("295","Lo Prado","49"),
("296","Macul","49"),
("297","MaipÃº","49"),
("298","Ã‘uÃ±oa","49"),
("299","Pedro Aguirre Cerda","49"),
("300","PeÃ±alolÃ©n","49"),
("301","Providencia","49"),
("302","Pudahuel","49"),
("303","Quilicura","49"),
("304","Quinta Normal","49"),
("305","Recoleta","49"),
("306","Renca","49"),
("307","San JoaquÃ­n","49"),
("308","San Miguel","49"),
("309","San RamÃ³n","49"),
("310","Vitacura","49"),
("311","Puente Alto","50"),
("312","Pirque","50"),
("313","San JosÃ© de Maipo","50"),
("314","Colina","51"),
("315","Lampa","51"),
("316","Tiltil","51"),
("317","San Bernardo","52"),
("318","Buin","52"),
("319","Calera de Tango","52"),
("320","Paine","52"),
("321","Melipilla","53"),
("322","AlhuÃ©","53"),
("323","CuracavÃ­","53"),
("324","MarÃ­a Pinto","53"),
("325","San Pedro","53"),
("326","Talagante","54"),
("327","El Monte","54"),
("328","Isla de Maipo","54"),
("329","Padre Hurtado","54"),
("330","PeÃ±aflor","54"),
("331","Valdivia","35"),
("332","Corral","35"),
("333","Lanco","35"),
("334","Los Lagos","35"),
("335","MÃ¡fil","35"),
("336","Mariquina","35"),
("337","Paillaco","35"),
("338","Panguipulli","35"),
("339","La UniÃ³n","36"),
("340","Futrono","36"),
("341","Lago Ranco","36"),
("342","RÃ­o Bueno","36"),
("343","Arica","1"),
("344","Camarones","1"),
("345","Putre","2"),
("346","General Lagos","2")
]
        cursor.execute("TRUNCATE TABLE tbl_comuna")
        start81=time.process_time() + start81
        a99=1
        b99=start81
        info99 = {
            'Iteracion': a99,
            'Hora' : b99,
        }
        with open('Data/Parte_3_Postgres_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info99)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqlpot = "INSERT INTO tbl_comuna (id, nombre, idprovincia) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val2)):
            list.append(val2[i])
        cursor.executemany(sqlpot, list)
        conn.commit()

    elif(topic=='Region'):
      with conn.cursor() as cursor:
        val1 = [("1","TarapacÃ¡","CL-TA"),
("2","Antofagasta","CL-AN"),
("3","Atacama","CL-AT"),
("4","Coquimbo","CL-CO"),
("5","ValparaÃ­so","CL-VS"),
("6","RegiÃ³n del Libertador Gral. Bernardo Oâ€™Higgins","CL-LI"),
("7","RegiÃ³n del Maule","CL-ML"),
("8","RegiÃ³n del BiobÃ­o","CL-BI"),
("9","RegiÃ³n de la AraucanÃ­a","CL-AR"),
("10","RegiÃ³n de Los Lagos","CL-LL"),
("11","RegiÃ³n AisÃ©n del Gral. Carlos IbÃ¡Ã±ez del Campo","CL-AI"),
("12","RegiÃ³n de Magallanes y de la AntÃ¡rtica Chilena","CL-MA"),
("13","RegiÃ³n Metropolitana de Santiago","CL-RM"),
("14","RegiÃ³n de Los RÃ­os","CL-LR"),
("15","Arica y Parinacota","CL-AP")
]
        cursor.execute("TRUNCATE TABLE tbl_region_v2")
        start81=time.process_time() + start81
        a99=1
        b99=start81
        info99 = {
            'Iteracion': a99,
            'Hora' : b99,
        }
        with open('Data/Parte_3_Postgres_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info99)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqlpot = "INSERT INTO tbl_region_v2 (id, nombre, iso_3166_2_cl) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val1)):
            list.append(val1[i])
        cursor.executemany(sqlpot, list)
        conn.commit()

    else:
      with conn.cursor() as cursor:
        val3 = [("1","Arica","15"),
("2","Parinacota","15"),
("3","Iquique","1"),
("4","Tamarugal","1"),
("5","Antofagasta","2"),
("6","El Loa","2"),
("7","Tocopilla","2"),
("8","CopiapÃ³","3"),
("9","ChaÃ±aral","3"),
("10","Huasco","3"),
("11","Elqui","4"),
("12","Choapa","4"),
("13","LimarÃ­","4"),
("14","ValparaÃ­so","5"),
("15","Isla de Pascua","5"),
("16","Los Andes","5"),
("17","Petorca","5"),
("18","Quillota","5"),
("19","San Antonio","5"),
("20","San Felipe de Aconcagua","5"),
("21","Marga Marga","5"),
("22","Cachapoal","6"),
("23","Cardenal Caro","6"),
("24","Colchagua","6"),
("25","Talca","7"),
("26","Cauquenes","7"),
("27","CuricÃ³","7"),
("28","Linares","7"),
("29","ConcepciÃ³n","8"),
("30","Arauco","8"),
("31","BiobÃ­o","8"),
("32","Ã‘uble","8"),
("33","CautÃ­n","9"),
("34","Malleco","9"),
("35","Valdivia","14"),
("36","Ranco","14"),
("37","Llanquihue","10"),
("38","ChiloÃ©","10"),
("39","Osorno","10"),
("40","Palena","10"),
("41","Coihaique","11"),
("42","AisÃ©n","11"),
("43","CapitÃ¡n Prat","11"),
("44","General Carrera","11"),
("45","Magallanes","12"),
("46","AntÃ¡rtica Chilena","12"),
("47","Tierra del Fuego","12"),
("48","Ãšltima Esperanza","12"),
("49","Santiago","13"),
("50","Cordillera","13"),
("51","Chacabuco","13"),
("52","Maipo","13"),
("53","Melipilla","13"),
("54","Talagante","13")
]
        cursor.execute("TRUNCATE TABLE tbl_provincia_v2")
        start81=time.process_time() + start81
        a99=1
        b99=start81
        info99 = {
            'Iteracion': a99,
            'Hora' : b99,
        }
        with open('Data/Parte_3_Postgres_Test_3.csv', 'a', newline = '') as csv_file:
            fieldnames = ['Iteracion', 'Hora']
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writerow(info99)
            log_box3.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
            log_box3.see("end") 
            cut_duration = 0
            scan_interval = 1
            time.sleep(scan_interval)
        sqlpot = "INSERT INTO tbl_provincia_v2 (id, nombre, idregion) VALUES (%s, %s, %s)"
        list=[]
        for i in range(len(val3)):
            list.append(val3[i])
        cursor.executemany(sqlpot, list)
        conn.commit()

    log_box3.insert(tk.END, '***\nTerminado Test3***')
        


	
		
def TESTT2(log_box2,MySQL_db,mongoDB_collection,cnxn,conn):
    fieldnames1 = ['Iteracion', 'Hora']
    fieldnames = ['Iteracion', 'Hora']
    if not os.path.exists('Data/Parte_3_MySQLTest_2.csv'):
    
        with open('Data/Parte_3_MySQLTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte_3_MySQLTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/Parte_3_MongoTest_2.csv'):
    
        with open('Data/Parte_3_MongoTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_MongoTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    
    if not os.path.exists('Data/Parte_3_SQLServerTest_2.csv'):
    
        with open('Data/Parte_3_SQLServerTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_SQLServerTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/Parte_3_PostgresTest_2.csv'):
    
        with open('Data/Parte_3_PostgresTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_PostgresTest_2.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    global start3
    start3 = 0
    log_box2.insert(tk.END, ' TEST 2 MongoDB...')
    result=list(mongoDB_collection.find({'species': topic_str}))
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
        with open('Data/Parte_3_MongoTest_2.csv', 'a', newline = '') as csv_file:
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
        sql = "SELECT * FROM pokemones WHERE species=%s;"
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
            with open('Data/Parte_3_MySQLTest_2.csv', 'a', newline = '') as csv_file:
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
        sqls = "SELECT * FROM pokemon WHERE species=?;"
        cursor.execute(sqls, (topic_str,))
        resultx = cursor.fetchall()
        #print(len(resultx))
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
            with open('Data/Parte_3_SQLServerTest_2.csv', 'a', newline = '') as csv_file:
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
        sqls = 'select * from public."pokemones" where "species"=%s;'
        cursor.execute(sqls, (topic_str,))
        resultx = cursor.fetchall()
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
            with open('Data/Parte_3_PostgresTest_2.csv', 'a', newline = '') as csv_file:
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
    if not os.path.exists('Data/Parte_3_MySQLTest_1.csv'):
    
        with open('Data/Parte_3_MySQLTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte_3_MySQLTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()


    if not os.path.exists('Data/Parte_3_MongoTest_1.csv'):
    
        with open('Data/Parte_3_MongoTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_MongoTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    if not os.path.exists('Data/Parte_3_SQLServerTest_1.csv'):
    
        with open('Data/Parte_3_SQLServerTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()
    else:
        with open('Data/Parte_3_SQLServerTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames1)
            csv_writer.writeheader()

    
    if not os.path.exists('Data/Parte_3_PostgresTest_1.csv'):
    
        with open('Data/Parte_3_PostgresTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()
    else:
         with open('Data/Parte_3_PostgresTest_1.csv', 'w+', newline = '') as csv_file:
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            csv_writer.writeheader()

    global start
    log_box.insert(tk.END, ' TEST 1 MongoDB...')
    start = time.process_time()
    if(random==2):
        for num in range(random):
            if(not RUNNING1):
                break
            result = list(mongoDB_collection.provincias.aggregate([{'$lookup':{'from': "comuna",'localField': "id",'foreignField' : "idProvincia",'as': "provincia_comuna"}}]))

    else:
        for num in range(random):
            if(not RUNNING1):
                break
            result = list(mongoDB_collection.provincias.aggregate([{'$lookup':{'from': "comuna",'localField': "id",'foreignField' : "idProvincia",'as': "provincia_comuna"}},{'$lookup':{'from': "region",'localField': "idRegion",'foreignField' : "id",'as': "provincia_region"}}]))
    
    a=1
    b= start
    info1 = {
        'Iteracion': a,
        'Hora' : b,}
    with open('Data/Parte_3_MongoTest_1.csv', 'a', newline = '') as csv_file:
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
    if(random==2):
        with MySQL_db.cursor() as cursor:
            sql = "select * from tbl_comuna inner join tbl_provincia on tbl_comuna.idProvincia=tbl_provincia.id;"
            for num in range (random):    
                if(not RUNNING1):
                    break 
            cursor.execute(sql,)
            result = cursor.fetchall()
            
            

    else:
        with MySQL_db.cursor() as cursor:
            sql = """select * from tbl_provincia inner join tbl_comuna on tbl_provincia.id=tbl_comuna.idProvincia
						 inner join tbl_region on tbl_provincia.idRegion=tbl_region.id;"""
            for num in range (random):
                if(not RUNNING1):
                    break 
            cursor.execute(sql,)
            result = cursor.fetchall()
            
           
    a=1
    b=start1
    info = {
        'Iteracion': a,
        'Hora' : b,
    }
    with open('Data/Parte_3_MySQLTest_1.csv', 'a', newline = '') as csv_file:
        fieldnames = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        csv_writer.writerow(info)
        log_box.insert(tk.END, f"\n\n Iteracion: {a}, Hora: {b}")
        log_box.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)

    global start6
    
    start6=time.process_time()
    log_box.insert(tk.END, ' \nTEST 1 SQL Server...')
    if(random==2):
        with cnxn.cursor() as cursor:
            sqls = "select * from tbl_comuna inner join tbl_provincia on tbl_comuna.idProvincia=tbl_provincia.id;"
            for num in range (random):
                if(not RUNNING1):
                    break 
            cursor.execute(sqls,)
            result = cursor.fetchall()
           
            
    else:
        with cnxn.cursor() as cursor:
            sqls = """select * from tbl_provincia inner join tbl_comuna on tbl_provincia.id=tbl_comuna.idProvincia
						 inner join tbl_region on tbl_provincia.idRegion=tbl_region.id;"""
            for num in range (random):
                if(not RUNNING1):
                    break 
            cursor.execute(sqls,)
            result = cursor.fetchall()
            

    a2=1
    b2=start6
    info3 = {
        'Iteracion': a2,
        'Hora' : b2,
    }
    with open('Data/Parte_3_SQLServerTest_1.csv', 'a', newline = '') as csv_file:
        fieldnames = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        csv_writer.writerow(info3)
        log_box.insert(tk.END, f"\n\n Iteracion: {a2}, Hora: {b2}")
        log_box.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)

    
    global start99
    start99= time.process_time()
    log_box.insert(tk.END, ' \nTEST 1 Postgres...')
    if(random==2):
        with conn.cursor() as cursor:
            sql99 = 'select * from tbl_comuna inner join tbl_provincia on tbl_comuna.idProvincia=tbl_provincia.id;'
            for num99 in range (random):
                if(not RUNNING1):
                    break 
            cursor.execute(sql99,)
            result = cursor.fetchall()
            
            
    else:
        with conn.cursor() as cursor:
            sql99 = """select * from tbl_provincia inner join tbl_comuna on tbl_provincia.id=tbl_comuna.idProvincia
						 inner join tbl_region on tbl_provincia.idRegion=tbl_region.id;"""
            for num99 in range (random):
                if(not RUNNING1):
                    break 
            cursor.execute(sql99,)
            result = cursor.fetchall()
            
            

    a99=1
    b99=start99
    info99 = {
        'Iteracion': a99,
        'Hora' : b99,
    }
    with open('Data/Parte_3_PostgresTest_1.csv', 'a', newline = '') as csv_file:
        fieldnames = ['Iteracion', 'Hora']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        csv_writer.writerow(info99)
        log_box.insert(tk.END, f"\n\n Iteracion: {a99}, Hora: {b99}")
        log_box.see("end") 
        cut_duration = 0
        scan_interval = 1
        time.sleep(scan_interval)


    log_box.insert(tk.END, '***\nTerminado TEST 1***')

        
    
    
    
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

    data = pd.read_csv('Data/Parte_3_MySQLTest_1.csv', index_col = None)
    dataq = pd.read_csv('Data/Parte_3_MongoTest_1.csv', index_col = None)
    datay = pd.read_csv('Data/Parte_3_SQLServerTest_1.csv', index_col = None)
    dataz = pd.read_csv('Data/Parte_3_PostgresTest_1.csv', index_col = None)
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
    plt.title('Busqueda por cantidad numerica de datos')
    #plt.show()
    plt.savefig('Graphs/Test1.png', bbox_inches='tight', dpi = 300)
    GRAPH_LABEL()

def SHOW_GRAPH2():

    data = pd.read_csv('Data/Parte_3_MySQLTest_2.csv', index_col = None)
    dataq = pd.read_csv('Data/Parte_3_MongoTest_2.csv', index_col = None)
    datay = pd.read_csv('Data/Parte_3_SQLServerTest_2.csv', index_col = None)
    dataz = pd.read_csv('Data/Parte_3_PostgresTest_2.csv', index_col = None)
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
    data = pd.read_csv('Data/Parte_3_MySQL_Test_3.csv', index_col = None)
    dataq = pd.read_csv('Data/Parte_3_Mongo_Test_3.csv', index_col = None)
    datay = pd.read_csv('Data/Parte_3_SQLServerTest_3.csv', index_col = None)
    dataz = pd.read_csv('Data/Parte_3_Postgres_Test_3.csv', index_col = None)
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
    
            
def GUI3(MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3):
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
    value_list = ['2', '3']
    value_list2 = ['a','b','c']
    value_list3 = ['Comuna', 'Region', 'Provincia']




    packet_loss_label_2 = ttk.Label(column_1_div_1, text = '\nSeleccione el N° tablas a unir.', font=("Calibri"), justify = 'center')
    packet_loss_label_2.pack(side = 'top')

    #duration_entrybox = ttk.Entry(column_1_div_1)
    #duration_entrybox.pack(side = 'top')

    values_shared_combobox = ttk.Combobox(column_1_div_1)
    values_shared_combobox.pack(side = 'top')

    values_shared_combobox['values'] = value_list
    values_shared_combobox.set(value_list[0])

    packet_loss_label_22 = ttk.Label(column_2_div_1,text = '\nCantidad de datos a solicitar', font=("Calibri"), justify = 'center')
    packet_loss_label_22.pack(side = 'top')

    ##duration_entrybox1 = ttk.Entry(column_2_div_1)
    ##duration_entrybox1.pack(side = 'top')

    values_shared1_combobox = ttk.Combobox(column_2_div_1)
    values_shared1_combobox.pack(side = 'top')

    values_shared1_combobox['values'] = value_list2
    values_shared1_combobox.set(value_list2[0])

    packet_loss_label_23 = ttk.Label( column_3_div_1,text = '\nSeleccione el dataset a eliminar.', font=("Calibri"), justify = 'center')
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

    begin_button2 = ttk.Button(div_2_top_div_c3, text= 'Iniciar', command=lambda:(rand2(values_shared2_combobox),Test3(log_box3,MySQL_db,mongoDB_collection,cnxn,conn,mongoDB_collection_2,mongoDB_collection_3)))
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
    


