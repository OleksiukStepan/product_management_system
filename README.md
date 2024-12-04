
# Product Management System

This is a **FastAPI-based Product Management System** that provides CRUD operations for managing products and categories. The system is built with FastAPI, SQLAlchemy, Pydantic, and Alembic for database migrations.


## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Testing](#testing)
5. [API Endpoints](#api-endpoints)
6. [Postman Collection](#postman-collection)

## Features

- **Product Management**: Create, retrieve, update, and delete products.
- **Category Management**: Create, retrieve, update, and delete categories.
- **Inventory Tracking**: Track product quantities.
- **FastAPI Framework**: Provides fast and efficient implementation of RESTful API endpoints.
- **Database Migrations**: Alembic-powered migrations for managing schema changes.

## Technologies Used

- **FastAPI**: Backend framework for building APIs.
- **SQLAlchemy**: ORM for database interaction.
- **Pydantic**: Data validation and serialization.
- **Alembic**: Database migrations.
- **SQLite**: Lightweight database for development and testing.
- **Pytest**: Unit testing framework.


## Installation and Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/product_management_system.git
    cd product_management_system
    ```

2. **Set Up the Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Database Migrations:**
    ```bash
    alembic revision --autogenerate
    alembic upgrade head
    ```

5. **Start the Server:**
    ```bash
    uvicorn src.main:app --reload
    ```
   
6. **Access the API:** Open your browser and navigate to:
   - Docs: http://127.0.0.1:8000/docs
   - Redoc: http://127.0.0.1:8000/redoc

## Testing

**Run tests:**
```bash
PYTHONPATH=. pytest -v tests/
```

## API Endpoints

### Products
| Method | Endpoint                | Description                       |
|--------|-------------------------|-----------------------------------|
| POST   | `/products/`            | Create a new product             |
| GET    | `/products/`            | Retrieve all products            |
| GET    | `/products/{product_id}/` | Retrieve a specific product       |
| PUT    | `/products/{product_id}/` | Update a specific product         |
| DELETE | `/products/{product_id}/` | Delete a specific product         |

### Categories
| Method | Endpoint                               | Description                                |
|--------|---------------------------------------|--------------------------------------------|
| POST   | `/categories/`                        | Create a new category                     |
| GET    | `/categories/`                        | Retrieve all categories                   |
| GET    | `/categories/{category_id}/`          | Retrieve a specific category              |
| PUT    | `/categories/{category_id}/`          | Update a specific category                |
| DELETE | `/categories/{category_id}/`          | Delete a specific category                |


## Postman Collection

A Postman collection for testing the API is included in the repository. Import the collection from:
```
postman_collection.json
```
