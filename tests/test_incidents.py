import sys
from pathlib import Path

# добавляем корень проекта в PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_incident():
    resp = client.post(
        "/incidents/",
        json={
            "description": "Самокат не отвечает",
            "source": "operator",
            "status": "new"
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] > 0
    assert data["description"] == "Самокат не отвечает"
    assert data["status"] == "new"
    assert data["source"] == "operator"


def test_get_incidents_with_filter():
    # создаём два инцидента с разными статусами
    client.post("/incidents/", json={
        "description": "Проблема 1",
        "source": "monitoring",
        "status": "in_progress",
    })
    client.post("/incidents/", json={
        "description": "Проблема 2",
        "source": "partner",
        "status": "resolved",
    })

    resp = client.get("/incidents/", params={"status": "resolved"})
    assert resp.status_code == 200
    items = resp.json()
    assert all(item["status"] == "resolved" for item in items)


def test_update_incident_status_and_404():
    # создаём инцидент
    create_resp = client.post("/incidents/", json={
        "description": "Нужно обновить статус",
        "source": "operator",
        "status": "new",
    })
    inc_id = create_resp.json()["id"]

    # обновляем статус
    update_resp = client.patch(
        f"/incidents/{inc_id}",
        json={"status": "resolved"},
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["status"] == "resolved"

    # пробуем обновить несуществующий id
    not_found_resp = client.patch(
        "/incidents/999999",
        json={"status": "resolved"},
    )
    assert not_found_resp.status_code == 404
