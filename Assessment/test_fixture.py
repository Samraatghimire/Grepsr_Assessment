import pytest
import requests

Base_URL = "https://practice.expandtesting.com/notes/api/api-docs/#/"

# Smoke test for creating a new note
@pytest.mark.smoke
def test_create_note():
    response = requests.post(
        Base_URL + "/notes",
        json={"title": "Test note", "content": "This is a test note."},
    )
    assert response.status_code == 200

#Categorizing notes into different category
@pytest.mark.smoke
def test_category_note():

# Get the note ID
    note_id = response.json()["id"]

# Create a new category
response = requests.post(
    Base_URL + "/notes",
    json={"name": "Test category"},
)
assert response.status_code == 200

# Get the category ID
category_id = response.json()["user_id"]

# Categorizing the note
response = requests.get(Base_URL + f"/notes/{id}")
assert response.status_code == 200

# Smoke test for updating a note
@pytest.mark.smoke
def test_update_note():
    response = requests.put(
        Base_URL + f"/notes{id}",
        json={"title": "Updated note", "content": "This is an updated note."},
    )
    assert response.status_code == 200

# Smoke test for deleting a note
@pytest.mark.smoke
def test_delete_note():
    response = requests.delete(Base_URL + f"/notes{id}")
    assert response.status_code == 200

#End of smoke testing

# Regression test for creating a note with an empty title
@pytest.mark.regression
def test_create_note_with_empty_title():
    response = requests.post(
        Base_URL + "/notes",
        json={"content": "This is a test note."},
    )
    assert response.status_code == 400

# Regression test for creating a note with an empty content
@pytest.mark.regression
def test_create_note_with_empty_content():
    response = requests.post(
        Base_URL + "/notes",
        json={"title": "Test note"},
    )
    assert response.status_code == 400

# Regression test for retrieving a note with an invalid ID
@pytest.mark.regression
def test_get_note_with_invalid_id():
    response = requests.get(Base_URL + f"/notes{id}")
    assert response.status_code == 404

# Regression test for updating a note with an invalid ID
@pytest.mark.regression
def test_update_note_with_invalid_id():
    response = requests.put(
        Base_URL + f"/notes{id}",
        json={"title": "Updated note", "content": "This is an updated note."},
    )
    assert response.status_code == 404

# Regression test for deleting a note with an invalid ID
@pytest.mark.regression
def test_delete_note_with_invalid_id():
    response = requests.delete(Base_URL + f"/notes/{id}")
    assert response.status_code == 404

