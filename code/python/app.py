from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from dbconnector import DatabaseConnector

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        db = DatabaseConnector('localhost', 'root', '', 'flask')
        db.connect()
        password_hash = generate_password_hash(form.password.data)
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (form.username.data, form.email.data, password_hash)
        db.execute_query(query, values)
        db.close()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        db = DatabaseConnector('localhost', 'root', '', 'flask')
        db.connect()
        query = "SELECT * FROM users WHERE email = %s"
        values = (form.email.data,)
        result = db.execute_query(query, values)
        db.close()
        if result is not None:
            if check_password_hash(result[3], form.password.data):
                user = User(result[0], result[1], result[2])
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
