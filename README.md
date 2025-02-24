# To-Do App API

This is a simple To-Do app API built using Flask, Flask-Swagger-UI (Flasgger), and SQLite as the database. The API allows users to create, read, update, and delete To-Do items. It is designed with Swagger documentation for easy interaction and testing.

## Features

- **Create a To-Do Item**
- **Read all To-Do Items**
- **Read a specific To-Do Item by ID**
- **Update a To-Do Item**
- **Delete a To-Do Item**
- **Delete all To-Do Items**
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

### 1. **Get All To-Do Items**
- **URL:** `/`
- **Method:** `GET`
- **Description:** Retrieves a list of all To-Do items.
- **Response:**
    - `200 OK` with a list of To-Do items.
    - **Example Response:**

    ```json
    [
        {"id": 1, "title": "Task 1", "description": "First task", "completed": false},
        {"id": 2, "title": "Task 2", "description": "Second task", "completed": true}
    ]
    ```

### 2. **Create a To-Do Item**
- **URL:** `/add`
- **Method:** `POST`
- **Description:** Adds a new To-Do item.
- **Request Body:**

    ```json
    {
      "title": "Task 1",
      "description": "First task"
    }
    ```

- **Response:**
    - `201 Created` if the task is successfully created.
    - `400 Bad Request` if `title` or `description` is missing.
    - **Example Response:**

    ```json
    {"created": "true"}
    ```

### 3. **Delete All To-Do Items**
- **URL:** `/delete`
- **Method:** `DELETE`
- **Description:** Deletes all To-Do items.
- **Response:**
    - `200 OK` if all tasks are successfully deleted.
    - **Example Response:**

    ```json
    {"message": "deleted all tasks"}
    ```

### 4. **Delete a Specific To-Do Item**
- **URL:** `/delete/<task_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific To-Do item by its ID.
- **Response:**
    - `200 OK` if the task is successfully deleted.
    - `404 Not Found` if the task doesn't exist.
    - **Example Response for Success:**

    ```json
    {"deleted": "true", "task_id": 1}
    ```

    - **Example Response for Not Found:**

    ```json
    {"error": "task not found"}
    ```

### 5. **Update a To-Do Item**
- **URL:** `/update/<task_id>`
- **Method:** `PATCH`
- **Description:** Updates a specific To-Do item by its ID.
- **Request Body:**

    ```json
    {
      "title": "Updated Task Title",
      "description": "Updated task description",
      "completed": true
    }
    ```

- **Response:**
    - `200 OK` if the task is successfully updated.
    - `400 Bad Request` if no fields to update are provided or `task_id` is included in the body.
    - `404 Not Found` if the task doesn't exist.
    - **Example Response for Success:**

    ```json
    {"updated": "true", "task_id": 1}
    ```

    - **Example Response for Not Found:**

    ```json
    {"error": "task not found"}
    ```

### 6. **Swagger Documentation**
The API is integrated with Swagger for interactive documentation and testing. You can access the Swagger UI by navigating to:

