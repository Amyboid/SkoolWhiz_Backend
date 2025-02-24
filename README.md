# To-Do App API

This is a simple To-Do app API built using Flask, Flask-Swagger-UI (Flasgger), and SQLite as the database. The API allows users to create, read, update, and delete To-Do items. It is designed with Swagger documentation for easy interaction and testing.

## Features

- **Create a To-Do Item**
- **Read all To-Do Items**
- **Read a specific To-Do Item by ID**
- **Update a To-Do Item**
- **Delete a To-Do Item**
- **Swagger Documentation** for interactive API testing

## Requirements

- Python 3.x
- Flask
- Flask-Swagger-UI (Flasgger)
- SQLite (built-in with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-app-api.git
    cd todo-app-api
    ```

2. Set up a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the SQLite database (if it doesn't exist):

    ```bash
    python create_db.py
    ```

## API Endpoints

The following endpoints are available:

### 1. **Create a To-Do Item**
- **URL:** `/todo`
- **Method:** `POST`
- **Description:** Creates a new To-Do item.
- **Request Body:**

    ```json
    {
      "task": "Finish homework",
      "done": false
    }
    ```

- **Response:**
    - `201 Created` on success with the created To-Do item.
    - `400 Bad Request` if request data is invalid.

### 2. **Get All To-Do Items**
- **URL:** `/todos`
- **Method:** `GET`
- **Description:** Retrieves a list of all To-Do items.
- **Response:**
    - `200 OK` with a list of To-Do items.

### 3. **Get a To-Do Item by ID**
- **URL:** `/todo/<id>`
- **Method:** `GET`
- **Description:** Retrieves a single To-Do item by its ID.
- **Response:**
    - `200 OK` with the To-Do item.
    - `404 Not Found` if the item doesn't exist.

### 4. **Update a To-Do Item**
- **URL:** `/todo/<id>`
- **Method:** `PUT`
- **Description:** Updates an existing To-Do item.
- **Request Body:**

    ```json
    {
      "task": "Finish homework",
      "done": true
    }
    ```

- **Response:**
    - `200 OK` if the item is updated successfully.
    - `404 Not Found` if the item doesn't exist.
    - `400 Bad Request` if the request data is invalid.

### 5. **Delete a To-Do Item**
- **URL:** `/todo/<id>`
- **Method:** `DELETE`
- **Description:** Deletes a To-Do item by its ID.
- **Response:**
    - `200 OK` if the item is deleted.
    - `404 Not Found` if the item doesn't exist.

## Swagger Documentation

The API is integrated with Swagger for interactive documentation and testing. You can access the Swagger UI by navigating to:

