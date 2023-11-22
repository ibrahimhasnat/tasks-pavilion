from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Optional
import uuid

router = APIRouter()

# In-memory data store for simplicity
tasks = []

class Task(BaseModel):
    id: Optional[str]
    title: str
    description: str = None
    priority: str = None
    label: str = None
    due_date: Optional[str] = None
    status: Optional[str] = None

class TaskCreate(BaseModel):
    title: str
    description: str = None
    priority: str = None
    label: str = None
    due_date: Optional[str] = None
    status: Optional[str] = None

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    try:
        new_task = Task(id=str(uuid.uuid4()), **task.dict())
        tasks.append(new_task)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/", response_model=List[Task])
def read_all_tasks():
    return tasks

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: str, updated_task: TaskCreate):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            # Update specific fields
            if updated_task.title is not None:
                tasks[i].title = updated_task.title
            if updated_task.description is not None:
                tasks[i].description = updated_task.description
            if updated_task.priority is not None:
                tasks[i].priority = updated_task.priority
            if updated_task.label is not None:
                tasks[i].label = updated_task.label
            if updated_task.due_date is not None:
                tasks[i].due_date = updated_task.due_date
            if updated_task.status is not None:
                tasks[i].status = updated_task.status

            return tasks[i]

    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: str):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            deleted_task = tasks.pop(i)
            return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.get("/labels/{label}", response_model=List[Task])
def read_tasks_by_label(label: str):
    filtered_tasks = [task for task in tasks if task.label == label]
    return filtered_tasks

@router.get("/priorities/{priority}", response_model=List[Task])
def read_tasks_by_priority(priority: str):
    filtered_tasks = [task for task in tasks if task.priority == priority]
    return filtered_tasks