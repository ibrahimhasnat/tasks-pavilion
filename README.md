# Tasks Pavilion API

Welcome to **Tasks Pavilion**, a simple FastAPI-based API for managing tasks. This API provides basic functionalities for creating, reading, updating, and deleting tasks, along with the ability to filter tasks by label and priority.

**[Explore API with Swagger UI](https://tasks-pavilion.onrender.com/docs)**

## Features

- **Create Task:** Create a new task by sending a POST request to `/api/tasks/`.

- **Read All Tasks:** Retrieve a list of all tasks by sending a GET request to `/api/tasks/`.

- **Read Task by ID:** Retrieve a specific task by its ID with a GET request to `/api/tasks/{task_id}`.

- **Update Task:** Update an existing task by sending a PUT request to `/api/tasks/{task_id}`.

- **Delete Task:** Delete a task by its ID with a DELETE request to `/api/tasks/{task_id}`.

- **Filter Tasks by Label:** Retrieve tasks filtered by label by sending a GET request to `/api/tasks/labels/{label}`.

- **Filter Tasks by Priority:** Retrieve tasks filtered by priority by sending a GET request to `/api/tasks/priorities/{priority}`.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ibrahimhasnat/tasks-pavilion.git
   cd tasks-pavilion
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt 
3. **Run the Application:**
    ```bash
    uvicorn main:app --reload
    ```
4. **Access the API:**
   
   Open your browser or a tool like Swagger UI to interact with the Tasks Pavilion API.
5. **Endpoints:**
   - Base URL: `http://127.0.0.1:8000`
   - Tasks API: `/api/tasks`
  
## Dependencies
- **[FastAPI:](https://fastapi.tiangolo.com/)** A modern, fast (high-performance), web framework for building APIs with Python.

- **[Pydantic:](https://pydantic.dev/)** Data validation and settings management using Python type hints.