from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: str
    phone: str
    address: str