from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
def list_tasks():
    return {"tasks": ["Task A = Grocery", "Task B = Laundry", "Task C = Homework"]}
