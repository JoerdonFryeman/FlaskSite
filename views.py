from script import *
from urls import urlpatterns
from flask import render_template, request, flash


@app.route(urlpatterns['index'])
def index():
    context = get_db_objects(urlpatterns['index'])
    return render_template('index.html', title=context[0], content=context[1])


@app.route(urlpatterns['about'])
def about():
    context = get_db_objects(urlpatterns['about'])
    return render_template('about.html', title=context[0], content=context[1])


@app.route(urlpatterns['contact'], methods=['POST', 'GET'])
def contact():
    context = get_db_objects(urlpatterns['contact'])
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено!')
        else:
            flash('Пожалуйста, заполните это поле...')
    return render_template('contact.html', title=context[0])


@app.route(urlpatterns['terms'])
def terms():
    context = get_db_objects(urlpatterns['terms'])
    return render_template('terms.html', title=context[0], content=context[1])


@app.route(urlpatterns['privacy'])
def privacy():
    context = get_db_objects(urlpatterns['privacy'])
    return render_template('privacy.html', title=context[0], content=context[1])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title='Страница не найдена! Ошибка 404...')


if __name__ == "__main__":
    app.run()
