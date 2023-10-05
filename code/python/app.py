from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
from dbconnector import DatabaseConnector

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e899d4a5c8f35f32fe47edb9620d1b8b'


# Login und Registrierung
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db = DatabaseConnector('localhost', 'root', 'password', 'mydatabase')
        db.connect()
        db.insert_user(form.email.data, generate_password_hash(form.password.data))
        db.close()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db = DatabaseConnector('localhost', 'root', 'password', 'mydatabase')
        db.connect()
        user = db.get_user(form.email.data)
        db.close()
        if user is not None and check_password_hash(user['password'], form.password.data):
            login_user(UserMixin(user['id']), remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
