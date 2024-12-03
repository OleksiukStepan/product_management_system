from fastapi.testclient import TestClient


def test_create_category(client: TestClient) -> None:
    response = client.post(
        "/categories/",
        json={"name": "Test Category"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"


def test_get_all_categories(client: TestClient) -> None:
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Test Category"


def test_update_category(client: TestClient) -> None:
    response = client.put(
        "/categories/1/",
        json={"name": "Updated Category"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Category"


def test_delete_category(client: TestClient) -> None:
    response = client.delete("/categories/1/")
    assert response.status_code == 200

    response = client.get("/categories/1/")
    assert response.status_code == 404
