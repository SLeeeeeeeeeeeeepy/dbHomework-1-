from database import SessionLocal
from models.user import User


def create_user(username, email):
    db = SessionLocal()
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(user_id):
    db = SessionLocal()
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(email):
    db = SessionLocal()
    return db.query(User).filter(User.email == email).first()

def update_user(user_id, new_username):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        user.username = new_username
        db.commit()
    return user

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)
        db.commit()