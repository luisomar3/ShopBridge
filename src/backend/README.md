# Shopbridge Flask App

Shopbridge is a web application that allows users to manage their inventory, add products, update, and delete them. This is a Flask app that uses JWT for user authentication and PostgreSQL as a database.

## Installation

1. Create a virtual environment and activate it:
    - `python3 -m venv env`
    - `source env/bin/activate`
2. Install the dependencies using `pip install -r requirements.txt`.
3. Create a PostgreSQL database using `createdb <database-name>`.
4. In the project directory, create a `.env` file and add the following variables:
    ```
    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=<your-secret-key>
    DATABASE_URL=postgresql://localhost/<database-name>
    ```
5. Run the database migrations using `flask db upgrade`.
6. Start the application using `flask run`.

## Configuration

The following environment variables can be used to configure the application:

| Environment Variable       | Description                                                            |
|----------------------------|------------------------------------------------------------------------|
| FLASK_APP                  | The name of the Flask application.                                      |
| FLASK_ENV                  | The environment in which the application is running.                   |
| SECRET_KEY                 | The secret key used for encrypting data.                                |
| DATABASE_URL               | The URL for the PostgreSQL database.                                    |
| JWT_ACCESS_TOKEN_EXPIRES   | The time in seconds for the access token to expire.                     |
| JWT_REFRESH_TOKEN_EXPIRES  | The time in seconds for the refresh token to expire.                    |
| JWT_BLACKLIST_ENABLED      | Boolean value to enable/disable token revocation.                       |
| JWT_BLACKLIST_TOKEN_CHECKS | The token checks that are performed when revoking tokens.               |


## API Reference
-------------

The API of the Shopbridge application is RESTful and uses JSON for data exchange. Here are the available endpoints:

| Method | Endpoint | Description | Requires Authentication |
| ------ | -------- | ----------- | ------------------------|
| POST   | /api/auth/register | Register a new user. | No |
| POST   | /api/auth/login | Login as an existing user. | No |
| DELETE | /api/auth/logout | Logout the current user. | Yes |
| POST   | /api/auth/refresh | Refresh the access token of the current user. | Yes |
| GET    | /api/items | Get a list of all items. | No |
| GET    | /api/items/<int:id> | Get a item by ID. | No |
| POST   | /api/items | Create a new item. | Yes |
| PUT    | /api/items/<int:id> | Update a item by ID. | Yes |
| DELETE | /api/items/<int:id> | Delete a item by ID. | Yes |


## Attributes

The Shopbridge Flask app has the following attributes:

- User authentication using JWT.
- Token revocation using a blacklist.
- PostgreSQL database for storing data.
- RESTful API endpoints for managing products.
- Flask-Migrate for handling database migrations.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).