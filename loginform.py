from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])

    cap_name = StringField('id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])

    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')