import requests

# Define the base URL of the API
BASE_URL = "http://api.example.com"

def test_create_ad_success():
    """
    Test the successful creation of an ad with valid data.
    """
    # Define the payload with ad data
    payload = {
        "title": "Test Ad",
        "description": "This is a test ad",
        "price": 1000,
        "sellerID": 1
    }
    
    # Send POST request to create an ad
    response = requests.post(f"{BASE_URL}/ads", json=payload)
    
    # Assert that the status code is 201 (Created)
    assert response.status_code == 201
    
    # Assert that the response contains the expected keys
    ad_data = response.json()
    assert "id" in ad_data
    assert ad_data["title"] == "Test Ad"
    assert ad_data["price"] == 1000

def test_create_ad_invalid_input():
    """
    Test creating an ad with missing fields, expecting a failure.
    """
    # Define payload with missing required fields
    payload = {
        "title": "",  # Title is empty
        "description": "This ad has no title",
        "price": 1000,
        "sellerID": 1
    }
    
    # Send POST request with invalid payload
    response = requests.post(f"{BASE_URL}/ads", json=payload)
    
    # Assert that the status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Assert that error message is as expected
    error_message = response.json().get("error")
    assert "Invalid input" in error_message
