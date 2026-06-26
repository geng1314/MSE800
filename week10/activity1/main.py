from auth import login, logout, forget_password, reset_password
from user_info import sign_in, info_edit, get_user_info, cancel_account



def auth_menu():
    """Display the auth menu and perform the selected authentication action."""
    print("\n--- Auth Module ---")
    print("1. Login")
    print("2. Logout")
    print("3. Forgot Password (Get Reset Token)")
    print("4. Reset Password with Token")
    sub = input("Select auth action: ")
    if sub == "1":
        email = input("Email: ")
        pw = input("Password: ")
        login(email, pw)
    elif sub == "2":
        logout()
    elif sub == "3":
        email = input("Enter registered email for reset: ")
        forget_password(email)
    elif sub == "4":
        email = input("Email: ")
        token = input("Reset Token: ")
        new_pw = input("New Password: ")
        reset_password(email, token, new_pw)


def user_info_menu():
    """Display the user info menu and perform the selected action."""
    print("\n--- User Info Module ---")
    print("1. Sign Up (Create New Account)")
    print("2. Edit Personal Info (Name / DOB)")
    print("3. View My User Info")
    print("4. Cancel / Delete Account")
    sub = input("Select user info action: ")
    if sub == "1":
        name = input("Full Name: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        email = input("New Email: ")
        pw = input("New Password: ")
        sign_in(name, dob, email, pw)
    elif sub == "2":
        email = input("Your registered email: ")
        new_name = input("New Full Name (leave blank to keep old): ") or None
        new_dob = input("New DOB (YYYY-MM-DD, blank to keep old): ") or None
        info_edit(email, new_name, new_dob)
    elif sub == "3":
        email = input("Your email: ")
        get_user_info(email)
    elif sub == "4":
        email = input("Enter email to delete account: ")
        confirm = input("Type YES to confirm permanent delete: ").upper()
        if confirm == "YES":
            cancel_account(email)


def main():
    """Display the main menu and route user selections to the auth or user info module."""
    print("===== User Login & Signup System =====")

    while True:
        print("\n==== Main Menu ====")
        print("1. Auth Functions (Login / Logout / Forgot Password)")
        print("2. User Info Functions (Signup / Edit Profile / View Info / Delete Account)")
        print("0. Exit Program")
        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            auth_menu()
        elif main_choice == "2":
            user_info_menu()
        elif main_choice == "0":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid input, try again")

if __name__ == "__main__":
    main()