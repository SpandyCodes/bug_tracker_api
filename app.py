from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from config import Config

from models import db
from models.user import User
from models.bug import Bug

from routes.auth import auth_bp
from routes.bug_api import bug_api_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(bug_api_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/dashboard')
@login_required
def dashboard():
    bugs = Bug.query.all() if current_user.is_admin else Bug.query.filter_by(assigned_to=current_user.id).all()
    users = User.query.all() if current_user.is_admin else []
    return render_template('dashboard.html', bugs=bugs, users=users)

@app.route('/assign/<int:bug_id>', methods=['POST'])
@login_required
def assign_bug(bug_id):
    if not current_user.is_admin:
        abort(403)
    bug = Bug.query.get_or_404(bug_id)
    user_id = request.form.get("user_id")
    bug.assigned_to = int(user_id) if user_id else None
    db.session.commit()
    flash('Bug assignment updated.')
    return redirect(url_for('dashboard'))

@app.route('/bug/<int:bug_id>', methods=['GET', 'POST'])
@login_required
def bug_detail(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    if not current_user.is_admin and bug.assigned_to != current_user.id:
        abort(403)

    if request.method == 'POST':
        if current_user.is_admin:
            bug.title = request.form['title']
            bug.description = request.form['description']
            bug.severity = request.form['severity']
            bug.status = request.form['status']
        else:
            bug.progress = int(request.form['progress'])
            bug.comments = request.form['comments']

        db.session.commit()
        flash('Bug updated.')
        return redirect(url_for('dashboard'))

    return render_template('bug_detail.html', bug=bug)

if __name__ == '__main__':
    app.run(debug=True)