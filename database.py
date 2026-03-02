from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # <-- Loads your .env

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No database URL found. Make sure DATABASE_URL environment variable is set.")

engine = create_engine(
    DATABASE_URL,
    echo=True,  
    pool_pre_ping=True,
    pool_recycle=300,   
    pool_size=5,        
    max_overflow=10
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
