# # src/login.py

# def login_mock(username, password, database):
#     if not username:
#         return "Username is required"
#     if not password:
#         return "Password is required"

#     user = database.find_user(username)

#     if user is None or user['password'] != password:
#         return "Invalid credentials"
    
#     return True  # Return True for successful login

# src/login.py

# src/login.py

def login_mock(username, password, database):
    # Check for required fields
    if not username or not password:
        return False  # Uniform False for invalid login attempts

    # Query the database for the user
    user = database.find_user(username)

    # Validate the retrieved user's password
    return user is not None and user["password"] == password

