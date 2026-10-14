"""A small, runnable FastAPI learning example.

Run with: uvicorn app:app --reload
API docs: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Practice API",
    description="A small example of routes, request validation, and in-memory data.",
    version="1.0.0",
)


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=1, le=120)
    roll: int = Field(ge=1)


students: dict[int, StudentCreate] = {}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI practice API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/students")
def list_students() -> list[dict[str, int | str]]:
    return [
        {"roll": roll, "name": student.name, "age": student.age}
        for roll, student in students.items()
    ]


@app.post("/students", status_code=201)
def create_student(student: StudentCreate) -> dict[str, int | str]:
    if student.roll in students:
        raise HTTPException(status_code=409, detail="A student with this roll already exists")
    students[student.roll] = student
    return {"roll": student.roll, "name": student.name, "age": student.age}


@app.get("/students/{roll}")
def get_student(roll: int) -> dict[str, int | str]:
    student = students.get(roll)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"roll": student.roll, "name": student.name, "age": student.age}
