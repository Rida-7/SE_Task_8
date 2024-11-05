
# def login(email, password):
#     # Dummy user data for testing
#     valid_email = "user@example.com"
#     valid_password = "password123"

#     if not email:
#         return "Email is required"
#     if not password:
#         return "Password is required"
#     if email != valid_email or password != valid_password:
#         return "Invalid credentials"
    
#     return "Login successful"
# src/login.py

# Simulated user database
user_db = {
    "user@example.com": "password123",
    "admin@example.com": "adminpass",
}

def login(email, password):
    if not email:
        return "Email is required"
    if not password:
        return "Password is required"
    if email not in user_db or user_db[email] != password:
        return "Invalid credentials"
    
    return "Login successful"

