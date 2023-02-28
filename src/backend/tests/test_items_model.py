import json

import pytest

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from config import TestingConfig
from shopbridge import db
from shopbridge.models.items import Item
from shopbridge.models.user import User
from shopbridge import create_app

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        user = User(email="test_user_12222222",password_hash="1234")
        # user_2 = User(email="test_user_chevere",password_hash="1234")
        db.session.add(user)
        db.session.commit()

        item = Item(name="Test item", description="This is a test item", price=10.0)
        db.session.add(item)
        db.session.commit()

        access_token = create_access_token(identity=user.id)
        
        # access_token_expired = create_access_token(identity=user_2.id,expires_delta=-10)
    
        test_data = {"token":access_token,"user_id":user.id,"item_id":item.id}
    yield app,test_data
    with app.app_context():
        db.drop_all()

# @pytest.fixture
# def new_item(app):
#     def _create_new_item(name, description, price):
#         with app.app_context():
#             item = Item(name=name, description=description, price=price)
#             db.session.add(item)
#             db.session.commit()
#             return item

#     yield _create_new_item

#     # Remove the created item after the test completes
#     with app.app_context():
#         db.session.rollback()
#         Item.query.delete()
#         db.session.commit()
        
def test_create_item(app):
    app, test_data = app
    client = app.test_client()
    response = client.post(
        "/api/items/",
        json={
            "name": "Test item",
            "description": "This is a test item",
            "price": 10.0,
        },
        headers={'Authorization':f'Bearer {test_data["token"]}'},
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id" in data
    assert "name" in data
    assert "description" in data
    assert "price" in data
    return data

def test_update_item(app):
    
    app, test_data = app
    client = app.test_client()

    response = client.put(
        f'/api/items/{test_data["item_id"]}',
        json={
            "name": "Updated test item",
            "description": "This is an updated test item",
            "price": 15.0,
        },
        headers={'Authorization':f'Bearer {test_data["token"]}'},
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Updated test item"
    assert data["description"] == "This is an updated test item"
    assert data["price"] == 15.0

def test_delete_item(app):
    
    app, test_data = app
    client = app.test_client()
    response = client.delete(f'/api/items/{test_data["item_id"]}', headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "message" in data

def test_list_items(app):
    test_create_item(app)
    instance,test_data = app
    client = instance.test_client()
    response = client.get("/api/items/", headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    test_create_item(app)
    response = client.get("/api/items/", headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 3
    
def test_get_item(app):
    instance,test_data = app
    client = instance.test_client()
    item_data = test_create_item(app)
    response = client.get(f'/api/items/{item_data["id"]}', headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Test item"
    assert data["description"] == "This is a test item"
    assert data["price"] == 10.0

def test_bulk_insert_items(app):

    instance,test_data = app
    client = instance.test_client()

    response = client.post(
        "/api/items/bulk",
        json=[
                {
                "name": "Test item 1",
                "description": "This is a test item 1",
                "price": 10.0,
                },
                {
                "name": "Test item 2",
                "description": "This is a test item 2",
                "price": 15.0,
                },
                ],
                headers={'Authorization':f'Bearer {test_data["token"]}'},
                )
    data = response.json
    assert response.status_code == 201
    assert data['message'] == '2 items inserted.'

def test_create_item_missing_data(app):
    
    instance,test_data = app
    client = instance.test_client()

    response = client.post("/api/items/", json={"name": "Test item", "price": 10.0},
                headers={'Authorization':f'Bearer {test_data["token"]}'},
                )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data

def test_update_item_not_found(app):
    instance,test_data = app
    client = instance.test_client()
    response = client.put(
    "/api/items/122",
    json={
    "name": "Updated test item",
    "description": "This is an updated test item",
    "price": 15.0,
    },
    headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 404
    data = json.loads(response.data)
    assert "error" in data

def test_get_item_not_found(app):
    instance,test_data = app
    client = instance.test_client()
    response = client.get("/api/items/1222", headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 404
    data = json.loads(response.data)
    assert "error" in data

def test_delete_item_not_found(app):
    instance,test_data = app
    client = instance.test_client()
    response = client.delete("/api/items/1222", headers={'Authorization':f'Bearer {test_data["token"]}'})
    assert response.status_code == 404
    data = json.loads(response.data)
    assert "error" in data

def test_missing_token(app):
    instance,test_data = app
    client = instance.test_client()
    response = client.get(
    "/api/items/",
    headers={"Content-Type":"application/json"})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data

#TODO: fix error with db
# def test_expired_token(app):
#     instance,test_data = app
#     client = instance.test_client()

#     response = client.post(
#     "/api/items/",
#     json={
#     "name": "Test item",
#     "description": "This is a test item",
#     "price": 10.0,
#     },
#     headers={"Authorization": f"Bearer {test_data['expired_token']}"},
#     )
#     assert response.status_code == 401
#     data = json.loads(response.data)
#     assert "message" in data
#     assert "Token has expired" in data["message"]




