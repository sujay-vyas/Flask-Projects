from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from App.models import User

auth_bp = Blueprint('auth', __name__ , template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        #passw = User.query.filter_by(password=password).first()
        if user and user.password == password:
            session['user'] = username
            flash('Login Successful!', 'success')
            return redirect(url_for('task.view_tasks'))
        else:
            flash('Invalid Credentials. Please try again.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))