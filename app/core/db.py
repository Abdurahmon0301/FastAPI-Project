from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite (lokal fayl)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# PostgreSQL uchun:
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Faqat SQLite uchun
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
