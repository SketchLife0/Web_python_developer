from flask import Flask, request
from pydantic import BaseModel, ValidationError

# Модель задачи
class Task(BaseModel):
    title: str
    description: str
    status: str

# Инициализация приложения Flask
app = Flask(__name__)

# Список задач
tasks = []

# Конечная точка GET /tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Конечная точка GET /tasks/{id}
@app.get("/tasks/{id}")
def get_task(id: int):
    try:
        task = tasks[id]
    except IndexError:
        raise ValueError("Задача с таким идентификатором не найдена")
    return task

# Конечная точка POST /tasks
@app.post("/tasks")
def create_task():
    try:
        task = Task.parse_obj(request.get_json())
    except ValidationError as e:
        raise ValueError(e.errors())
    tasks.append(task)
    return task

# Конечная точка PUT /tasks/{id}
@app.put("/tasks/{id}")
def update_task(id: int):
    try:
        task = Task.parse_obj(request.get_json())
    except ValidationError as e:
        raise ValueError(e.errors())
    tasks[id] = task
    return task

# Конечная точка DELETE /tasks/{id}
@app.delete("/tasks/{id}")
def delete_task(id: int):
    try:
        tasks.pop(id)
    except IndexError:
        raise ValueError("Задача с таким идентификатором не найдена")
    return "Задача удалена"

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)