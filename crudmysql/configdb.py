#libreria para conexión a MySQL
import pymysql

#Método pra realizar la conexión a mysql
def get_connection():
    return pymysql.connect(host='localhost',user='root',password='',db='dbbibliotk')

