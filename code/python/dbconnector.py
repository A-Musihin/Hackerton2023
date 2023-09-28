import mysql.connector

#Klassen zum Verbinden mit der Datenbank und zum Ausführen von Queries 
class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as error:
            print("Fehler beim Verbinden zur Datenbank: {}".format(error))
            exit()

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        return result