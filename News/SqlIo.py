import mysql.connector
from   mysql.connector import Error

class SqlIo:
    def __init__(self, database, query, query2):
        self.DefInp(database)
        self.ConSql()
        self.ExeSql(query)
        self.ExeSql(query2)
    def DefInp(self, database):
        self.host = "localhost"
        self.user = "root"
        self.password = "JornautSQL2021!"
        self.database = database
        self.response = ""
    def ConSql(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            self.response += "MySQL Database to "+str(self.database)+" connection successful;"
        except Error as err:
            self.response += "Error: '{err}';"
    def ExeSql(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            self.response += "Query "+str(query)+" successful;"
            self.result = self.cursor.fetchall()
            self.connection.commit()
            self.response += " DB response is "+str(self.result)
        except Error as err:
            self.response += "Error: '{err}';"