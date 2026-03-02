from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
load_dotenv()  # <-- Loads your .env

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No database URL found. Make sure DATABASE_URL environment variable is set.")

engine = create_engine(
    DATABASE_URL,
    echo=True,  
    # Since you are using pgbouncer (port 6543), 
    # it's best to let Supabase handle the pooling.
    poolclass=NullPool, 
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
