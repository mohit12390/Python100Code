list = []

number = int(input("Enter an number \n"))

for i in range(1,11):
    # print(f"{number} x i = {number * i}")
    list.append(number*i)

print(list)

for i in list:
    print(i)