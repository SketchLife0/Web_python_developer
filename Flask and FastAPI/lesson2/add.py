from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        email = request.form['email']

        # Создаем cookie
        response = make_response(redirect('/greet'))
        response.set_cookie('user_data', f'{name},{email}')

        return response

@app.route('/greet')
def greet():
    # Проверяем наличие cookie
    user_data_cookie = request.cookies.get('user_data')

    if user_data_cookie:
        # Разбираем cookie на данные пользователя
        name, email = user_data_cookie.split(',')
        return render_template('greet.html', name=name)
    else:
        # Если cookie отсутствует, перенаправляем на страницу ввода
        return redirect('/')

@app.route('/logout')
def logout():
    # Удаляем cookie и перенаправляем на страницу ввода
    response = make_response(redirect('/'))
    response.delete_cookie('user_data')
    return response

if __name__ == '__main__':
    app.run(debug=True)
