import pytest
from flask import json
from app import app


@pytest.fixture
def test_client():
    # This fixture starts the Flask app for testing
    with app.test_client() as client:
        yield client


def test_login_endpoint(test_client):
    # Use the test_client fixture to make requests to the Flask app
    response = test_client.post('/login',
                                headers={'Authorization': 'Basic dmlub2loZXJvQGdtYWlsLmNvbTpBd2FyZW5lc3MxOTg4ITE='})

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Extract cookies from the response headers

    print (response.headers)

    print(dir(response.headers))
    values = [x for x in response.headers.values()]
    cookie_token = values[2].split("=")
    assert 'token' in cookie_token





    # Check if the 'token' cookie is set in the response

