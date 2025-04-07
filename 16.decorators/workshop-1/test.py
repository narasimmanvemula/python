def lowercase(func):
    def modify():
        x = func()
        return x.lower()
    return modify

@lowercase
def _words():
    return "HELLO World !"

result = _words()
print(result)
