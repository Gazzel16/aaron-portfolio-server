from sqlalchemy import text
from database import engine  # Import your engine here
import sys

def check_db_connection():
    print("--- Database Connection Check ---")
    try:
        # Establish a connection and execute a simple query
        with engine.connect() as connection:
            # result = 1 if successful
            result = connection.execute(text("SELECT 1"))
            print("✅ Status: SUCCESS")
            print(f"🔗 Database Engine: {engine.url.drivername}")
            print(f"🏠 Host: {engine.url.host or 'localhost'}")
            
    except Exception as e:
        print("❌ Status: FAILED")
        print(f"⚠️  Error Detail: {e}")
        sys.exit(1) # Exit with error code

if __name__ == "__main__":
    check_db_connection()