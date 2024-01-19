from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    # Сохраните данные о посещении страницы
    request.user.message_set.create(message="Главная страница посещена")

    html = """
        <html>
            <head>
                <title>Главная страница</title>
            </head>
            <body>
                <h1>Привет, это моя первая страница Django!</h1>
            </body>
        </html>
    """
    return HttpResponse(html)

@login_required
def about(request):
    # Сохраните данные о посещении страницы
    request.user.message_set.create(message="Страница \"О себе\" посещена")

    html = """
        <html>
            <head>
                <title>О себе</title>
            </head>
            <body>
                <h1>Меня зовут Bard, я большой языковой модель от Google AI.</h1>
                <p>Я еще нахожусь в разработке, но я уже могу делать многое, например:</p>
                <ul>
                    <li>Я могу генерировать текст, переводить языки, писать разные виды творческого контента и отвечать на ваши вопросы информативным образом.</li>
                    <li>Я учусь на огромном наборе данных текстов и кода, и я постоянно совершенствуюсь.</li>
                </ul>
            </body>
        </html>
    """
    return HttpResponse(html)