# REST API Automation Framework

A Python-based REST API automation project using `requests` and `pytest`.

This project demonstrates automated testing for GET, POST, PUT, DELETE, and negative API scenarios.

## Problem

Manually validating APIs can be repetitive and time-consuming.

API automation helps verify:

- HTTP status codes
- JSON response data
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
- User ID
- User name
- Email

### POST Data

Validates:

- POST request
- HTTP 201 response
- Request payload
- Returned title
- User ID

### PUT Data

Validates:

- PUT request
- HTTP 200 response
- Updated response content

### DELETE Data

Validates:

- DELETE request
- HTTP 200 response

### Negative Test

Requests a non-existing user:

```text
/users/9999
