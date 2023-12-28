from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените на свой секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Используется SQLite в качестве примера
db = SQLAlchemy(app)

# Модель для хранения данных о пользователях
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

# Форма регистрации
class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[InputRequired(), Length(min=2, max=50)])
    last_name = StringField('Фамилия', validators=[InputRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=6, max=256)])
    submit = SubmitField('Зарегистрироваться')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Хеширование пароля перед сохранением в базу данных
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация успешна!', 'success')
        return redirect(url_for('register'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблицы в базе данных при запуске приложения
    app.run(debug=True)
