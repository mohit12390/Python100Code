# def factorial(num):
#     if num == 0 or num ==1:
#         return 1
#     else:
#         return num * factorial(num-1)
#
# print(factorial(6))

# def sum(num):
#     sum = 0
#     while (num > 0):
#
#         sum += num
#         num -= 1
#     print("The sum is", sum)
#
#
# sum(6)

# Python program to display the Fibonacci sequence

def Fibo(n):
   if n <= 1:
       return n
   else:
       return(Fibo(n-1) + Fibo(n-2))
n = int(input("ENter a number "))

for i in range(n):

    print(Fibo(i), end=' ')