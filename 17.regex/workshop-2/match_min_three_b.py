import re
def text_match(text):
        patterns = 'ab{3}?'
        # Match two or three ab s
        # patterns = 'ab{2,3}?'

        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("abbb"))
print(text_match("aabbbbbc"))