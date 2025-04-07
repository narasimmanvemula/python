

"""
Singleton Pattern for Course Management.

✅ Ensures only one instance – Prevents multiple conflicting instances.
✅ Used for centralized management – Ideal for managing courses, configs, logs, etc.
✅ Efficient memory usage – Prevents unnecessary object creation.

Real-World Use Cases of Singleton

-  Database Connections – Ensures only one connection is used throughout the app.
-  Logging Systems – Centralized logging across the application.
-  Configuration Managers – Loads settings once and shares across components.
-  Cache Managers – Keeps data in memory to improve performance.

"""

class CourseManager:
    """Singleton class for managing course registrations."""

    _instance = None  # Class attribute to store the singleton instance

    def __new__(cls):
        """Ensures only one instance of CourseManager exists."""
        if cls._instance is None:
            cls._instance = super(CourseManager, cls).__new__(cls)
            cls._instance.courses = []  # Initialize the list of courses
        return cls._instance

    def add_course(self, course_name):
        """Adds a course to the course list."""
        self.courses.append(course_name)
        print(f"Added course: {course_name}")

    def get_courses(self):
        """Returns the list of courses."""
        return self.courses

# Example Usage
manager1 = CourseManager()
manager2 = CourseManager()

manager1.add_course("Python Programming")
manager2.add_course("Machine Learning")

print(manager1.get_courses())  # Output: ['Python Programming', 'Machine Learning']
print(manager2.get_courses())  # Output: ['Python Programming', 'Machine Learning']
print(manager1 is manager2)  # Output: True (Both variables reference the same instance)
