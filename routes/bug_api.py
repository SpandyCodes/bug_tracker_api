# routes/bug_api.py
from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from services.bug_manager import BugManager
from models.bug import Bug

bug_api_bp = Blueprint('bug_api', __name__, url_prefix='/api')

@bug_api_bp.route('/bugs', methods=['GET'])
@login_required
def list_bugs():
    bugs = Bug.query.all() if current_user.is_admin else Bug.query.filter_by(assigned_to=current_user.id).all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "description": b.description,
        "severity": b.severity,
        "status": b.status,
        "progress": b.progress,
        "comments": b.comments,
        "assigned_to": b.assigned_to
    } for b in bugs])

@bug_api_bp.route('/bugs/<int:bug_id>', methods=['GET'])
@login_required
def get_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    if not current_user.is_admin and bug.assigned_to != current_user.id:
        abort(403)
    return jsonify({
        "id": bug.id,
        "title": bug.title,
        "description": bug.description,
        "severity": bug.severity,
        "status": bug.status,
        "progress": bug.progress,
        "comments": bug.comments,
        "assigned_to": bug.assigned_to
    })

@bug_api_bp.route('/bugs', methods=['POST'])
@login_required
def create_bug():
    if not current_user.is_admin:
        abort(403)
    data = request.get_json()
    bug = BugManager.create_bug(data)
    return jsonify({"message": "Bug created", "id": bug.id}), 201

@bug_api_bp.route('/bugs/<int:bug_id>', methods=['PUT'])
@login_required
def update_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    if not current_user.is_admin and bug.assigned_to != current_user.id:
        abort(403)
    data = request.get_json()
    BugManager.update_bug(bug_id, data)
    return jsonify({"message": "Bug updated"})

@bug_api_bp.route('/bugs/<int:bug_id>', methods=['DELETE'])
@login_required
def delete_bug(bug_id):
    if not current_user.is_admin:
        abort(403)
    BugManager.delete_bug(bug_id)
    return jsonify({"message": "Bug deleted"})

@bug_api_bp.route('/assign/<int:bug_id>', methods=['POST'])
@login_required
def assign_bug_api(bug_id):
    if not current_user.is_admin:
        abort(403)
    user_id = request.json.get("user_id")
    BugManager.assign_bug(bug_id, user_id)
    return jsonify({"message": "Bug assigned"})
