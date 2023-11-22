from fastapi import FastAPI
from routers import tasks

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Welcome to Tasks Pavilion'}

app.include_router(tasks.router, prefix='/api/tasks', tags=['Tasks'])