
import pytest
import requests

# Fixture to initialize the API client
@pytest.fixture
def api_client():
    base_url = "https://practice.expandtesting.com/notes/api/api-docs/#/"
    return requests.Session()

# Fixture to create test notes
def test_create_note(api_client, create_test_category, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    note_data = {
        "title": "New Note",
        "content": "This is a new note.",
        "category_id": create_test_category
    }
    response = api_client.post(f"{base_url}/notes", json=note_data)
    assert response.status_code == 200

# Fixture to create test categories
@pytest.fixture
def create_test_category(api_client, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    category_data = {"name": "Test Category"}
    response = api_client.post(f" {base_url}/notes", json=category_data)
    category_id = response.json()["id"]
    yield category_id

# Fixture to update a note
def test_update_note(api_client, create_test_note, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    note_id = create_test_note
    updated_data = {
        "title": "Updated Note",
        "content": "This note has been updated."
    }
    response = api_client.put(f" {base_url}/notes/{id}", json=updated_data)
    assert response.status_code == 200

# Fixture to delete a note
def test_delete_note(api_client, create_test_note, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    note_id = create_test_note
    response = api_client.delete(f"{base_url}/notes/{id}")
    assert response.status_code == 200

# Fixture to Search notes by title or category
def test_search_note_by_title(api_client, create_test_note, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    note_id = create_test_note
    response = api_client.get(f" {base_url}/notes?title=Test Note")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_search_note_by_category(api_client, create_test_category, base_url="https://practice.expandtesting.com/notes/api/api-docs/#/"):
    category_id = create_test_category
    response = api_client.get(f" {base_url}/notes?category_id={category_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0