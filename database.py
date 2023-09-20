import mysql.connector
class DataBase:
    def __init__(self):
        self._host = "HOST HERE"
        self._user = "USER HERE"
        self._passwd = "PASSWORD HERE"
        self._database = "DATABASE HERE"
        self.login = "LOGIN PASS HERE"

    def connect(self):  # connects to the database and returns the connection
        conn = mysql.connector.connect(
            host= self._host,
            user=self._user,
            passwd=self._passwd,
            database=self._database
        )
        return conn

    def close_conection(self, connection, cursor):  # commits the change and closes the cursor and db
        connection.commit()
        cursor.close()
        connection.close()