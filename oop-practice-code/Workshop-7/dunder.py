# Dunder (Double Underscore) methods allow objects to behave like built-in Python types.

class Course:
    """Represents a course with special dunder methods."""

    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration
        self.students = []

    def enroll_student(self, student_name):
        """Enrolls a student in the course."""
        self.students.append(student_name)

    def __str__(self):
        """Defines how the object is printed."""
        return f"{self.name} taught by {self.instructor}, {self.duration} weeks."

    def __len__(self):
        """Returns number of enrolled students."""
        return len(self.students)

    def __eq__(self, other):
        """Compares two courses by name and instructor."""
        if isinstance(other, Course):
            return self.name == other.name and self.instructor == other.instructor
        return False

# Example Usage
course1 = Course("Python", "Arun", 6)
course2 = Course("Python", "Arun", 6)
course3 = Course("Machine Learning", "Bala", 10)

print(course1)  # Calls __str__: Output → Python taught by Arun, 6 weeks.
print(len(course1))  # Calls __len__: Output → 0 (no students yet)
print(course1 == course2)  # Calls __eq__: Output → True
print(course1 == course3)  # Output → False
