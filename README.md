# 🐞 Bug Tracker WebApp

A role-based Bug Tracker built with **Flask**, featuring:
- Object-Oriented Models (User, Bug)
- Authentication (Register/Login/Logout)
- Admin/User dashboards
- Bug tracking with status, severity, progress, and comments
- REST API for bugs
- Assign/unassign bugs (admin)
- Responsive Bootstrap UI with filters
- Ready for Vercel deployment

---

## 🚀 Features

### 👤 Roles
- **Admin**: Manage all bugs, assign users, view full system.
- **User**: See only assigned bugs, update progress, comment.

### 🐞 Bug Fields
- Title, Description
- Severity: Low / Medium / High
- Status: Open / In Progress / Done
- Progress: 0-100%
- Comments
- Assigned To: user (nullable)

### 🔐 Auth
- Register, Login, Logout with Flask-Login
- Passwords hashed using Werkzeug

---

## 🧱 Tech Stack

- Flask + Flask-SQLAlchemy
- Flask-Login
- Bootstrap 5
- SQLite
- Jinja2
- JavaScript (filtering)
- Vercel-compatible

---

## 🗂️ Directory Structure

```
bug_tracker/
├── app.py
├── config.py
├── setup_db.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── bug.py
├── routes/
│   ├── auth.py
│   └── bug_api.py
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── bug_detail.html
├── static/
│   ├── style.css
│   └── script.js
├── tests/
│   ├── test_auth.py
│   └── test_bug_api.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

## ✅ Local Setup

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/bug_tracker.git
cd bug_tracker

# Create and activate virtual env
python -m venv env
source env/bin/activate       # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Setup DB with sample data
python setup_db.py

# Run the app
python app.py
```

---

## 🌐 Deployment (Vercel)

Create `vercel.json`:

```json
{
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "app.py" }]
}
```

Then:
- Push to GitHub
- Import repo in [vercel.com](https://vercel.com)
- Deploy as Python serverless app

---

## 🧪 Tests

Run tests with `pytest`:

```bash
pytest tests/
```

---

## 🧑 Authors & License

MIT License © 2025 — [Your Name]