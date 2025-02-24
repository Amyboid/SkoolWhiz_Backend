<h1 align="center"> Skoolwhiz To-do REST API 📌</h1>

A simple, **RESTful API** for managing **Todo items** using **Flask** and **SQLite**. Supports **CRUD operations**, Swagger API documentation.

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue)

![pip](https://img.shields.io/badge/pip-%2320232a?style=for-the-badge&logo=pypi&logoColor=3775A9)
![python](https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=3776AB)
![Flask](https://img.shields.io/badge/flask-%2320232a?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2320232a?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/swagger-%2320232a?style=for-the-badge&logo=swagger&logoColor=white)

</div>

## Features ✨

- ✅ **Create a To-Do Item**
- 📋 **Read all To-Do Items**
- ✏️ **Update a To-Do Item**
- ❌ **Delete a To-Do Item**
- 🗑️ **Delete all To-Do Items**
- 🧑‍💻 **Swagger Documentation** for interactive API testing

## Requirements 🛠️

- 🐍 **Python 3.x**
- 🧰 **Flask** 
- 📄 **Flask-Swagger-UI (Flasgger)**
- 💾 **SQLite** (built-in with Python)

## Installation & SetUp 🏗️

1. Clone the repository:

    ```bash
    git clone https://github.com/Amyboid/SkoolWhiz_Backend.git
    cd SkoolWhiz_Backend
    ```

2. Set up a virtual environment (recommended):

    ```bash
    py -3 -m venv .venv
    ```
    
    ### Windows 💻

    ```bash
    .venv\Scripts\activate
    ```

    ### macOS / Linux 🍃

    ```bash
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask App 🚀:

    ```bash
    flask run
    ```

## API Endpoints 🛣️

The following endpoints are available:

| **Endpoint**                          | **Method** | **Description**                                                | **Request Body**                                                                                                                                                        | **Response Status**     | **Example Response**                                                                                                                                                     |
|---------------------------------------|------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Get All To-Do Items**            | `GET`      | Retrieves a list of all To-Do items.                           | None                                                                                                                                                                   | `200 OK`                | ```json [{ "id": 1, "title": "Task 1", "description": "First task", "completed": false }, { "id": 2, "title": "Task 2", "description": "Second task", "completed": true }] ``` |
| **2. Create a To-Do Item**            | `POST`     | Adds a new To-Do item.                                         | ```json { "title": "Task 1", "description": "First task" } ```                                                                                                        | `201 Created`           | ```json { "created": "true" } ```                                                                                                                                            |
| **3. Delete All To-Do Items**         | `DELETE`   | Deletes all To-Do items.                                       | None                                                                                                                                                                   | `200 OK`                | ```json { "message": "deleted all tasks" } ```                                                                                                                              |
| **4. Delete a Specific To-Do Item**   | `DELETE`   | Deletes a specific To-Do item by its ID.                       | None                                                                                                                                                                   | `200 OK` / `404 Not Found` | ```json { "deleted": "true", "task_id": 1 } ``` <br> ```json { "error": "task not found" } ```                                                                             |
| **5. Update a To-Do Item**            | `PATCH`    | Updates a specific To-Do item by its ID.                       | ```json { "title": "Updated Task Title", "description": "Updated task description", "completed": true } ```                                                            | `200 OK` / `404 Not Found` | ```json { "updated": "true", "task_id": 1 } ``` <br> ```json { "error": "task not found" } ```                                                                             |

### Notes 📝:
- The `Request Body` column shows the JSON format expected for `POST` and `PATCH` requests.
- The `Response Status` shows possible HTTP status codes that could be returned.
- The `Example Response` column provides sample responses returned from the API for each endpoint.

### 6. Swagger Documentation 📑

The API is integrated with **Swagger** for interactive documentation and testing. You can access the Swagger UI by navigating to:

- **URL:** `/apidocs` (Make sure your Flask app is running)

Once the Flask app is running, open your browser and go to [http://localhost:5000/apidocs](http://localhost:5000/apidocs). This will display the **Swagger UI**, where you can:

- **View the full API documentation**
- **Test each endpoint interactively** by entering input data and hitting "Execute"
- **See real-time responses** with status codes, response data, and more 🖥️
