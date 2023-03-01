# Shopbridge App
Shopbridge is a simple inventory management system that allows users to add, edit, and delete items. This repository contains the instructions to set up the Shopbridge app using Docker.

## Flask APP
## Prerequisites
1. Docker installed on your machine

## Backend

1. Clone this repository

```
git clone https://github.com/your-username/shopbridge.git

```
2. Open your terminal and navigate to the root directory of the project.

3. Create a Docker container for the PostgreSQL database:

```

docker run --name db -e POSTGRES_DB=shopbridge_dev -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -v shopbridge-db-data:/var/lib/postgresql/data -p 5432:5432 -d postgres

```

4. Build the Flask app Docker image:

```
docker build -t flask-app .

```

5. Run the Flask app Docker container:

```
docker run -d --rm --name flask-web -p 8000:8000 --link db:db -w /app/backend flask-app
```

## React Installation

## Prerequisites
1. Install Node.js and npm.

## Instalation

1. Navigate to the frontend directory:

```
cd frontend
```


2. Install the dependencies:

```
npm install
```

3. Start the React app:

```
npm start
```

4. Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to view the Shopbridge app frontend.


## Note

Here is [Swagger Docs](https://app.swaggerhub.com/apis-docs/luisomar3/ShopBridge/1.0#/default/get_api_items__id_) for the flask API

Inside backend and frontend folder you will find specific instruction and docs, on the backend folder you can find the API docs.
License
This project is licensed under the [MIT License](https://opensource.org/license/mit/)