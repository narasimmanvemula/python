# set_operations.py

# 1. Creating a Set
fruits = {"apple", "banana", "cherry", "banana"}  # Duplicate 'banana' will be ignored
print("Initial Set:", fruits)

# 2. Adding Elements
print("\nAdding Elements:")
fruits.add("orange")
print("After adding 'orange':", fruits)

# Adding multiple elements using update
fruits.update(["mango", "grape", "mango"])
print("After adding 'mango' and 'grape':", fruits)

# 3. Removing Elements
print("\nRemoving Elements:")
fruits.discard("banana")  # Removes 'banana' if it exists (no error if it doesn't)
print("After discarding 'banana':", fruits)

# Using remove (raises KeyError if element does not exist)
fruits.remove("apple")
print("After removing 'apple':", fruits)

# Using pop to remove an arbitrary item
popped_fruit = fruits.pop()  # Removes and returns an arbitrary element
print("Popped element:", popped_fruit)
print("Set after pop:", fruits)

# Clearing all elements
fruits.clear()
print("Set after clear:", fruits)

# Re-define the set for the next operations
fruits = {"apple", "banana", "cherry", "mango"}

# 4. Set Operations
vegetables = {"carrot", "potato", "mango", "banana"}

# Union
print("\nSet Operations:")
all_food = fruits | vegetables  # Equivalent to fruits.union(vegetables)
print("Union of fruits and vegetables:", all_food)

# Intersection
common_food = fruits & vegetables  # Equivalent to fruits.intersection(vegetables)
print("Intersection of fruits and vegetables:", common_food)

# Difference
fruit_only = fruits - vegetables  # Equivalent to fruits.difference(vegetables)
print("Difference (fruits only):", fruit_only)

# Symmetric Difference
unique_food = fruits ^ vegetables  # Equivalent to fruits.symmetric_difference(vegetables)
print("Symmetric Difference (unique to each set):", unique_food)

# 5. Checking Membership
print("\nChecking Membership:")
if "apple" in fruits:
    print("'apple' is in the fruits set")

# 6. Set Comprehensions
print("\nSet Comprehensions:")
squares = {x**2 for x in range(1, 6)}
print("Set of squares:", squares)

# 7. Frozen Set (Immutable Set)
print("\nFrozen Set:")
immutable_set = frozenset(["apple", "banana", "cherry"])
print("Frozen set:", immutable_set)

# Trying to add to a frozenset will raise an error
try:
    immutable_set.add("orange")
except AttributeError as e:
    print("Error adding to frozenset:", e)

# 8. Practical Example
print("\nPractical Example:")
# Set of students who attended two different classes
class_A = {"Arun", "Bala", "Charlie", "David"}
class_B = {"Charlie", "David", "Eve", "Frank"}

# Students who attended either class
all_students = class_A | class_B
print("All students (Union):", all_students)

# Students who attended both classes
both_classes = class_A & class_B
print("Students in both classes (Intersection):", both_classes)

# Students who attended only one of the classes
one_class_only = class_A ^ class_B
print("Students in only one class (Symmetric Difference):", one_class_only)

# Students who attended class A but not class B
only_class_A = class_A - class_B
print("Students only in class A (Difference):", only_class_A)
