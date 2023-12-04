from app.models.todo import Todo
from fastapi import HTTPException
from fastapi import HTTPException

from opentelemetry import trace
from opentelemetry import metrics


tracer = trace.get_tracer("todo.tracer")
meter = metrics.get_meter("todo.meter")

todo_counter = meter.create_counter(
    "get.todo",
    description="This is a description",
)



todos = [
    Todo(id=1, item="Buy groceries"),
    Todo(id=2, item="Walk the dog"),
    # ... other todos ...
]
def get_todos_successful():
    with tracer.start_as_current_span("get-todos"):
        todo_counter.add(1)
        return {
            "data": todos
            }

def get_todos_with_error():
    with tracer.start_as_current_span("get-todos-e"):
        raise HTTPException(status_code=500, detail="Internal server error")


def add_todo(todo: Todo):
    #delay_seconds = random.uniform(1, 3) # Introcuding some latency in the function
    #time.sleep(delay_seconds)
    todos.append(todo)
    return todo


def update_todo(id: int, updated_todo: Todo)-> Todo:
     for todo in todos:
        if todo.id == id:
            todo.item = updated_todo.item
            return todo
     else:
         raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")