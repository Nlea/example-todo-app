from fastapi import APIRouter, HTTPException, Response
from app.models.todo import Todo
from random import choice
from app.custom_exception import CustomException
import random

from app.services.todo_services import get_todos_successful, get_todos_with_error, add_todo, update_todo


router = APIRouter()


@router.post("/todos")

async def add_todo_endpoint(todo: Todo) -> dict:
    new_todo = add_todo(todo)
    return {"data": f"Todo with id {new_todo.id} has been added."}

@router.get("/todos")

async def get_todos_endpoint() -> dict:
    random_number = random.random()
    if random_number < 0.1: # You can change the number here to get a higher error ratio from your code
        return get_todos_successful()
    else:
        return get_todos_with_error()


@router.put("/todos/{id}")

async def update_todo_endpoint(id: int, todo: Todo) -> dict:
    updated_todo = update_todo(id, todo) 
    return {
        "data": f"Todo with id {updated_todo.id} has been updated."
        }    

    ##try:
      ##  if choice([True, False]):  # Simulate random exception
        ##    raise CustomException("Simulated error occurred: This Id number can't be updated.")
        ##updated_todo = update_todo(id, todo) 
        
        ##return {
          ##  "data": f"Todo with id {updated_todo.id} has been updated."
       ## }    
    ##except CustomException as ce:
      ##  raise HTTPException(status_code=400, detail=str(ce))
           
