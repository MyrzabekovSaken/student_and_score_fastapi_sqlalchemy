from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True


class ScoreBase(BaseModel):
    value: int = Field(..., ge=0, le=10)
    student_id: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True
