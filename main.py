from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import json
import os
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")  # change for production

# -----------------------------
# Email configuration (Replit/Render ready)
# -----------------------------
MAIL_USER = os.getenv("EMAIL_USER", "aayushpatilofficial@gmail.com")
MAIL_PASS = os.getenv("EMAIL_PASS", "")  # use App Password in production

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=MAIL_USER,
    MAIL_PASSWORD=MAIL_PASS,
    MAIL_DEFAULT_SENDER=MAIL_USER
)

mail = Mail(app)

# -----------------------------
# Data paths
# -----------------------------
DATA_DIR = "data"
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")
PORTFOLIO_FILE = os.path.join(DATA_DIR, "portfolio.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize files if missing
if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(PORTFOLIO_FILE):
    sample = [
        {"id": 1, "title": "Math Quiz App", "desc": "Interactive advanced math quizzes.", "tags": ["Flask", "AI", "Quiz"]},
        {"id": 2, "title": "HopePulse Prototype", "desc": "Wearable mental health demo.", "tags": ["Hardware", "ML"]}
    ]
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(sample, f, indent=2)

# -----------------------------
# Helpers
# -----------------------------
def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# Inject datetime globally into templates
@app.context_processor
def inject_now():
    return {"datetime": datetime}

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    portfolio = read_json(PORTFOLIO_FILE)
    return render_template("index.html", portfolio=portfolio)

@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(read_json(PORTFOLIO_FILE))

@app.route("/contact", methods=["POST"])
def contact():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip()
    message = form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill all required fields.", "error")
        return redirect(url_for("index") + "#contact")

    # Save to contacts.json
    entry = {"name": name, "email": email, "message": message, "time": datetime.utcnow().isoformat() + "Z"}
    contacts = read_json(CONTACTS_FILE)
    contacts.insert(0, entry)
    write_json(CONTACTS_FILE, contacts)

    # Send email safely
    try:
        msg = Message(
            subject=f"New Contact Form Submission from {name}",
            recipients=[MAIL_USER],  # your email
            body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("Thanks! Your message has been sent successfully.", "success")
    except Exception as e:
        print("Email send failed:", e)
        flash("Message saved, but email could not be sent.", "warning")

    return redirect(url_for("index") + "#contact")

# Contacts viewer (optional, remove in prod)
@app.route("/_contacts")
def _contacts():
    return jsonify(read_json(CONTACTS_FILE))

# -----------------------------
# Run server (dev) or use gunicorn in production
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
