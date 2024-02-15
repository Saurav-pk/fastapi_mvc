from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.model import Notes


class PostService:
    def create_notes(self, db: Session, post):
        db_post = Notes(**post.dict())
        db.add(db_post)
        db.commit()
        return db_post

    def get_notes(self, db: Session, post_id: int):
        post = db.query(Notes).filter(Notes.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=404, detail='Note not found')
        return post

    def update_notes(self, db: Session, post_id: int, post):
        db_post = db.query(Notes).filter(Notes.id == post_id).first()
        if db_post is None:
            raise HTTPException(status_code=404, detail='Note not found')
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        return db_post

    def delete_notes(self, db: Session, post_id: int):
        db_post = db.query(Notes).filter(Notes.id == post_id).first()
        if db_post is None:
            raise HTTPException(status_code=404, detail='Note not found')
        db.delete(db_post)
        db.commit()
        return db_post
