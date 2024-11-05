import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from unittest.mock import Mock
from login_mock import login_mock

def test_login_with_mock():
    # Create a mock database
    mock_database = Mock()
    
    # Set up the mock to return a predefined user
    mock_database.find_user.return_value = {"username": "user", "password": "password"}

    # Call the login function with the mock database
    result = login_mock("user", "password", mock_database)
    
    # Check if the result is True (or the expected success message)
    assert result == True
