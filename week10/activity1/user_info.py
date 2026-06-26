from datetime import date
from auth import load_db, save_db

DB_FILE = "users.json"

# 1. sign_in = signup: create new account (Full Name, DOB, email, password)
def sign_in(full_name: str, dob: str, email: str, password: str) -> bool:
    """Register a new user account with personal details and credentials."""
    db = load_db()
    if email in db:
        print("Email already registered, please log in instead")
        return False
    # Validate DOB format
    try:
        date.fromisoformat(dob)
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD (e.g. 1990-01-15)")
        return False
    # Create new user record
    db[email] = {
        "full_name": full_name,
        "date_of_birth": dob,
        "password": password,
        "reset_token": None,
        "token_expiry": None
    }
    save_db(db)
    print(f"Account created for {full_name}!")
    return True

# 2. info_edit: update Full Name or Date of Birth
def info_edit(email: str, new_name: str = None, new_dob: str = None) -> bool:
    """Update a user's personal profile details.

    Parameters:
        email: The email address for the account to update.
        new_name: Optional new full name.
        new_dob: Optional new date of birth in YYYY-MM-DD format.

    Returns:
        True if the profile was updated successfully, False otherwise.
    """
    db = load_db()
    if email not in db:
        print("Account not found")
        return False
    user = db[email]
    if new_name:
        user["full_name"] = new_name
    if new_dob:
        try:
            date.fromisoformat(new_dob)
            user["date_of_birth"] = new_dob
        except ValueError:
            print("Invalid DOB format, update cancelled")
            return False
    save_db(db)
    print("Profile information updated successfully")
    return True

# 3. get_user_info: fetch & display user personal data
def get_user_info(email: str) -> dict | None:
    """Retrieve and display a user's profile information.

    Parameters:
        email: The email address of the user.

    Returns:
        A dictionary with the user's public profile data or None if not found.
    """
    db = load_db()
    user = db.get(email)
    if not user:
        print("No user found")
        return None
    # Hide password for safety
    safe_data = {
        "Full Name": user["full_name"],
        "Date of Birth": user["date_of_birth"],
        "Email": email
    }
    print("\n=== Your Profile ===")
    for k, v in safe_data.items():
        print(f"{k}: {v}")
    return safe_data

# 4. cancel_account: delete user account entirely
def cancel_account(email: str) -> bool:
    """Delete a user account from the database.

    Parameters:
        email: The email address of the account to cancel.

    Returns:
        True if the account was deleted successfully, False otherwise.
    """
    db = load_db()
    if email not in db:
        print("Account does not exist")
        return False
    del db[email]
    save_db(db)
    print("Account permanently cancelled and data deleted")
    return True