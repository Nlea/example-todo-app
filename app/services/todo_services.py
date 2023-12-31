from app.models.todo import Todo
from fastapi import HTTPException
from autometrics import autometrics
from fastapi import HTTPException
import time
import random


todos = [
    Todo(id=1, item="Buy groceries"),
    Todo(id=2, item="Walk the dog"),
    # ... other todos ...
]
@autometrics
def get_todos_successful():
    return {
        "data": todos
    }
@autometrics
def get_todos_with_error():
    raise HTTPException(status_code=500, detail="Internal server error")

@autometrics
def add_todo(todo: Todo):
    #delay_seconds = random.uniform(1, 3) # Introcuding some latency in the function
    #time.sleep(delay_seconds)
    todos.append(todo)
    return todo

@autometrics
def update_todo(id: int, updated_todo: Todo)-> Todo:
     for todo in todos:
        if todo.id == id:
            todo.item = updated_todo.item
            return todo
     else:
         raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")