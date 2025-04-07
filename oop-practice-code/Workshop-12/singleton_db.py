"""
Singleton Database Manager with .env Configuration.

- Loads database name from .env file.
- Uses Singleton to ensure a single database connection.
- Supports basic CRUD operations.

"""

import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    """Singleton class for managing SQLite database connections."""

    _instance = None  # Stores the single instance

    def __new__(cls):
        """Ensures only one database connection exists."""
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            db_name = os.getenv("DATABASE_NAME", "default.db")  # Load from .env
            cls._instance.connection = sqlite3.connect(db_name, check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def get_cursor(self):
        """Returns the cursor for executing queries."""
        return self.cursor

    def commit(self):
        """Commits changes to the database."""
        self.connection.commit()

    def close(self):
        """Closes the database connection."""
        self.connection.close()
        print("Database connection closed.")

# Test Singleton Behavior
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1 is db2)  # Output: True (Both reference the same instance)
