from fastapi.testclient import TestClient

from mizan.main import create_app


def test_live_returns_ok() -> None:
    client = TestClient(create_app())

    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
