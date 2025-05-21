from fastapi import FastAPI
from user_controller.users_routes import router as user_router
from task_controller.task_routes import router as task_router

app = FastAPI()

# Include the routers
app.include_router(user_router)
app.include_router(task_router)
