even_nunbers = [2, 4, 6, 810, 34]
print(even_nunbers)

print(type(even_nunbers[-1]))

# slicing operations
print(even_nunbers[0:2]) #2 4 
print(even_nunbers[1:])  #4 6 810 34
print(even_nunbers[-4:-2]) # why not 6 only? # 4 6

# index operations
print(type(even_nunbers[2]))
del even_nunbers[2]
print(even_nunbers)

even_nunbers[0] = 2345
# [2345, 4, 6, 810]
print(even_nunbers)

odd_nunbers = [1,3,5,7,9]
even_nunbers.append(234)
all_numbers = even_nunbers # why it is not working ?
# [2345, 4, 6, 810, 3456]
print(all_numbers)

print(len(odd_nunbers + even_nunbers))

# Merge the contents even_nunbers, odd_nunbers ?
print(even_nunbers + odd_nunbers + even_nunbers)
