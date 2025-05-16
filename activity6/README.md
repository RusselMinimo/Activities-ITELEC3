# ITELEC3 Activity 6 - CRUD API

This project implements a CRUD (Create, Read, Update, Delete) API using Django REST Framework. It consists of three models with authentication for all endpoints.

## Table of Contents
- [Installation](#installation)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Categories](#categories)
  - [Products](#products)
  - [Customers](#customers)
- [Error Handling](#error-handling)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd activity6
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

## Authentication

All API endpoints require authentication. The API supports token-based authentication.

To obtain a token:

```
POST /api/api-token-auth/

Request Body:
{
    "username": "your_username",
    "password": "your_password"
}

Response:
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

Include the token in all API requests:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

## API Endpoints

### Categories

#### List all categories
```
GET /api/categories/

Response:
[
    {
        "id": 1,
        "name": "Electronics",
        "description": "Electronic devices and accessories",
        "created_at": "2023-10-15T10:30:00Z",
        "updated_at": "2023-10-15T10:30:00Z",
        "is_active": true
    },
    ...
]
```

#### Get a specific category
```
GET /api/categories/{id}/

Response:
{
    "id": 1,
    "name": "Electronics",
    "description": "Electronic devices and accessories",
    "created_at": "2023-10-15T10:30:00Z",
    "updated_at": "2023-10-15T10:30:00Z",
    "is_active": true
}
```

#### Create a category
```
POST /api/categories/

Request Body:
{
    "name": "Books",
    "description": "Books and literature",
    "is_active": true
}

Response:
{
    "id": 2,
    "name": "Books",
    "description": "Books and literature",
    "created_at": "2023-10-15T11:00:00Z",
    "updated_at": "2023-10-15T11:00:00Z",
    "is_active": true
}
```

#### Update a category
```
PUT /api/categories/{id}/

Request Body:
{
    "name": "Books",
    "description": "Books, e-books and audiobooks",
    "is_active": true
}

Response:
{
    "id": 2,
    "name": "Books",
    "description": "Books, e-books and audiobooks",
    "created_at": "2023-10-15T11:00:00Z",
    "updated_at": "2023-10-15T11:30:00Z",
    "is_active": true
}
```

#### Delete a category
```
DELETE /api/categories/{id}/

Response:
204 No Content
```

### Products

#### List all products
```
GET /api/products/

Response:
[
    {
        "id": 1,
        "name": "Smartphone",
        "description": "Latest smartphone model",
        "price": "999.99",
        "category": 1,
        "stock": 50,
        "created_at": "2023-10-15T10:30:00Z",
        "updated_at": "2023-10-15T10:30:00Z",
        "is_available": true
    },
    ...
]
```

#### Get a specific product
```
GET /api/products/{id}/

Response:
{
    "id": 1,
    "name": "Smartphone",
    "description": "Latest smartphone model",
    "price": "999.99",
    "category": 1,
    "stock": 50,
    "created_at": "2023-10-15T10:30:00Z",
    "updated_at": "2023-10-15T10:30:00Z",
    "is_available": true
}
```

#### Create a product
```
POST /api/products/

Request Body:
{
    "name": "Laptop",
    "description": "Powerful laptop for professionals",
    "price": "1499.99",
    "category": 1,
    "stock": 25,
    "is_available": true
}

Response:
{
    "id": 2,
    "name": "Laptop",
    "description": "Powerful laptop for professionals",
    "price": "1499.99",
    "category": 1,
    "stock": 25,
    "created_at": "2023-10-15T11:30:00Z",
    "updated_at": "2023-10-15T11:30:00Z",
    "is_available": true
}
```

#### Update a product
```
PUT /api/products/{id}/

Request Body:
{
    "name": "Laptop",
    "description": "Ultra-powerful laptop for professionals",
    "price": "1599.99",
    "category": 1,
    "stock": 20,
    "is_available": true
}

Response:
{
    "id": 2,
    "name": "Laptop",
    "description": "Ultra-powerful laptop for professionals",
    "price": "1599.99",
    "category": 1,
    "stock": 20,
    "created_at": "2023-10-15T11:30:00Z",
    "updated_at": "2023-10-15T12:00:00Z",
    "is_available": true
}
```

#### Delete a product
```
DELETE /api/products/{id}/

Response:
204 No Content
```

### Customers

#### List all customers
```
GET /api/customers/

Response:
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main St, City",
        "created_at": "2023-10-15T10:30:00Z",
        "updated_at": "2023-10-15T10:30:00Z",
        "is_active": true
    },
    ...
]
```

#### Get a specific customer
```
GET /api/customers/{id}/

Response:
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "address": "123 Main St, City",
    "created_at": "2023-10-15T10:30:00Z",
    "updated_at": "2023-10-15T10:30:00Z",
    "is_active": true
}
```

#### Create a customer
```
POST /api/customers/

Request Body:
{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone": "+0987654321",
    "address": "456 Oak St, Town",
    "is_active": true
}

Response:
{
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone": "+0987654321",
    "address": "456 Oak St, Town",
    "created_at": "2023-10-15T12:00:00Z",
    "updated_at": "2023-10-15T12:00:00Z",
    "is_active": true
}
```

#### Update a customer
```
PUT /api/customers/{id}/

Request Body:
{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone": "+1987654321",
    "address": "789 Pine St, Village",
    "is_active": true
}

Response:
{
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone": "+1987654321",
    "address": "789 Pine St, Village",
    "created_at": "2023-10-15T12:00:00Z",
    "updated_at": "2023-10-15T12:30:00Z",
    "is_active": true
}
```

#### Delete a customer
```
DELETE /api/customers/{id}/

Response:
204 No Content
```

## Error Handling

### Authentication Errors
```
401 Unauthorized

{
    "detail": "Authentication credentials were not provided."
}
```

### Invalid Credentials
```
400 Bad Request

{
    "non_field_errors": ["Unable to log in with provided credentials."]
}
```

### Validation Errors
```
400 Bad Request

{
    "field_name": ["Error message for the field."]
}
```

### Not Found
```
404 Not Found

{
    "detail": "Not found."
}
``` 