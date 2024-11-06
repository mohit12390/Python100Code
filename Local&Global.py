x = 4

def my_func():
    global x
    x = 5
    y = 5
    print("Local variable is ", y)

my_func()
print("Global variable " ,x)