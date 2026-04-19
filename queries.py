from database import SessionLocal
from models.course import Course
from models.user import User


def get_user_by_id(user_id):
    db = SessionLocal()
    user = db.get(User, user_id)
    db.close()
    return user

def get_user_by_username(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

def get_course_by_title(title):
    db = SessionLocal()
    course = db.query(Course).filter(Course.title == title).first()
    db.close()
    return course

def get_user_courses(user_id):
    db = SessionLocal()
    user = db.get(User, user_id)
    courses = user.courses if user else []
    db.close()
    return courses

def get_course_students(course_id):
    db = SessionLocal()
    course = db.get(Course, course_id)
    students = course.students if course else []
    db.close()
    return students

def get_lessons_by_course(course_id):
    db = SessionLocal()
    course = db.get(Course, course_id)
    lessons = course.lessons if course else []
    db.close()
    return lessons

def get_user_profile(user_id):
    db = SessionLocal()
    user = db.get(User, user_id)
    profile = user.profile if user else None
    db.close()
    return profile

def get_courses_by_username(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    courses = user.courses if user else []
    db.close()
    return courses

def get_students_by_course_title(title):
    db = SessionLocal()
    course = db.query(Course).filter(Course.title == title).first()
    students = course.students if course else []
    db.close()
    return students

def get_users_with_courses():
    db = SessionLocal()

    results = (
        db.query(User.username, Course.title)
        .join(User.courses)
        .all()
    )

    db.close()
    return results