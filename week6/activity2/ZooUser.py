from ZooUserDecorators import log_activity



@log_activity
def login():

    # Global variable to show the username in the logout function
    global userName
    userName = input("Enter your username: ")
    print(f"{userName} , welcome!")


@log_activity
def logout(): 
    print(f"{userName} ,  see you next time.")  