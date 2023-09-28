from flask import Flask, render_template, request, redirect, url_for
frome flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, username, email)
        self.id = id
        self.username = username
        self.email = email

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(1, username, email)

        user.password_hash = generate_password_hash(password)

        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.session.query(User).filter(User.username == username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        
        return render_template('login.html')

    return render_template('login.html')        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
