from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
def index():
    context = {'page_name': 'Главная'}
    return render_template('index.html', **context)


@app.route('/shoes/')
@app.route('/shoes.html/')
def shoes():
    _shoes = [{'title':'Черные кроссовки',
              'desc' : 'Отличные кроссы',
              'img':'shoes_pic1.jpg',
              'alt' : 'кеды'},
             ]
    context = {'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/clothing/')
@app.route('/clothing.html/')
def clothing():
    _clothing = [{'title':'Футболка',
              'desc' : 'Патриотическая футболка',
              'img':'clothing_pic1.jpeg',
              'alt' : 'футболка'},
             {'title': 'Штаны',
              'desc': 'Хаки штаны',
              'img': 'clothing_pic2.jpg',
              'alt': 'штаны'}
             ]
    context = {'clothing': _clothing}
    return render_template('clothing.html', **context)


@app.route('/jacket/')
@app.route('/jacket.html/')
def jacket():
    _jackets = [{'title':'Куртка',
              'desc' : 'Куртка зеленая',
              'img':'jacket_pic1.jpg',
              'alt' : 'куртка'}
             ]
    context = {'jackets': _jackets}
    return render_template('jacket.html', **context)


@app.route('/about/')
@app.route('/about.html/')
def about():
    context = {'page_name': 'О нас'}
    return render_template('about.html', **context)


@app.route('/contacts/')
@app.route('/contacts.html/')
def contacts():
    context = {'page_name': 'Контакты',
               'email': 'we@love.you',
               'site': 'we_love_you.com',
               'location': 'Moscow, Russia'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)