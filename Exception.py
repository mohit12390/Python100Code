# try:
#     # a = 10 / 0
#     name = "Mohit"
#     # number = int(input("Enter a number :"))
#     # print(number)
#     print(name[5])
# except IndexError as err:
#     print(err)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

l = [1,2,3]
try:
    num = int(input("Enter a nyumber \n"))
    print(l[num])
except ValueError as err:
    print(err)
except IndexError as err:
    print(err)
finally:
    print("Hey buddy ")