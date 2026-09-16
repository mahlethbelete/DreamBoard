from sqlalchemy.orm import Session

from models.category import Category


def create_category(db: Session, category: Category):
    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def get_category_by_name(db: Session, user_id: int, name: str):
    return (
        db.query(Category)
        .filter(Category.user_id == user_id, Category.name == name)
        .first()
    )


def get_categories_by_user(db: Session, user_id: int):
    return db.query(Category).filter(Category.user_id == user_id).all()


def update_category(db: Session, category: Category, data: dict):
    for field, value in data.items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)

    return category


def delete_category(db: Session, category: Category):
    db.delete(category)
    db.commit()
