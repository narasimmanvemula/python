"""
✅ Hides unnecessary details (students don’t need to know how a course is delivered, just that it exists).
✅ Forces child classes to implement required methods (get_details() must be defined in every course type).
✅ Improves maintainability (easier to add new types of courses without modifying existing code).
"""

"""
Abstraction in Python - Course Management System.

- Uses ABC (Abstract Base Class) to define a generic Course structure.
- Concrete classes (OnlineCourse, OfflineCourse) must implement abstract methods.

"""

from abc import ABC, abstractmethod

class Course(ABC):
    """Abstract Base Class for all Courses."""

    def __init__(self, name, instructor, duration):
        """Initialize course attributes."""
        self.name = name
        self.instructor = instructor
        self.duration = duration

    @abstractmethod
    def course_mode(self):
        """Abstract method to define course mode (online/offline)."""
        pass  # Must be implemented in child classes

    @abstractmethod
    def get_details(self):
        """Abstract method to get course details."""
        pass  # Must be implemented in child classes

# Concrete class 1: Online Course
class OnlineCourse(Course):
    """Concrete implementation for an online course."""

    def __init__(self, name, instructor, duration, platform):
        super().__init__(name, instructor, duration)
        self.platform = platform

    def course_mode(self):
        """Defines the course mode as Online."""
        return "Online"

    def get_details(self):
        """Returns course details."""
        return f"{self.name} by {self.instructor}, {self.duration} weeks, Platform: {self.platform}"

# Concrete class 2: Offline Course
class OfflineCourse(Course):
    """Concrete implementation for an offline course."""

    def __init__(self, name, instructor, duration, location):
        super().__init__(name, instructor, duration)
        self.location = location

    def course_mode(self):
        """Defines the course mode as Offline."""
        return "Offline"

    def get_details(self):
        """Returns course details."""
        return f"{self.name} by {self.instructor}, {self.duration} weeks, Location: {self.location}"

# Example Usage
online_python = OnlineCourse("Python Programming", "Arun", 6, "Udemy")
offline_ml = OfflineCourse("Machine Learning", "Bala", 8, "NYC Campus")

print(online_python.get_details())  # Python Programming by Arun, 6 weeks, Platform: Udemy
print(offline_ml.get_details())  # Machine Learning by Bala, 8 weeks, Location: NYC Campus
