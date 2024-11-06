marks = [10,50,90,98,1,2,45,54]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("This is my marks ")
#     index += 1
    # if mark[index] ==3:
    #     print("I am cool")

for index,mark in enumerate(marks):
    if index == 3:
        print(f"The Index position is {index} and marks is {mark}")