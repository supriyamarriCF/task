from pydantic import BaseModel, EmailStr, field_validator

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: EmailStr
    phone: str
    address: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if not value.endswith("@gmail.com"):
            raise ValueError("Email must end with @gmail.com.")
        return value