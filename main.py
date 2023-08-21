import uvicorn
from fastapi import FastAPI
from app.endpoints import todos  # Import the endpoint from the sub-module

app = FastAPI()

# Include the router from the endpoint sub-module
app.include_router(todos.router)
#app.include_router(prom_metrics.router)

if __name__ == "__main__":
    #import uvicorn
    uvicorn.run(app, host="localhost", port=8000)