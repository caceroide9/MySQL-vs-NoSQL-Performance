import time
import sys
from pymongo import MongoClient
from MySQLdb import *
import csv

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

  

print("Primer TEST busqueda de datos por indice numerico")
# MySQL INT Type TEST
start = time.process_time()
start1 = time.time()

with MySQL_db.cursor() as cursor:
  sql = "SELECT id_pais, Nombre  FROM pais WHERE id_pais= %s;"
  for num in random:
    cursor.execute(sql, (num,))
    result = cursor.fetchall()
    info = {
            'Resultado' : num,
            'Hora' : time.process_time() - start
            }
    
    print(result)
    
print("Tiempo tomado MySQL: ", time.process_time() - start)
fieldnames = ['Iteracion','Hora']
with open('Data/ping_data.csv', 'a', newline = '') as csv_file:
  csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
  csv_writer.writerow(info)





#MongoDB int TEST
start = time.process_time()
start1 = time.time()
for num in random:
	result = list(mongoDB_collection.find({'id_pais': num}))
	print(result)
print("Tiempo tomado MongoDB :", time.process_time() - start) 


print("Segundo Test busqueda de indice texto")

topic_str = "Chile"
# MySQL String(Equal) Type TEST
start = time.time()
with MySQL_db.cursor() as cursor:
  sql = "SELECT Nombre FROM pais WHERE Nombre=%s;"
  print("MySQL string(Equal) TEST")
  cursor.execute(sql, (topic_str,))
  result = cursor.fetchall()
print("소요시간 : ", time.time() - start)


#MongoDB string(Equal) TEST
start = time.time()
print("MongoDB string(Equal) TEST")
result = list(mongoDB_collection.find({'Nombre': topic_str}))
print("소요시간 :", time.time() - start)


topic = {"ni","le"}
#MySQL string(NOINDEX) TEST
start = time.time()
with MySQL_db.cursor() as cursor:
	sql = "SELECT count(*) AS cnt FROM pais WHERE Nombre LIKE %s"
	print("MySQL string(NOINDEX) TEST")
	for topic_one in topic:
		temp_topic = '%' + topic_one + '%'
		cursor.execute(sql, (temp_topic,))
		result = cursor.fetchone()
		print(topic_one,'의 갯수: ', result['cnt'])
print("소요시간 :", time.time() - start)


##Agregar el contar abajo si es necesario

#MongoDB string(NOINDEX) TEST
start = time.time()
print("MongoDB string(NOINDEX INDEX) TEST")
for topic_one in topic:
	result = mongoDB_collection.find({"Nombre": {'$regex': topic_one}})


	print(topic_one,'의 갯수: ', result)
print("소요시간 :", time.time() - start)