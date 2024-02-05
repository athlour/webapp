import jwt
import datetime
import base64
from flask import Flask, make_response, abort, request, jsonify

PRIVATE_KEY_SECRET ="ge6PvBAQfnc7CB2lVOkmyeMZnISINPAQ"

app = Flask(__name__)

def decode_credentials():
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    if auth_header and auth_header.startswith('Basic '):
        # Extract the base64-encoded part
        encoded_credentials = auth_header[len('Basic '):]
        # Decode the base64-encoded credentials
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        # Split the credentials into username and password
        username, password = credentials.split(':', 1)
        return {"username":username,"password":password}
    else:
        return "No Basic Auth credentials provided"


def verify_jwt_token(func):
    def wrapper(*args, **kwargs):
        # Get the JWT token from the cookie
        jwt_token = request.cookies.get('token')

        if jwt_token:
            try:
                # Verify the JWT token
                decoded_payload = jwt.decode(jwt_token, PRIVATE_KEY_SECRET, algorithms=['HS256'])
                # Attach the decoded payload to the request object for access in the route
                request.decoded_payload = decoded_payload
                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({"status": "error", "message": "Token has expired"})
            except jwt.InvalidTokenError:
                return jsonify({"status": "error", "message": "Invalid token"})
        else:
            return jsonify({"status": "error", "message": "JWT token not found in the cookie"})

    return wrapper




def get_jwt():
    username = decode_credentials()["username"]
    payload = {
        'user_id': 1,
        'username': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token expiration time
    }
    # Generate the JWT token
    jwt_token = jwt.encode(payload, PRIVATE_KEY_SECRET, algorithm='HS256')

    return jwt_token


@app.route('/login', methods=["POST"])
def login():
    jwt_token = get_jwt()
    if jwt_token is False:
        abort(401)
    else:
        response = make_response("",200)
        response.set_cookie('token', jwt_token, expires= datetime.datetime.now() + datetime.timedelta(hours=1), httponly=True, secure=True)
    return response,200


@app.route("/emp", methods=["GET"])
@verify_jwt_token
def employee():
    response_body = {
        "employee": {
        "id": 12345,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1 (555) 123-4567",
        "address": {
        "street": "123 Main Street",
        "city": "Anytown",
        "state": "CA",
        "zipCode": "12345"
        },
        "position": "Software Engineer",
        "department": "Engineering",
        "salary": 80000,
        "startDate": "2023-01-15",
        "isFullTime": "true",}
    }


    # Using make_response
    response = make_response(response_body)
    response.status_code = 200


    return response




if __name__=="__main__":
    app.run()