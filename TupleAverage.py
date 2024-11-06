def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum/len(numbers))


average(3,4,5)