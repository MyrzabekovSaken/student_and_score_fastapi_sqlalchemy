from sqlalchemy.orm import Session

import models
import dtos

# Student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def create_student(db: Session, student: dtos.StudentCreate):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: dtos.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    db.delete(db_student)
    db.commit()
    return db_student


# Score

def get_scores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Score).offset(skip).limit(limit).all()


def get_score_by_id(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()


def create_score(db: Session, score: dtos.ScoreCreate):
    db_score = models.Score(value=score.value, student_id=score.student_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def update_score(db: Session, score_id: int, score: dtos.ScoreCreate):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    db_score.value = score.value
    db.commit()
    db.refresh(db_score)
    return db_score


def delete_score(db: Session, score_id: int):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    db.delete(db_score)
    db.commit()
    return db_score
