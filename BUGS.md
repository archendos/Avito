# BUG REPORTS

## Bug 1: Price Format Incorrect on Ad Creation
- **Priority**: High
- **Description**: When an ad is created with a price value, the price format in the response is incorrect (e.g., missing currency symbol or decimal places).
- **Steps to Reproduce**:
  1. Create an ad with a valid price.
  2. Check the response for the price field.
- **Expected Result**: Price should be formatted as `$1000.00`.
- **Actual Result**: Price returned as `1000`.

## Bug 2: Ads for a Seller Not Displaying Properly
- **Priority**: Medium
- **Description**: When fetching all ads for a seller, the returned list is sometimes incomplete.
- **Steps to Reproduce**:
  1. Add multiple ads for a seller.
  2. Fetch ads using the seller ID.
- **Expected Result**: All ads associated with the seller should be returned.
- **Actual Result**: Only some ads are returned.

## Bug 3: Invalid Seller ID Error Not Handled
- **Priority**: Low
- **Description**: When a non-existent seller ID is used to fetch ads, the API returns an unhandled exception.
- **Steps to Reproduce**:
  1. Send a request with an invalid seller ID.
  2. Observe the server response.
- **Expected Result**: A clear 404 error with a message like "Seller not found".
- **Actual Result**: Server throws an exception with a generic message.