from pydantic import BaseModel

from models.model import User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


class UserBase(BaseModel):
    username: str


class UserService:
    def create_user(self, db: Session, user):
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        return db_user

    def get_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return user

    def update_user(self, db: Session, user_id: int, user: UserBase):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail='User not found')
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        return db_user

    def delete_user(self, db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail='User not found')
        db.delete(db_user)
        db.commit()
        return db_user
