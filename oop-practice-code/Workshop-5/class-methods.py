# Add methods: Enrollment, Completion

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

# Creating an instance
ai_course = Course("AI & ML", "Dr. Prasad", 10)

# Enrolling students
ai_course.enroll_student("Arun")
ai_course.enroll_student("Balaji")

# Mark course as completed
ai_course.mark_completed()

# Display course details
print(ai_course.get_details())
