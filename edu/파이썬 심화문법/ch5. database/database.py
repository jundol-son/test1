import psycopg2
DB_Name = 'test1'
User_Name = 'postgres'
Password = 's5764191**'
Table_Name = '시가평가액'
Host_IP = '127.0.0.1'
Port_num = '5432'
class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host=Host_IP,dbname=DB_Name,user=User_Name,password=Password,port=Port_num)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()