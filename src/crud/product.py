from typing import Optional

from sqlalchemy.orm import Session

from src.models import Product
from src.schemas import ProductCreate, ProductUpdate


def get_all_product(db: Session) -> list[Product]:
    return db.query(Product).all()


def get_product(db: Session, product_id: int) -> Optional[Product]:
    return db.query(Product).filter(Product.id==product_id).first()


def create_product(db: Session, product: ProductCreate) -> Product:
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def update_product(
        db: Session,
        product_id: int,
        product: ProductUpdate
) -> Optional[Product]:
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int) -> Optional[Product]:
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product
