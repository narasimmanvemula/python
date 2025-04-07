fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
# [1, 1, 3, 5, 13, 21, 55]

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
# [0, 2, 8, 34]


# or alternatively:

even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)
# [0, 2, 8, 34]


"""

filter(function, sequence)

Offers a simple way to filter out all the elements of a sequence "sequence", for which the function function returns True. i.e. an item will be produced by the iterator result of filter(function, sequence) if item is included in the sequence "sequence" and if function(item) returns True.

"""
