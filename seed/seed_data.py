from database import SessionLocal
from models.user import User
from models.profile import Profile
from models.course import Course
from models.lesson import Lesson


def seed_data():
    db = SessionLocal()

    user1 = User(username="alexander_pavlovich_romanov", email="alexander@mail.com")
    user2 = User(username="frederick_the_great", email="frederick@mail.com")
    user3 = User(username="napoleon_bonaparte", email="napoleon@mail.com")

    profile1 = Profile(full_name="Alexander I Pavlovich", bio="Backend student")
    profile1.user = user1
    profile2 = Profile(full_name="Frederick II of Prussia", bio="Frontend developer")
    profile2.user = user2
    profile3 = Profile(full_name="Napoleon Bonaparte", bio="Data analyst")
    profile3.user = user3

    course1 = Course(title="Python Basics", description="Introduction to Python")
    course2 = Course(title="SQLAlchemy ORM", description="Working with databases")
    course3 = Course(title="Web Development", description="Building web apps")

    lesson1 = Lesson(title="Variables", content="Intro to variables")
    lesson1.course = course1
    lesson2 = Lesson(title="Loops", content="For and while loops")
    lesson2.course = course1

    lesson3 = Lesson(title="ORM Basics", content="What is ORM")
    lesson3.course = course2
    lesson4 = Lesson(title="Relationships", content="SQLAlchemy relations")
    lesson4.course = course2

    lesson5 = Lesson(title="HTML", content="Structure of web pages")
    lesson5.course = course3

    user1.courses.append(course1)
    user1.courses.append(course2)

    user2.courses.append(course2)
    user2.courses.append(course3)

    user3.courses.append(course1)

    db.add_all([
        user1, user2, user3,
        profile1, profile2, profile3,
        course1, course2, course3,
        lesson1, lesson2, lesson3, lesson4, lesson5
    ])

    db.commit()
    db.close()

    print("Database seeded successfully!")