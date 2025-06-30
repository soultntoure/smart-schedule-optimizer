from fastapi import APIRouter
from .endpoints import users, tasks, schedules, subjects, preferences

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(schedules.router, prefix="/schedules", tags=["schedules"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
api_router.include_router(preferences.router, prefix="/preferences", tags=["preferences"])
