from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm.session import Session
from typing import List
from endpoind.post import post_router
from endpoind.user import user_router
from core.db import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Allows all headers
)
# Jadvallarni yaratish
Base.metadata.create_all(bind=engine)


@app.get("/", tags=["/"])
def health():
    return {"status":"healthy"}


app.include_router(
    post_router
)
app.include_router(
    user_router
)
