import os

from django.shortcuts import redirect
from flask import Flask, request, url_for, render_template
from werkzeug.utils import secure_filename, redirect
from loginform import LoginForm
import json


UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/load_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'''<!doctype html>
                        <html lang="ru">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css"
                                href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                        </head>
                        <body>
                            <div class="text-center">
                                <h1>Загрузка фотграфии</h1>
                                <h3>Для участия в миссии</h3>
                            </div>
                            <div>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                <label for="photo">Приложите фотографию</label>
                                <div class="form-group">
                                    <img src="{url_for('static', filename=f'img/{filename}')}" alt="Картинка пропала">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                    <input type=submit value='Загрузить'>
                                </div>
                            </form>
                            </div>
                        </body>
                        </html>'''
    return f'''<!doctype html>
            <html lang="ru">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                    crossorigin="anonymous">
                <link rel="stylesheet" type="text/css"
                    href="{url_for('static', filename='css/style.css')}"/>
                <title>Отбор астронавтов</title>
            </head>
            <body>
                <div class="text-center">
                    <h1>Загрузка фотграфии</h1>
                    <h3>Для участия в миссии</h3>
                </div>
                <div>
                <form class="login_form" method="post" enctype="multipart/form-data">
                    <div class="form-group">
                        <label for="photo">Приложите фотографию</label>
                        <input type="file" class="form-control-file" id="photo" name="file">
                        <input type=submit value='Загрузить'>
                    </div>
                </form>
                </div>
            </body>
            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
