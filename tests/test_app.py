import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_info():
    client = app.test_client()

    response = client.get("/info")

    assert response.status_code == 200
    assert response.json == {
        "name": "python-ci-cd-demo",
        "version": "1.0.0"
    }