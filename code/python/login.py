import mysql.connector
from loged import logedin
from dbconnector import DatabaseConnector

#Funktion zum Login des Mitarbeiters mit der Datenbank

def login():
    db_connector = DatabaseConnector("127.0.0.1", "root", "", "dbone")
    db_connector.connect()
 
    try:

        count = 0
        while not count == 3:

            username = input("Username: ")
            password = input("Passwort: ")


            sql = "SELECT * FROM Mitarbeiter m JOIN Credentials c ON m.MitarbeiterID = c.MitarbeiterID WHERE m.username = %s AND c.password = %s"
            values = (username, password)
            result = db_connector.execute_query(sql, values)

            if result:
                return logedin(username)
            else:
                count += 1
                print("Login fehlgeschlagen. Erneut versuchen! Versuch {} von 3".format(count))


        if count == 3:
            print("Zu viele Login versuche, Software wird beendet.")
            exit()

    except mysql.connector.Error as error:
        print("Fehler beim Verbinden zur Datenbank: {}".format(error))
        exit()

    finally:
        db_connector.close()