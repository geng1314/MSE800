from datetime import datetime




def log_activity(func):

    def wrapper(*args, **kwargs):

        # Print function name and time  
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Execute the function
        result = func(*args, **kwargs)

        # Print completion status
        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper