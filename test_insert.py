# test_insert.py
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

# Create tables (in case not created)
models.Base.metadata.create_all(bind=engine)

def test_create_student():
    db: Session = SessionLocal()
    try:
        # Create a sample student (no ID — DB will auto-generate)
        student_data = schemas.StudentCreate(
            name="Test Student",
            age=20,
            year="3rd Year"
        )

        # Insert into DB
        new_student = models.Student(
            name=student_data.name,
            age=student_data.age,
            year=student_data.year
        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        print("✅ Inserted student:", new_student.id, new_student.name)
    finally:
        db.close()

if __name__ == "__main__":
    test_create_student()
