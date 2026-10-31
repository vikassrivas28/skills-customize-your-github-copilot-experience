# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage tasks. Practice HTTP methods, request validation, route parameters, and status codes.

## 📝 Tasks

### 🛠️ Set Up the API and Read Tasks

#### Description
Create the FastAPI application and implement endpoints that let a client list tasks and retrieve one task by its ID.

#### Requirements
Completed program should:

- Install the packages listed in `requirements.txt` with `python -m pip install -r requirements.txt`.
- Define a FastAPI application named `app` and a Pydantic `Task` model with a title and a completion state that defaults to `False`.
- Implement `GET /tasks` to return all tasks and `GET /tasks/{task_id}` to return one task.
- Return an HTTP 404 response when a requested task ID does not exist.
- Run the app with `uvicorn main:app --reload` and use `/docs` to inspect and try the endpoints.


### 🛠️ Create and Update Tasks

#### Description
Add endpoints that allow clients to create tasks and replace the details of an existing task.

#### Requirements
Completed program should:

- Implement `POST /tasks` to accept a validated `Task`, assign it a unique integer ID, and return the new task with HTTP 201.
- Implement `PUT /tasks/{task_id}` to replace an existing task's title and completion state while keeping its ID.
- Return HTTP 404 when an update targets an ID that does not exist.
- Confirm that reading a task after creating or updating it returns the latest data.


### 🛠️ Delete Tasks and Handle Missing IDs

#### Description
Complete the API by adding a delete endpoint and checking how it responds to unknown IDs.

#### Requirements
Completed program should:

- Implement `DELETE /tasks/{task_id}` to remove an existing task and return HTTP 204 when successful.
- Return HTTP 404 when a delete targets an ID that does not exist.
- Use `/docs` or `curl` to verify successful list, read, create, update, and delete requests, plus 404 responses for unknown IDs.
