# Static Method
# Static methods are methods that are bound to a class rather than its object. They do not require a class instance to be called. They are defined using the @staticmethod decorator.

"""
✅ A static method is a method that belongs to a class, not an instance.
✅ It does not require access to instance (self) or class (cls) variables.
✅ It is defined using the @staticmethod decorator.
✅ Typically used for utility functions that do not modify instance or class data.
"""

class Course:
    total_courses = 0  # Class variable to track course count

    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration
        Course.total_courses += 1  # Increase count when a course is created

    @classmethod
    def get_total_courses(cls):
        return f"Total courses available: {cls.total_courses}"

    @staticmethod
    def university_info():
        return "Welcome to XYZ University!"

# Creating courses
course1 = Course("Data Science", "Dr. Lee", 12)
course2 = Course("Cybersecurity", "Mr. Adams", 10)

# Using class method
print(Course.get_total_courses())

# Using static method
print(Course.university_info())
