"""
Factory Pattern for Course Creation.

- Defines a CourseFactory that dynamically creates different types of courses.
- Abstract class Course ensures all courses follow the same structure.

"""

from abc import ABC, abstractmethod

# Step 1: Define the Abstract Base Class (Parent)
class Course(ABC):
    """Abstract base class for all courses."""

    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    @abstractmethod
    def get_details(self):
        """Abstract method to get course details."""
        pass

# Step 2: Create Concrete Classes for Different Course Types
class OnlineCourse(Course):
    """Represents an online course."""

    def __init__(self, name, instructor, duration, platform):
        super().__init__(name, instructor, duration)
        self.platform = platform

    def get_details(self):
        return f"[Online] {self.name} by {self.instructor}, {self.duration} weeks, Platform: {self.platform}"

class OfflineCourse(Course):
    """Represents an offline (classroom) course."""

    def __init__(self, name, instructor, duration, location):
        super().__init__(name, instructor, duration)
        self.location = location

    def get_details(self):
        return f"[Offline] {self.name} by {self.instructor}, {self.duration} weeks, Location: {self.location}"

# Step 3: Implement the Factory Class
class CourseFactory:
    """Factory class to create Course objects dynamically."""

    @staticmethod
    def create_course(course_type, name, instructor, duration, extra_info):
        """Creates and returns a course based on the type."""
        if course_type == "online":
            return OnlineCourse(name, instructor, duration, extra_info)  # extra_info = platform
        elif course_type == "offline":
            return OfflineCourse(name, instructor, duration, extra_info)  # extra_info = location
        else:
            raise ValueError("Invalid course type! Use 'online' or 'offline'.")

# Example Usage
course1 = CourseFactory.create_course("online", "Python Programming", "Arun", 6, "Udemy")
course2 = CourseFactory.create_course("offline", "Machine Learning", "Bala", 8, "NYC Campus")

print(course1.get_details())  # Output: [Online] Python Programming by Arun, 6 weeks, Platform: Udemy
print(course2.get_details())  # Output: [Offline] Machine Learning by Bala, 8 weeks, Location: NYC Campus
