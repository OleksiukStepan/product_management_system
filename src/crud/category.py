from typing import Optional

from sqlalchemy.orm import Session

from src.models import Category
from src.schemas import CategoryCreate, CategoryUpdate


def get_all_categories(db: Session) -> list[Category]:
    return db.query(Category).all()


def get_category(db: Session, category_id: int) -> Optional[Category]:
    return db.query(Category).filter(Category.id==category_id).first()


def create_category(db: Session, category: CategoryCreate) -> Category:
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


def update_category(
        db: Session,
        category_id: int,
        category: CategoryUpdate
) -> Optional[Category]:
    db_category = get_category(db, category_id)
    if not db_category:
        return None

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)

    return db_category


def delete_category(db: Session, category_id: int) -> Optional[Category]:
    db_category = get_category(db, category_id)
    if not db_category:
        return None

    db.delete(db_category)
    db.commit()

    return db_category
