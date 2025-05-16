# Student Management System API

This is a Django REST API for managing students, courses, and enrollments. The API implements CRUD operations for all models and requires authentication for all endpoints.

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
- Windows: `.\venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

All endpoints require authentication. You can use Basic Auth or Session Authentication.

### Students

#### List all students
- **Method**: GET
- **URL**: `/api/students/`
- **Headers**: 
  - `Authorization: Basic <credentials>` or Session Cookie
- **Response**: 
```json
[
    {
        "id": 1,
        "student_id": "2024001",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "date_of_birth": "2000-01-01",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
]
```

#### Create student
- **Method**: POST
- **URL**: `/api/students/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
  - `Content-Type: application/json`
- **Request Body**:
```json
{
    "student_id": "2024001",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "date_of_birth": "2000-01-01"
}
```

#### Get single student
- **Method**: GET
- **URL**: `/api/students/{id}/`
- **Headers**: 
  - `Authorization: Basic <credentials>`

#### Update student
- **Method**: PUT/PATCH
- **URL**: `/api/students/{id}/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
  - `Content-Type: application/json`
- **Request Body**: Same as create (PUT) or partial data (PATCH)

#### Delete student
- **Method**: DELETE
- **URL**: `/api/students/{id}/`
- **Headers**: 
  - `Authorization: Basic <credentials>`

### Courses

#### List all courses
- **Method**: GET
- **URL**: `/api/courses/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
- **Response**: 
```json
[
    {
        "id": 1,
        "course_code": "CS101",
        "title": "Introduction to Programming",
        "description": "Basic programming concepts",
        "credits": 3,
        "instructor": "Dr. Smith",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
]
```

#### Create course
- **Method**: POST
- **URL**: `/api/courses/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
  - `Content-Type: application/json`
- **Request Body**:
```json
{
    "course_code": "CS101",
    "title": "Introduction to Programming",
    "description": "Basic programming concepts",
    "credits": 3,
    "instructor": "Dr. Smith"
}
```

Similar endpoints exist for GET single, PUT/PATCH, and DELETE operations.

### Enrollments

#### List all enrollments
- **Method**: GET
- **URL**: `/api/enrollments/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
- **Response**: 
```json
[
    {
        "id": 1,
        "student": 1,
        "course": 1,
        "student_name": "John Doe",
        "course_name": "CS101 - Introduction to Programming",
        "enrollment_date": "2024-05-01",
        "grade": "A",
        "status": "active",
        "created_at": "2024-05-01T10:00:00Z",
        "updated_at": "2024-05-01T10:00:00Z"
    }
]
```

#### Create enrollment
- **Method**: POST
- **URL**: `/api/enrollments/`
- **Headers**: 
  - `Authorization: Basic <credentials>`
  - `Content-Type: application/json`
- **Request Body**:
```json
{
    "student": 1,
    "course": 1,
    "grade": "A",
    "status": "active"
}
```

Similar endpoints exist for GET single, PUT/PATCH, and DELETE operations.

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- 400 Bad Request: Invalid data
- 401 Unauthorized: Missing or invalid authentication
- 403 Forbidden: Insufficient permissions
- 404 Not Found: Resource not found
- 500 Internal Server Error: Server-side error

Example error response:
```json
{
    "error": "Resource not found"
}
```

## Authentication

The API supports two authentication methods:
1. Session Authentication (for browser-based access)
2. Basic Authentication (for API clients)

To authenticate:
1. Session: Log in through `/api-auth/login/`
2. Basic: Send Base64 encoded `username:password` in Authorization header 