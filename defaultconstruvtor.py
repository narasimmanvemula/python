class Course:
    # Default Constructor
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor 
        self.duration = duration

    def get_details(self):
        return f"Course: {self.name}, Instructor: {self.instructor}, Duration: {self.duration} weeks"

# Creating objects (instances of the Course class)
python_course = Course("Python Programming", "Arun", 6)
ml_course = Course("Machine Learning", "Bala", 8)
ds_course = Course("Algorithms", "Balasubramanium", 10)

# Accessing methods
print(python_course.get_details())  
print(ml_course.get_details())
print(ds_course.get_details())
