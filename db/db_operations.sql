use dbx;

SELECT * from tasks
WHERE TaskState='open' AND TaskState='in progress';

/*Schüler fügt neuen Task zu seiner Zuweisung hinzu. Der Status ist beim Einfügen immer 'open'*/
USE dbx;
INSERT INTO tasks (TaskDescription,AssignedTo,TaskState) VALUES
('%1',%2,'open'); /*%1 Aufgabenbeschreibung , %2 UserID des Schülers*/
COMMIT;

/*Schüler löscht Aufgabe aus seiner Aufgabenliste*/
USE dbx;
DELETE FROM tasks WHERE TaskID=%1 AND AssignedTo=%2; /*%1 Aufgabennummer die übergeben werden sollte %2 UserID des Schülers*/
COMMIT;

USE dbx;
