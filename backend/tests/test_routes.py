from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_get_list():
	response = client.get("/")
	assert response.status_code == 200

# def test_create_habit():

#def test_delete_habit():

#def test_update_habit():