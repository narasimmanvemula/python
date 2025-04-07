"""
Course Management System using Singleton Database Connection.

- Uses the singleton database connection from singleton_db.py.
- Provides methods to create tables, insert data, fetch, update, and delete courses.

"""

from singleton_db import DatabaseConnection

class CourseManager:
    """Handles Course CRUD operations using the Singleton DB connection."""

    def __init__(self):
        self.db = DatabaseConnection()  # Get the singleton instance
        self.cursor = self.db.get_cursor()
        self.create_table()

    def create_table(self):
        """Creates the courses table if it does not exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                instructor TEXT NOT NULL,
                duration INTEGER NOT NULL
            )
        """)
        self.db.commit()

    def add_course(self, name, instructor, duration):
        """Inserts a new course into the database."""
        self.cursor.execute("INSERT INTO courses (name, instructor, duration) VALUES (?, ?, ?)",
                            (name, instructor, duration))
        self.db.commit()
        print(f"Course '{name}' added successfully.")

    def get_courses(self):
        """Fetches all courses from the database."""
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()

    def delete_course(self, course_id):
        """Deletes a course by ID."""
        self.cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        self.db.commit()
        print(f"Course with ID {course_id} deleted.")

    def close_connection(self):
        """Closes the database connection."""
        self.db.close()

# Example Usage
if __name__ == "__main__":
    manager = CourseManager()
    manager.add_course("Python Programming", "Arun", 6)
    manager.add_course("Machine Learning", "Bala", 8)

    print(manager.get_courses())  # Fetch all courses
    manager.delete_course(1)  # Delete course with ID 1

    manager.close_connection()
