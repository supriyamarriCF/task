Student Management System - Backend API
Base URL
https://task-2-hjlr.onrender.com/
Swagger Documentation
https://task-2-hjlr.onrender.com/docs
Technology Stack
FastAPI
PostgreSQL (Neon)
Render
Pydantic
Setup in VS Code
1. Open the Backend folder
cd Backend
2. Install all required packages
pip install -r requirements.txt
3. Install Email Validator
pip install email-validator
4. Run the FastAPI Server
python -m uvicorn main:app --reload
5. Open Swagger UI
http://127.0.0.1:8000/docs
Environment Variables (.env)
DB_HOST=<neon-host>
DB_NAME=<database-name>
DB_USER=<database-user>
DB_PASSWORD=<database-password>
DB_PORT=5432
API Endpoints
Method	Endpoint	Description
GET	/students	Get all students
GET	/students/{id}	Get student by ID
POST	/students	Add a student
PUT	/students/{id}	Update a student
DELETE	/students/{id}	Delete a student
Request Body
{
  "name": "Rahul Sharma",
  "age": 20,
  "course": "B.Tech CSE",
  "email": "rahul@gmail.com",
  "phone": "9876543210",
  "address": "Bangalore"
}
Validation
Email must be a valid Gmail address (@gmail.com).
Phone number must contain exactly 10 digits.
All fields are required.
Backend Architecture
Frontend
     │
     ▼
Render (FastAPI Backend)
     │
     ▼
Neon PostgreSQL Database
The frontend should communicate only with the deployed Render API.
Do not connect directly to the Neon PostgreSQL database.
Notes
Render URL: https://task-2-hjlr.onrender.com/
Swagger Docs:https://task-2-hjlr.onrender.com/docs
The Render free tier may take 30–60 seconds to respond after inactivity.
All requests and responses use JSON format.

# Student Management System - Backend API

A RESTful Student Management System Backend API built using FastAPI, PostgreSQL (Neon), and deployed on Render. The API supports CRUD (Create, Read, Update, Delete) operations for student records with Pydantic validation.

## Live Demo

**Base URL**

https://task-2-hjlr.onrender.com/

**Swagger Documentation**

https://task-2-hjlr.onrender.com/docs

## Technology Stack

- FastAPI
- PostgreSQL (Neon)
- Render
- Pydantic
- psycopg2
- python-dotenv

## Project Structure

```text
Backend/
│── main.py
│── database.py
│── schemas.py
│── requirements.txt
│── .env
└── README.md
```

> Remove `models.py` and `crud.py` from the structure if they do not exist in your project.

## Local Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Install Email Validator:

```bash
pip install email-validator
```

### 3. Configure Environment Variables

Create a `.env` file inside the Backend folder.

```env
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=5432
```

### 4. Run the Server

```bash
python -m uvicorn main:app --reload
```

### 5. Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |

## Sample Request Body

```json
{
  "name": "Rahul Sharma",
  "age": 20,
  "course": "B.Tech CSE",
  "email": "rahul@gmail.com",
  "phone": "9876543210",
  "address": "Bangalore"
}
```

## Validation Rules

### Email

- Must be a valid email address.
- Must end with `@gmail.com`.

Examples:

```
rahul@gmail.com
```

Valid

```
rahul@yahoo.com
```

Invalid

### Phone

- Must contain exactly 10 digits.

Examples:

```
9876543210
```

Valid

```
98765
98765432101
```

Invalid

### Required Fields

- Name
- Age
- Course
- Email
- Phone
- Address

## Backend Architecture

```text
Frontend
    │
    ▼
FastAPI Backend (Render)
    │
    ▼
Neon PostgreSQL Database
```

The frontend should communicate only with the deployed FastAPI API hosted on Render. It should never connect directly to the Neon PostgreSQL database.

## Response Format

All API requests and responses use JSON.

Example:

```json
{
  "message": "Student Added Successfully"
}
```

## Notes

- Render free tier may take 30–60 seconds to wake up after inactivity.
- All requests and responses are in JSON format.

## Features

- Create Student
- View All Students
- View Student by ID
- Update Student
- Delete Student
- PostgreSQL Integration
- Pydantic Validation
- Gmail Email Validation
- Phone Number Validation
- Swagger API Documentation
- Render Deployment

## Author

Developed using FastAPI, PostgreSQL (Neon), Render, and Pydantic.