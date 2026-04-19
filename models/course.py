from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.association import student_course


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)

    lessons = relationship("Lesson", back_populates="course")

    students = relationship(
        "User",
        secondary=student_course,
        back_populates="courses"
    )