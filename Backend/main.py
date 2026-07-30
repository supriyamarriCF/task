from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

from database import get_connection
from schemas import Student

app = FastAPI(
    title="Student Management System"
)

# ==============================
# CORS CONFIGURATION
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production if desired
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# JSON FILE STORAGE FUNCTION
# ==============================

def save_student_json(student_data):

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(student_data)

    with open("students.json", "w") as file:
        json.dump(
            students,
            file,
            indent=4
        )

# ==============================
# HOME API
# ==============================

@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management System"
    }

# ==============================
# CREATE STUDENT
# ==============================

@app.post("/students")
def add_student(student: Student):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO students
            (name, age, course, email, phone, address)
            VALUES
            (%s, %s, %s, %s, %s, %s)
            """,
            (
                student.name,
                student.age,
                student.course,
                student.email,
                student.phone,
                student.address
            )
        )

        conn.commit()

        save_student_json({
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "email": student.email,
            "phone": student.phone,
            "address": student.address
        })

        return {
            "message": "Student Added Successfully"
        }

    except Exception as e:
        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        conn.close()

# ==============================
# READ ALL STUDENTS
# ==============================

@app.get("/students")
def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("SELECT * FROM students")

        data = cursor.fetchall()

        students = []

        for s in data:
            students.append({
                "id": s[0],
                "name": s[1],
                "age": s[2],
                "course": s[3],
                "email": s[4],
                "phone": s[5],
                "address": s[6]
            })

        return students

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        conn.close()

# ==============================
# READ STUDENT BY ID
# ==============================

@app.get("/students/{id}")
def get_student(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT * FROM students WHERE id=%s",
            (id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3],
            "email": student[4],
            "phone": student[5],
            "address": student[6]
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        conn.close()

# ==============================
# UPDATE STUDENT
# ==============================

@app.put("/students/{id}")
def update_student(id: int, student: Student):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            UPDATE students
            SET
                name=%s,
                age=%s,
                course=%s,
                email=%s,
                phone=%s,
                address=%s
            WHERE id=%s
            """,
            (
                student.name,
                student.age,
                student.course,
                student.email,
                student.phone,
                student.address,
                id
            )
        )

        conn.commit()

        return {
            "message": "Student Updated Successfully"
        }

    except Exception as e:

        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        conn.close()

# ==============================
# DELETE STUDENT
# ==============================

@app.delete("/students/{id}")
def delete_student(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (id,)
        )

        conn.commit()

        return {
            "message": "Student Deleted Successfully"
        }

    except Exception as e:

        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        conn.close()