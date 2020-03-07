from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

