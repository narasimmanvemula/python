class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration
        self.students = []  
        self.completed = False  

    def enroll_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has enrolled in {self.name}")

    def mark_completed(self):
        self.completed = True
        print(f"{self.name} has been completed.")

    def get_details(self):
        return f"Course: {self.name}, Instructor: {self.instructor}, Duration: {self.duration} weeks, Students: {self.students}, Completed: {self.completed}"

class OnlineCourse(Course):
    def __init__(self, name, instructor, duration, platform):
        # Inherit attributes from Course
        super().__init__(name, instructor, duration)  
        self.platform = platform

    def get_details(self):
        return f"{super().get_details()}, Platform: {self.platform}"

# Creating an Online Course instance
online_python = OnlineCourse("Advanced Python", "Arun", 8, "Udemy")

# Enrolling a student
online_python.enroll_student("Dinesh")

# Display details
print(online_python.get_details())
