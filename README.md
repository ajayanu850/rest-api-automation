# REST API Automation Framework

A Python-based REST API automation project using `requests` and `pytest`.

This project demonstrates automated testing for GET, POST, PUT, DELETE, response validation, and negative API scenarios.

## Problem

Manually validating APIs can be repetitive and time-consuming.

API automation helps verify:

- HTTP status codes
- Response headers
- JSON response structure
- Required fields
- Data types
- CRUD operations
- Invalid requests
- Error responses

## Solution

This project uses Python, Requests, and Pytest to automate REST API validation against the public JSONPlaceholder API.

## Test Scenarios

### GET User

Validates:

- GET request
- HTTP 200 response
- JSON Content-Type
- Response is a dictionary
- Required fields: id, name, email
- User ID
- Data types
- Basic email format

### POST Data

Validates:

- POST request
- HTTP 201 response
- JSON Content-Type
- Required response fields
- Request vs response values
- Data types

### PUT Data

Validates:

- PUT request
- HTTP 200 response
- JSON Content-Type
- Required response fields
- Updated values
- Data types

### DELETE Data

Validates:

- DELETE request
- HTTP 200 response

### Negative Test

Requests a user that does not exist:

```text
/users/9999
