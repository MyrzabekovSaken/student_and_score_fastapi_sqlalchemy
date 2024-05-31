from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session


from database import SessionLocal, engine
import service
import models
import dtos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Student

@app.get("/students", response_model=list[dtos.Student])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_students(db, skip, limit)


@app.get("/students/{student_id}", response_model=dtos.Student)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    db_student = service.get_student_by_id(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/students", response_model=dtos.Student, status_code=201)
def create_student(student: dtos.StudentCreate, db: Session = Depends(get_db)):
    return service.create_student(db, student)


@app.put("/students/{student_id}", response_model=dtos.Student)
def update_student(student_id: int, student: dtos.StudentCreate, db: Session = Depends(get_db)):
    return service.update_student(db, student_id, student)


@app.delete("/students/{student_id}", response_model=dtos.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return service.delete_student(db, student_id)


# Score

@app.get("/scores", response_model=list[dtos.Score])
def get_scores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_scores(db, skip, limit)


@app.get("/scores/{score_id}", response_model=dtos.Score)
def get_score_by_id(score_id: int, db: Session = Depends(get_db)):
    db_score = service.get_score_by_id(db, score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score


@app.post("/scores", response_model=dtos.Score, status_code=201)
def create_score(score: dtos.ScoreCreate, db: Session = Depends(get_db)):
    return service.create_score(db, score)


@app.put("/scores/{score_id}", response_model=dtos.Score)
def update_score(score_id: int, score: dtos.ScoreCreate, db: Session = Depends(get_db)):
    return service.update_score(db, score_id, score)


@app.delete("/scores/{score_id}", response_model=dtos.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    return service.delete_score(db, score_id)
