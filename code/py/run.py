from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route ('/')

def hello_world():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

@app.route('/add_text', methods=['POST'])
def add_text():
    if request.method == 'POST':
        text_input = request.form['text_input']

        # SQL-Befehl zum Einfügen des Texts in die Datenbank
        insert_query = "INSERT INTO deine_tabelle (text_spalte) VALUES (%s)"
        data = (text_input,)

        try:
            cursor.execute(insert_query, data)
            db.commit()
            return redirect(url_for('index'))  # Umleitung zur Startseite
        except Exception as e:
            db.rollback()
            return "Fehler beim Einfügen des Texts in die Datenbank: " + str(e)
