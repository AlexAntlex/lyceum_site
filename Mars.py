import json

from django.shortcuts import redirect
from flask import Flask, render_template, url_for
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('prof.html', prof=prof, image_1=url_for('static', filename='img/image_2.png'),
                           image_2=url_for('static', filename='img/image_1.png'))


@app.route('/list_prof/<list>')
def list_prof(list):
    prof_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
                  'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите']
    return render_template('list_prof.html', list=list, prof_list=prof_list)


@app.route('/answer')
def news():
    with open("test.json", "rt", encoding="utf8") as f:
        anket_list = json.loads(f.read())
    return render_template('auto_answer.html', anket_list=anket_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    names = ["rnj", "wqef", "qwerty", "Plotva"]
    return render_template('distrib.html', names=names)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
