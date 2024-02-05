import pytest
import requests
from flask import json
from app import app



@pytest.fixture
def base_url():
    return 'http://localhost:5000'  # Update the URL based on your Flask app's configuration

def test_login_endpoint(base_url):
    # Make a POST request to the /login endpoint
    response = requests.post(f'{base_url}/login', headers={'Authorization': 'Basic dmlub2loZXJvQGdtYWlsLmNvbTpBd2FyZW5lc3MxOTg4ITE='})

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the 'token' cookie is set in the response
    assert 'token' in response.cookies

