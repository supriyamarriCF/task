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
Render URL: https://assignment-2zgv.onrender.com
Swagger Docs: https://assignment-2zgv.onrender.com/docs
The Render free tier may take 30–60 seconds to respond after inactivity.
All requests and responses use JSON format.