from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
from dbconnector import DatabaseConnector

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    db = DatabaseConnector('localhost', 'root', '', 'flask')
    db.connect()
    query = "SELECT * FROM users WHERE id = %s"
    values = (user_id,)
    result = db.execute_query(query, values)
    db.close()
    if result:
        user = User()
        user.id = result[0]['id']
        user.username = result[0]['username']
        user.email = result[0]['email']
        user.password_hash = result[0]['password']
        return user
    else:
        return None
    
app.route('/login', methods=['GET', 'POST'])
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
        if result and check_password_hash(result[0]['password'], form.password.data):
            user = User()
            user.id = result[0]['id']
            user.username = result[0]['username']
            user.email = result[0]['email']
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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

@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
