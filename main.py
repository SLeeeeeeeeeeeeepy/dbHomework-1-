from database import engine, Base
import models.user
import models.profile
import models.course
import models.lesson
import models.association
from queries import get_user_courses


from seed.seed_data import seed_data

from crud.user_crud import (
    create_user,
    get_user_by_id,
    update_user,
    delete_user
)

from crud.course_crud import (
    create_course,
    get_course_by_id
)

from queries import (
    get_user_courses,
    get_course_students,
    get_lessons_by_course
)

from database import SessionLocal
from models.user import User


def main():
    print("\n   RESET DATABASE")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("\n   SEED DATA")
    seed_data()

    print("\n   CRUD USER")
    user = create_user("temp_user", "temp@mail.com")
    print("Created : ", user.username)

    fetched = get_user_by_id(user.id)
    print("Fetched : ", fetched.username)

    update_user(user.id, "updated_user")
    updated = get_user_by_id(user.id)
    print("Updated : ", updated.username)

    print("\n   CRUD COURSE")
    course = create_course("Test Course", "Demo course")
    print("Created course : ", course.title)

    fetched_course = get_course_by_id(course.id)
    print("Fetched course : ", fetched_course.title)

    print("\n    RELATIONS")

    db = SessionLocal()

    user1 = db.query(User).filter(User.username == "alexander_pavlovich_romanov").first()
    print("User profile : ", user1.profile.full_name)

    courses = get_user_courses(user1.id)
    print("User courses : ", [c.title for c in courses])

    students = get_course_students(2)
    print("Course students : ", [s.username for s in students])

    lessons = get_lessons_by_course(1)
    print("Course lessons : ", [l.title for l in lessons])

    print("\n   ALL USERS IN DB")
    all_users = db.query(User).all()
    print([u.username for u in all_users])

    db.close()

    print("\n   DELETE DEMO")
    delete_user(user.id)
    print("Temp user deleted")

if __name__ == "__main__":
    main()