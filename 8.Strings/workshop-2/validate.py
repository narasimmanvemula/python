text = "Hello123"
print(text.isalpha())  # Output: False (checks if all characters are alphabets)
print(text.isdigit())  # Output: False (checks if all characters are digits)
print(text.isalnum())  # Output: True (checks if all characters are alphanumeric)

text = "   Hello, World!   "
print(text.strip())  # Output: Hello, World! (removes leading and trailing whitespace)
print(text.rstrip())  # Output:    Hello, World! (removes trailing whitespace)
print(text.lstrip())  # Output: Hello, World!    (removes leading whitespace)

text = "Hello, World!"
print(text.partition(","))  # Output: ('Hello', ',', ' World!') (splits into three parts based on the first occurrence)
print(text.rpartition(","))  # Output: ('Hello, World!', ',', '') (splits into three parts based on the last occurrence)
