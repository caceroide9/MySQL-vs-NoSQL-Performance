import time
import sys
from pymongo import MongoClient
from MySQLdb import *

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
for i in range(9):
	random.append(int(f.readline()))

print(random)
# MySQL INT Type TEST
start = time.process_time()
start1 = time.time()

with MySQL_db.cursor() as cursor:
  sql = "SELECT id_pais, Nombre  FROM pais WHERE id_pais= %s;"
  for num in random:
    cursor.execute(sql, (num,))
    result = cursor.fetchall()
    print(result)
print("Tiempo tomado MySQL: ", time.process_time() - start)
print("소요시간 :", time.time() - start1)


#MongoDB int TEST
start = time.process_time()
start1 = time.time()
for num in random:
	result = list(mongoDB_collection.find({'id_pais': num}))
	print(result)
print("Tiempo tomado MongoDB :", time.process_time() - start) 
print("소요시간 :", time.time() - start1)




