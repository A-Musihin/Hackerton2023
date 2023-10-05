from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from dbconnector import DatabaseConnector


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        db = DatabaseConnector('localhost', 'root', 'password', 'mydatabase')
        db.connect()
        user = db.get_user(self.email.data)
        db.close()

        if user is None or user['password'] != self.password.data:
            self.email.errors.append('Invalid email or password')
            return False

        return True


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate(self):
        if not super(RegistrationForm, self).validate():
            return False

        db = DatabaseConnector('localhost', 'root', 'password', 'mydatabase')
        db.connect()
        user = db.get_user(self.email.data)
        if user is not None:
            self.email.errors.append('Email already registered')
            db.close()
            return False

        db.insert_user(self.email.data, self.password.data)
        db.close()

        return True