from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from services.note_service import PostService
from databases.database import SessionLocal, engine
from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str
    user_id: int


router = APIRouter()
PostService = PostService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_notes(post: NoteBase, db: Session = Depends(get_db)):
    return PostService.create_notes(db, post)


@router.get("/get/{post_id}", status_code=status.HTTP_200_OK)
async def read_notes(post_id: int, db: Session = Depends(get_db)):
    return PostService.get_notes(db, post_id)


@router.put("/update/{post_id}", status_code=status.HTTP_200_OK)
async def update_notes(post_id: int, post: NoteBase, db: Session = Depends(get_db)):
    return PostService.update_notes(db, post_id, post)


@router.delete("/delete/{post_id}", status_code=status.HTTP_200_OK)
async def delete_notes(post_id: int, db: Session = Depends(get_db)):
    return PostService.delete_notes(db, post_id)
