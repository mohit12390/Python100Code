# MAP
from functools import reduce


def cube(x):
    return x * x* x

# print(cube(3))
# list = []
l = [3,6,9,12,15,18,21]
# for i in l:
#     list.append(cube(i))
newl = list(map(cube,l))
# print(newl)

# FILTER
filter_function = lambda x: x % 2 == 0

newnewl = list(filter(filter_function, l))
print(newnewl)


sum = reduce(lambda x,y : x + y , l)
print(sum)