from sqlalchemy.orm import Session
from core.models import Post, Comment
from schema.schema import PostBase

def get_posts(db: Session):
    return db.query(Post).all()

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()

# def create_user(db: Session, user: UserCreate):
#     hashed_password = f"hashed_{user.password}"  # Haqiqiy loyihada hash qiling!
#     db_user = User(
#         email=user.email,
#         name=user.name,
#         hashed_password=hashed_password
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def delete_user(db: Session, user_id: int):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user:
#         db.delete(user)
#         db.commit()
#         return True
#     return False

# # Post CRUD
# def get_posts(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Post).offset(skip).limit(limit).all()

# def create_post(db: Session, post: PostCreate, user_id: int):
#     db_post = Post(**post.dict(), author_id=user_id)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post

# def get_user_posts(db: Session, user_id: int):
#     return db.query(Post).filter(Post.author_id == user_id).all()