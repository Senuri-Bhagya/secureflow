from app.main import app


def test_home_returns_project_information():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["project"] == "SecureFlow"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"
