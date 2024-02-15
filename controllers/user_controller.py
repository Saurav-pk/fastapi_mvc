from fastapi import Depends, APIRouter, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from databases.database import SessionLocal
from services.user_service import UserService

router = APIRouter()
UserService = UserService()


class UserBase(BaseModel):
    username: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)


@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    return UserService.update_user(db, user_id, user)


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db, user_id)
