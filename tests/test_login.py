import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from login import login  # This import will fail until the function is implemented

def test_login_valid():
    assert login("user@example.com", "password123") == "Login successful"

def test_login_invalid_email():
    assert login("invalidemail@example.com", "password123") == "Invalid credentials"

def test_login_invalid_password():
    assert login("user@example.com", "wrongpassword") == "Invalid credentials"

def test_login_empty_email():
    assert login("", "password123") == "Email is required"

def test_login_empty_password():
    assert login("user@example.com", "") == "Password is required"
