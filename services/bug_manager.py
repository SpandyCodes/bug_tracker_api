from models import db
from models.bug import Bug
from models.user import User

class BugManager:

    @staticmethod
    def create_bug(data):
        bug = Bug(
            title=data['title'],
            description=data.get('description', ''),
            severity=data['severity'],
            status=data.get('status', 'Open')
        )
        db.session.add(bug)
        db.session.commit()
        return bug

    @staticmethod
    def update_bug(bug_id, updates):
        bug = Bug.query.get_or_404(bug_id)
        bug.title = updates.get('title', bug.title)
        bug.description = updates.get('description', bug.description)
        bug.severity = updates.get('severity', bug.severity)
        bug.status = updates.get('status', bug.status)
        bug.progress = updates.get('progress', bug.progress)
        bug.comments = updates.get('comments', bug.comments)
        db.session.commit()
        return bug

    @staticmethod
    def assign_bug(bug_id, user_id):
        bug = Bug.query.get_or_404(bug_id)
        user = User.query.get_or_404(user_id)
        bug.assigned_to = user.id
        db.session.commit()
        return bug

    @staticmethod
    def delete_bug(bug_id):
        bug = Bug.query.get_or_404(bug_id)
        db.session.delete(bug)
        db.session.commit()
        return True
