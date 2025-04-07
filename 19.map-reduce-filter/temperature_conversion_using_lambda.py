C = [39.2, 36.5, 37.3, 38, 37.8] 

F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
# [102.56, 97.7, 99.14, 100.4, 100.03999999999999]

C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)
# [39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]


"""
r = map(func, seq)

The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. Before Python3, map() used to return a list, where each element of the result list was the result of the function func applied on the corresponding element of the list or tuple "seq". With Python 3, map() returns an iterator.


"""