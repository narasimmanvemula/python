import re

# Pattern matching and search
text = "Hello, my name is Alice."
pattern = r"\b[A-Z][a-z]+\b"  # Matches capitalized words
matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'Alice']

# String substitution using regex
new_text = re.sub(pattern, "John", text)
print(new_text)  # Output: John, my name is John.
