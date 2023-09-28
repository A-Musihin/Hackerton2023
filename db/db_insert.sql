/* Fills Database "dbx" with Table Data */
/* PWs encrypted in SHA256 */

USE dbx;

INSERT IGNORE INTO Credentials (UserID, UserPW)
VALUES (1,'5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5');

INSERT IGNORE INTO User (UserID, UserFirstName, UserLastName, UserType)
VALUES (1,'Long','Johnson','admin');

INSERT IGNORE INTO UserType (UserTypeID, Description)
VALUES (1,'Prinzenrolle');

