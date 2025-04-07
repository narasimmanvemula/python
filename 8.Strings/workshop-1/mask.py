text = "Hello"
padded_text = text.ljust(10)  # Left-justify with padding
print(padded_text)  # Output: Hello     (total length is 10)

padded_text = text.rjust(10, "*")  # Right-justify with custom padding character
print(padded_text)  # Output: *****Hello (total length is 10)

centered_text = text.center(10, "-")  # Center-align with custom padding character
print(centered_text)  # Output: --Hello--- (total length is 10)


