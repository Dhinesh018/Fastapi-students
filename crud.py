from sqlalchemy.orm import Session
import models,schemas


def create_student(db:Session,student : schemas.StudentCreate):
    db_student = models.Student(name=student.name,
                                age=student.age,
                                year=student.year)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db:Session,student_id : int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db:Session,skip: int = 0,limit : int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()


def update_student(db:Session,student_id:int,updated_student: schemas.StudentCreate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if student:
        
        student.name = updated_student.name
        student.age = updated_student.age
        student.year = updated_student.year
        db.commit()
        db.refresh(student)
    return student


def delete_student(db: Session,student_id : int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student