from sqlalchemy.orm import Session

from models.user import User


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def get_users(db: Session):
    return db.query(User).all()


# db.add(object)
# db.commit()
# db.refresh(object)

# db.query(Model).filter(...).first()
# db.query(Model).filter(...).all()
# db.query(Model).all()
