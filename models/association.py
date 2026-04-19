from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base


student_course = Table(
    "student_course",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)