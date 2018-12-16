from app import app
import models
from flask import render_template, redirect, request
from forms import UserForm


@app.route('/')
def index():
    users = models.Users.all()
    return render_template('index.html', data=users)
    # return "Hello World"


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = models.Users(username=form.username.data,
                            email=form.email.data, password=form.password.data)
        user.add()
        # return str(user)
        return redirect('/')
    else:
        return render_template('signup.html', form=form)
