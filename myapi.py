from fastapi import FastAPI , Path
from pydantic import BaseModel 
from typing import Optional
app = FastAPI()

students = {
    1: {
        "name": "Dinesh",
        "age": "21",
        "year": "final"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year:str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    
@app.get("/")
def index():
    return {"data": "First data"}

@app.get("/student_id/{student_id}")
def get_student_id(student_id: int = Path(... , description="enter the id of the student you wanna view")):
    return students[student_id]