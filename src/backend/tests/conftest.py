# import pytest
# from flask.testing import FlaskClient
# from shopbridge import create_app
# from config import TestingConfig


# @pytest.fixture
# def client():
#     app = create_app(config_class=TestingConfig)
#     return app.test_client()

# @pytest.fixture
# def authenticated_client(client):
    
#     headers = {'Content-Type': 'application/json'}
#     data = {'email': 'testuser2', 'password': 'testpassword'}
#     response = client.post('/api/auth/register', headers=headers, json=data)
    

#     assert response.status_code == 201
#     access_token = response.json['access_token']

#     # Define headers to include token
#     # headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }

#     # Return a test client with headers set
    
#     client._set_headers(headers)
#     yield client