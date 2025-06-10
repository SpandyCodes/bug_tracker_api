from app import app, db
from models.user import User
from models.bug import Bug

def seed_data():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create users
    admin = User(username='admin', email='admin@example.com', is_admin=True)
    admin.set_password('admin123')

    alice = User(username='alice', email='alice@example.com')
    alice.set_password('alice123')

    bob = User(username='bob', email='bob@example.com')
    bob.set_password('bob123')

    carol = User(username='carol', email='carol@example.com')
    carol.set_password('carol123')

    users = [admin, alice, bob, carol]
    db.session.add_all(users)
    db.session.commit()

    # Create bugs
    bugs = [
        Bug(title="Login fails", description="User cannot log in", severity="High", assigned_to=alice.id),
        Bug(title="Navbar breaks", description="Navbar unresponsive on mobile", severity="Medium", assigned_to=bob.id),
        Bug(title="Crash on submit", description="Crash when submitting bug form", severity="High"),
        Bug(title="Typo in footer", description="Spelling mistake", severity="Low", assigned_to=carol.id)
    ]

    db.session.add_all(bugs)
    db.session.commit()
    print("✅ Database setup complete.")

if __name__ == '__main__':
    with app.app_context():
        seed_data()
