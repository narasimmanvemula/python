# dictionary_operations.py

# 1. Creating a Dictionary
student = {
    "first name": "Arun",
    "age": 23,
    "courses": ["Math", "Science"]
}

print("Initial Dictionary:", student)

# 2. Accessing Values
print("\nAccessing Values:")
print("Name:", student["first name"])                      # Direct access
print("Age using get():", student.get("age"))         # Using get method
print("Grade (default if missing):", student.get("grade", "Not Available Yet"))

# 3. Adding or Updating Values
print("\nAdding or Updating Values:")
student["grade"] = "A"                                # Add new key-value
student["age"] = 24                                   # Update existing value
print("Updated Dictionary:", student)

# 4. Removing Items
print("\nRemoving Items:")
removed_grade = student.pop("grade", "N/A")           # Removes and returns value
print("Removed Grade:", removed_grade)
del student["age"]                                    # Delete age key-value pair
print("Dictionary after deletion:", student)

# Using popitem to remove the last item
last_item = student.popitem()                         # Removes last inserted item
print("Last item removed:", last_item)
print("Dictionary after popitem:", student)

# 5. Looping Through a Dictionary
print("\nLooping Through Dictionary:")
for key in student:
    print("Key:", key)
for value in student.values():
    print("Value:", value)
for key, value in student.items():
    print(f"{key}: {value}")

# 6. Checking for Keys
print("\nChecking for Keys:")
if "name" in student:
    print("Key 'name' exists in dictionary.")

# 7. Dictionary Comprehensions
print("\nDictionary Comprehensions:")
squares = {x: x*x for x in range(1, 6)}
print("Squares Dictionary:", squares)

# 8. Merging Dictionaries
print("\nMerging Dictionaries:")
student.update({"age": 25, "year": "Senior"})         # Using update method
print("Dictionary after update:", student)

# Using dictionary unpacking
new_student = {**student, "grade": "B"}
print("New Dictionary with unpacking:", new_student)

# 9. Dictionary Methods
print("\nDictionary Methods:")
print("Keys:", student.keys())                        # Get all keys
print("Values:", student.values())                    # Get all values
print("Items:", student.items())                      # Get all key-value pairs

# 10. Clearing the Dictionary
print("\nClearing Dictionary:")
student.clear()                                       # Clear all i
