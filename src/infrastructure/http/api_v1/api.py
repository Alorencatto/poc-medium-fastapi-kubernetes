from fastapi import APIRouter

from src.infrastructure.http.api_v1.endpoints import users

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


router.include_router(users.router)
