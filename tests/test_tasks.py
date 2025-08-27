BASE_URL = "/tasks"


def test_get_all_tasks(test_client, test_task):
    response = test_client.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["title"] == test_task.title
    assert data[0]["description"] == test_task.description
    assert data[0]["status"] == test_task.status


def test_create_task(test_client):
    payload = {
        "title": "new_task",
        "description": "new_description",
        "status": "Создано",
    }
    response = test_client.post(BASE_URL + "/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["status"] == payload["status"]


def test_get_task_by_id(test_client, test_task):
    response = test_client.get(f"{BASE_URL}/{test_task.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == str(test_task.id)
    assert data["title"] == test_task.title
    assert data["description"] == test_task.description
    assert data["status"] == test_task.status


def test_update_task(test_client, test_task):
    payload = {
        "title": "updated_title",
        "description": "updated_description",
        "status": "В работе",
    }
    response = test_client.put(f"{BASE_URL}/{test_task.id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == str(test_task.id)
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["status"] == payload["status"]


def test_delete_task(test_client, test_task):
    response = test_client.delete(f"{BASE_URL}/{test_task.id}")
    assert response.status_code == 204
    response2 = test_client.get(f"{BASE_URL}/{test_task.id}")
    assert response2.status_code == 400
