from flask import Blueprint, render_template
from .forms import RegisterForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/register')
def register():
    form = RegisterForm()



    return render_template('register.html', form=form)