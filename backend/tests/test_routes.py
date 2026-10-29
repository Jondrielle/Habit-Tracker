from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_get_list():
	response = client.get("/")
	assert response.status_code == 200


def test_create_habit_valid_name_and_description_data():
	response = client.post("/habit",
		json={
			"name":"wash dishes",
			"description":"daily"
		})
	assert response.status_code == 200
	data = response.json()
	assert data["name"] == "wash dishes"
	assert data["description"] == "daily"

def test_create_habit_valid_name_only():
	response = client.post("/habit",
		json={
			"name":"Do laundry"
		})
	assert response.status_code == 200
	assert response.json()["name"] == "Do laundry"

def test_create_habit_missing_required_name_field():
	response = client.post("/habit", 
		json={
			"description":"weekly chores"
		})
	assert response.status_code == 422

def test_create_habit_missing_json():
	response = client.post("/habit")
	assert response.status_code == 422

def test_create_habit_streak_default_value():
	response = client.post("/habit",
		json={
			"name":"read",
			"description":"daily"
		})
	assert response.status_code == 200
	assert response.json()["streak"] == 0

def test_create_habit_is_complete_default_value():
	response = client.post("/habit",
		json={
			"name": "Shower",
		})

	assert response.status_code == 200
	assert response.json()["is_complete"] is False

def test_create_habit_last_completed_date_default_value():
	response = client.post("/habit",
		json={
			"name": "Shower",
		})

	assert response.status_code == 200
	assert response.json()["last_completed"] is None


def test_delete_a_nonexistent_habit():
	response = client.delete("/habit/1000")
	assert response.status_code == 404

#def test_delete_habit():

#def test_update_habit():