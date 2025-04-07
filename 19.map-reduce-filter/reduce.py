import functools

print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))
# 113

"""

reduce(func, seq)

Continually applies the function func() to the sequence seq. 
It returns a single value.

"""
