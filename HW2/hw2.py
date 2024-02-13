from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Создание cookie-файла
        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)
        return resp

    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # Получение данных из cookie-файла
    name = request.cookies.get('name')
    email = request.cookies.get('email')

    if name and email:
        return render_template('welcome.html', name=name)

    return redirect('/')

@app.route('/logout')
def logout():
    # Удаление cookie-файла
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)