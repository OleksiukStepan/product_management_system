from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src import schemas
from src.crud import product, category
from src.dependencies import get_db
from src.exceptions import ProductNotFoundError, CategoryNotFoundError
from src.models import Product, Category

app = FastAPI()


@app.post("/products/", response_model=schemas.Product)
def create_product_endpoint(
    product_data: schemas.ProductCreate,
    db: Session = Depends(get_db)
) -> Product:
    return product.create_product(db, product_data)


@app.get("/products/", response_model=list[schemas.Product])
def get_all_products(db: Session = Depends(get_db)) -> list[Product]:
    return product.get_all_product(db)


@app.get("/products/{product_id}/", response_model=schemas.Product)
def get_product_endpoint(
        product_id: int,
        db: Session = Depends(get_db)
) -> Product:
    db_product = product.get_product(db, product_id)
    if not db_product:
        raise ProductNotFoundError(product_id)

    return db_product


@app.put("/products/{product_id}/", response_model=schemas.ProductUpdate)
def update_product_endpoint(
        product_data: schemas.ProductUpdate,
        product_id: int,
        db: Session = Depends(get_db)
) -> Product:
    updated_product = product.update_product(db, product_id, product_data)
    if not updated_product:
        raise ProductNotFoundError(product_id)

    return updated_product


@app.delete("/products/{product_id}/", response_model=schemas.Product)
def delete_product_endpoint(
        product_id: int,
        db: Session = Depends(get_db)
) -> Product:
    deleted_product = product.delete_product(db, product_id)
    if not deleted_product:
        raise ProductNotFoundError(product_id)

    return deleted_product


@app.post("/categories/", response_model=schemas.Category)
def create_category_endpoint(
        category_data: schemas.CategoryCreate,
        db: Session = Depends(get_db)
) -> Category:
    return category.create_category(db, category_data)


@app.get("/categories/", response_model=list[schemas.Category])
def get_all_categories(db: Session = Depends(get_db)) -> list[Category]:
    return category.get_all_categories(db)


@app.get("/categories/{category_id}/", response_model=schemas.Category)
def get_category_endpoint(
        category_id: int,
        db: Session = Depends(get_db)
) -> Category:
    db_category = category.get_category(db, category_id)
    if not db_category:
        raise CategoryNotFoundError(category_id)

    return db_category


@app.put("/categories/{category_id}/", response_model=schemas.Category)
def update_category_endpoint(
        category_data: schemas.CategoryUpdate,
        category_id: int,
        db: Session = Depends(get_db)
) -> Category:
    updated_category = category.update_category(db, category_id, category_data)
    if not updated_category:
        raise CategoryNotFoundError(category_id)

    return updated_category


@app.delete("/categories/{category_id}/", response_model=schemas.Category)
def delete_category_endpoint(
        category_id: int,
        db: Session = Depends(get_db)
) -> Category:
    deleted_category = category.delete_category(db, category_id)
    if not deleted_category:
        raise CategoryNotFoundError(category_id)

    return deleted_category
