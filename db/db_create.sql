/*Creates Database "dbx" with Tables */

CREATE DATABASE IF NOT EXISTS dbx;
USE dbx;

CREATE TABLE IF NOT EXISTS credentials (
	CredID INT PRIMARY KEY AUTO_INCREMENT,	
    UserID INT,
    CredPW VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    UserFirstName VARCHAR(50),
    UserLastName VARCHAR(50),
    UserMode INT, /*Entscheided ob SelfPaced oder Begleitend*/
    UserType ENUM('admin','teacher','student') NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    TaskID INT PRIMARY KEY AUTO_INCREMENT,
    TaskType ENUM('own','delegated'),
    TaskDescription LONGTEXT,
    TaskState ENUM('done','in progress','open','') NOT NULL,
    AssignedTo INT NOT NULL
);


/*Settings Table hat nur einen Datensatz - Singleton*/
/*Idee: Nummernserienverwaltung
Idee: Aufgabenmodus - Lehrer verwaltet Aufgaben, Schüler verwaltet eigenständig Aufgaben.




 */
CREATE TABLE IF NOT EXISTS db_settings (
    SettingsID INT PRIMARY KEY /*Placeholder*/
);

/*Fremdschlüsselzuweisung*/

ALTER TABLE credentials
ADD CONSTRAINT FK_CREDENTIALS_USERS
FOREIGN KEY (UserID)
REFERENCES users (UserID);

ALTER TABLE tasks
ADD CONSTRAINT FK_TASKS_USERS
FOREIGN KEY (AssignedTo)
REFERENCES users (UserID);

/* AUTOINCREMENT FLUSH*/

ALTER TABLE credentials AUTO_INCREMENT = 0;




/* SQL-Query - Graveyard */

/*Tabelle 'usertype' obsolete da eigenes Feld in Users Tabelle*/
/*
CREATE TABLE IF NOT EXISTS usertype (
    UserTypeID SET ('admin','teacher','student') PRIMARY KEY NOT NULL,
    Description VARCHAR(50)
);
*/

/*OBSOLETE da eigenes Feld auf Users Tabelle*/
/*
ALTER TABLE users
ADD CONSTRAINT FK_USER_USERTYPE
FOREIGN KEY (UserType)
REFERENCES UserType (UserTypeID);
*/