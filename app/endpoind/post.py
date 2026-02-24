from sqlalchemy.orm import Session
from core.db import get_db
from core.models import User, Post
from schema.schema import PostBase
from fastapi import Depends, FastAPI, APIRouter, HTTPException
post_router = APIRouter()

@post_router.post("/create_post", tags=["Posts"])
def Create(post: PostBase, db: Session = Depends(get_db)):
    new_post = Post(
        title = post.title,
        content = post.content  
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@post_router.get("/posts", tags=["Posts"])
def Read(db: Session = Depends(get_db)):
    return db.query(Post).all()


@post_router.put("/update_post", tags=["Posts"])
def update(post_id: int, post: PostBase, db: Session = Depends(get_db)):

    item = db.query(Post).filter(Post.id == post_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Post not found")

    item.title = post.title # type: ignore
    item.content = post.content # type: ignore

    db.commit()
    db.refresh(item)

    return {"message": "Updated", "data": item}


@post_router.delete("/delete_post", tags=["Posts"])
def Delete(post_id: int, db: Session = Depends(get_db)):
    item = db.query(Post).filter(Post.id == post_id).first()
    if item == None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(item)
    db.commit()
    return {"message":"O'chirildi!"}