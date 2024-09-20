# TEST CASES

## API Testing for Ad Service

### Test Case 1: Create an Ad - Successful Scenario
- **Description**: This test verifies the successful creation of an ad with valid input data.
- **Steps**:
  1. Send a POST request to `/ads` with valid ad data (e.g., title, description, price, sellerID).
  2. Check that the response status is 201 (Created).
  3. Verify that the response body contains the created ad details.
  4. Verify that the ad is saved in the database.
- **Expected Result**: Ad is created successfully, response contains valid ad data, and a unique ID is generated.

### Test Case 2: Get Ad by ID - Successful Scenario
- **Description**: This test checks if an ad can be fetched using its unique ID.
- **Steps**:
  1. Send a GET request to `/ads/{id}` with an existing ad ID.
  2. Check that the response status is 200 (OK).
  3. Verify that the returned ad details match the expected data.
- **Expected Result**: The correct ad details are returned.

### Test Case 3: Get All Ads by Seller ID
- **Description**: This test checks if all ads from a seller can be retrieved.
- **Steps**:
  1. Send a GET request to `/ads?sellerID={sellerID}` with a valid seller ID.
  2. Check that the response status is 200 (OK).
  3. Verify that the response contains a list of ads associated with the seller.
- **Expected Result**: A list of ads belonging to the specified seller is returned.

### Test Case 4: Create an Ad - Invalid Input
- **Description**: This test verifies that the API returns an error when creating an ad with invalid input.
- **Steps**:
  1. Send a POST request to `/ads` with invalid or missing fields.
  2. Check that the response status is 400 (Bad Request).
  3. Verify that the error message details the reason for the failure.
- **Expected Result**: An appropriate error message is returned for invalid input.
