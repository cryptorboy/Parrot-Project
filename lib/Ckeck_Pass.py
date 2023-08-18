import re

def is_valid_password(password):
    # Define the password combination requirements using regular expressions
    # At least 8 characters
    # Contains at least one uppercase letter
    # Contains at least one lowercase letter
    # Contains at least one digit
    # Contains at least one special character from !@#$%^&*()
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$"

    # Check if the password matches the defined pattern
    if re.match(pattern, password):
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_valid_password("Pratik@21"))

