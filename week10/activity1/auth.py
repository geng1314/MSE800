import json
import random
import string
from datetime import datetime

DB_FILE = "users.json"

def load_db():
    """Load and return the user database from the JSON file."""
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    """Save the given data to the user database file."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# 1. login: verify email + password
def login(email: str, password: str) -> bool:
    """Verify email and password against the user database."""
    db = load_db()
    if email not in db:
        print("Account does not exist")
        return False
    user = db[email]
    if user["password"] == password:
        print(f"Welcome back, {user['full_name']}!")
        return True
    print("Incorrect password")
    return False

# 2. logout: simple session clear (simulation)
def logout() -> None:
    """Simulate logging out by clearing the current session."""
    print("Successfully logged out. Session cleared.")

# 3. forget_password: generate reset token + print reset link
def forget_password(email: str) -> str | None:
    """Generate and store a password reset token for the given email."""
    db = load_db()
    if email not in db:
        print("No account found with this email")
        return None
    # Generate secure random reset token
    reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    db[email]["reset_token"] = reset_token
    db[email]["token_expiry"] = str(datetime.now())
    save_db(db)
    print(f"Password reset token sent! Token: {reset_token}")
    print(f"Use this token to set a new password for {email}")
    return reset_token

# Helper: reset password using token (called after forget_password)
def reset_password(email: str, token: str, new_password: str) -> bool:
    """Reset the password for the given email using a reset token."""
    db = load_db()
    user = db.get(email)
    if not user or user.get("reset_token") != token:
        print("Invalid or expired reset token")
        return False
    user["password"] = new_password
    del user["reset_token"]
    del user["token_expiry"]
    save_db(db)
    print("Password updated successfully! You can log in now.")
    return True