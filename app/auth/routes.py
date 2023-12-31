from flask import Blueprint, redirect, render_template, request, url_for

from .forms import RegisterForm, LoginForm
from ..models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)

            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))
            

    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            user_name = form.username.data
            password = form.password.data

        return redirect(url_for('get_products'))

    return render_template('login.html', form=form)


