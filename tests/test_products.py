from fastapi.testclient import TestClient


def test_create_product(client: TestClient) -> None:
    response = client.post(
        "/products/",
        json={
            "name": "Test product",
            "description": "Test product description",
            "price": 30.02,
            "quantity": 100,
            "category_id": None
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test product"
    assert data["description"] == "Test product description"
    assert data["price"] == 30.02
    assert data["quantity"] == 100


def test_get_all_products(client: TestClient) -> None:
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Test product"


def test_update_product(client: TestClient) -> None:
    response = client.put(
        "/products/1/",
        json={
            "name": "Updated product",
            "description": "Updated description",
            "price": 150.0,
            "quantity": 5,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated product"
    assert data["price"] == 150.0
    assert data["quantity"] == 5


def test_delete_product(client: TestClient) -> None:
    response = client.delete("/products/1/")
    assert response.status_code == 200

    response = client.get("/products/1/")
    assert response.status_code == 404
