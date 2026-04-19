from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.association import student_course


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )