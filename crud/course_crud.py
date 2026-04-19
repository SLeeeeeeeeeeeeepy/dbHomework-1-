from database import SessionLocal
from models.course import Course


def create_course(title, description):
    db = SessionLocal()
    course = Course(title=title, description=description)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_course_by_id(course_id):
    db = SessionLocal()
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(course_id, new_title):
    db = SessionLocal()
    course = db.query(Course).get(course_id)
    if course:
        course.title = new_title
        db.commit()
    return course

def delete_course(course_id):
    db = SessionLocal()
    course = db.query(Course).get(course_id)
    if course:
        db.delete(course)
        db.commit()