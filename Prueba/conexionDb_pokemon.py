import mysql.connector

class Registro_datos_Pok():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='paises', 
                                            user = 'root',
                                            password ='LS9lm10N11')
    
    def inserta_productoPO(self,pk_id, artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, mode, acousticness, instrumentalness, liveness, valence, tempo, genre):
        cur = self.conexion.cursor()
        sql='''INSERT INTO `Spotify` (`pk_id`, `artist`, `song`, `duration_ms`, `explicit`, `year`, `popularity`, `danceability`, `energy`, `key`, `mode`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `genre`) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(pk_id, artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, mode, acousticness, instrumentalness, liveness, valence, tempo, genre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def buscar_productosPO(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Spotify " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_productoPO(self, pk_id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Spotify WHERE pk_id = {}".format(pk_id)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productosPO(self,pk_id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM Spotify WHERE pk_id = {}'''.format(pk_id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a   

    def actualiza_productosPo(self, pk_id, artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, mode, acousticness, instrumentalness, liveness, valence, tempo, genre):
        cur = self.conexion.cursor()
        sql ='''UPDATE Spotify SET  pk_id =' {}' , artist = '{}', song = '{}', duration_ms = '{}', explicit = '{}', year = '{}', popularity = '{}', danceability = '{}', energy = '{}', key = '{}', mode = '{}', acousticness = '{}', instrumentalness = '{}', liveness = '{}', valence = '{}', tempo = '{}', genre = '{}'
        WHERE pk_number = '{}' '''.format(pk_id, artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, mode, acousticness, instrumentalness, liveness, valence, tempo, genre)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  