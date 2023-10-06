/* Fills Database "dbx" with Table Data */
/* PWs encrypted in SHA256 */

USE dbx;

INSERT IGNORE INTO credentials (UserID, UserPW)
VALUES (1,'5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5');

INSERT IGNORE INTO users (UserID, UserFirstName, UserLastName, UserType)
VALUES (1,'Long','Johnson','admin');

INSERT 


/* SQL-QUERY GRAVEYARD*/ 
/*

INSERT IGNORE INTO UserType (UserTypeID, Description)
VALUES (1,'Prinzenrolle');

*/
/**/