from fastapi import HTTPException


class BaseAPIException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class ProductNotFoundError(BaseAPIException):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=404,
            detail=f"Product with ID {product_id} not found"
        )


class CategoryNotFoundError(BaseAPIException):
    def __init__(self, category_id: int):
        super().__init__(
            status_code=404,
            detail=f"Category with ID {category_id} not found"
        )