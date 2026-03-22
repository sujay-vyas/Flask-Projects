from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from App import mydb
from App.models import Task, User

register_bp = Blueprint('register', __name__ , template_folder='templates')

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not password or not confirm_password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('register.register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register.register'))

        existing_user = mydb.session.execute(
            mydb.select(User).filter_by(username=username)
        ).scalar_one_or_none()

        if existing_user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register.register'))

        new_user = User(username=username, password=password)
        mydb.session.add(new_user)
        mydb.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')