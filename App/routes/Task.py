from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from App import mydb
from App.models import Task
task_bp = Blueprint('task', __name__, template_folder='templates')

@task_bp.route('/')
def view_tasks():
    if 'user' not in session:
        flash('Please log in to view tasks.', 'warning')
        return redirect(url_for('auth.login'))

    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks) 

@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        flash('Please log in to add tasks.', 'warning')
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status="Pending")
        mydb.session.add(new_task)
        mydb.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty.', 'danger')

    return redirect(url_for('task.view_tasks'))

@task_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user' not in session:
        flash('Please log in to update tasks.', 'warning')
        return redirect(url_for('auth.login'))

    task = mydb.session.get(Task, task_id)
    if not task:
        flash('Task not found.', 'danger')
        return redirect(url_for('task.view_tasks'))
    if task.status == "Pending":
        task.status = "Working"
    elif task.status == "Working":
        task.status = "Completed"
    else:
        task.status = "Pending"
    mydb.session.commit()
    flash('Task updated successfully!', 'success')
    return redirect(url_for('task.view_tasks'))

@task_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user' not in session:
        flash('Please log in to delete tasks.', 'warning')
        return redirect(url_for('auth.login'))

    Task.query.delete()
    mydb.session.commit()
    flash('All tasks cleared successfully!', 'success')

    return redirect(url_for('task.view_tasks'))

@task_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        flash('Please log in to delete tasks.', 'warning')
        return redirect(url_for('auth.login'))

    task = mydb.session.get(Task, task_id)
    if not task:
        flash('Task not found.', 'danger')
        return redirect(url_for('task.view_tasks'))

    mydb.session.delete(task)
    mydb.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('task.view_tasks'))