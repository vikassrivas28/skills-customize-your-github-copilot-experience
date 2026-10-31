from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read the API assignment", "completed": False},
    {"id": 2, "title": "Try the interactive docs", "completed": False},
]
next_task_id = 3


@app.get("/tasks")
def list_tasks():
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    pass
