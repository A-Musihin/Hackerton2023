/*Creates Database "dbx" with Tables */

CREATE DATABASE IF NOT EXISTS dbx;
USE dbx;

CREATE TABLE IF NOT EXISTS credentials (
	 CredID INT PRIMARY KEY AUTO_INCREMENT,	
    UserID INT,
    UserPW VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    UserFirstName VARCHAR(50),
    UserLastName VARCHAR(50),
    UserType SET('admin','teacher','student') NOT NULL
);

/*Tabelle 'usertype' obsolete da eigenes Feld in Users Tabelle*/
/*
CREATE TABLE IF NOT EXISTS usertype (
    UserTypeID SET ('admin','teacher','student') PRIMARY KEY NOT NULL,
    Description VARCHAR(50)
);
*/

/*Fremdschlüsselzuweisung*/

ALTER TABLE credentials
ADD CONSTRAINT FK_USER_CREDS
FOREIGN KEY (UserID)
REFERENCES users (UserID);

/*OBSOLETE da eigenes Feld auf Users Tabelle*/
/*
ALTER TABLE users
ADD CONSTRAINT FK_USER_USERTYPE
FOREIGN KEY (UserType)
REFERENCES UserType (UserTypeID);
*/