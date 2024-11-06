
def merafunc(fx, value):
    return 6 + fx(value)

square = lambda x : x * x
cube = lambda x: x * x * x
addition = lambda x: x + x

# print(square(6))
# print(cube(3))
# print(merafunc(addition,3))
print(merafunc(lambda x: x ** x,4))