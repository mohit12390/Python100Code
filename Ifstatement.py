# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("I am an Male and Tall ")
# elif is_male or is_tall:
#     print("I am an male or tall ")
# else:
#     print("I am nothing ")

while True:
    print("-------------------------------------")
    print("+ for addition ")
    print("- for subtraction ")
    print("* for multiplication")
    print("/ for division ")
    print("% for modulus ")
    print("-------------------------------------")
    num1 = int(input("Please enter  your first number !!\n"))
    op = input("Please enter operator !!\n")
    num2 = int(input("Please enter  your number2 !!\n"))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "%":
        print(num1 % num2)
    else:
        print("Invalid operator ")





