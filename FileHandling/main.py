
# try:
#     f = open("Hello.txt","r")
#     print(f.read())
# except IOError as err:
#     print(err)
#
# finally:
#     print("Hello you caome in finally block")
#     f.close()

# f = open("Viraj.txt","a")
# f.writelines("\n nivhe aata kya  ")
# print()
# f.close()

# with open("Viraj.txt","r") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)

with open("Kirti.txt","w") as f:
    lines = ['line1\n','line2\n','line3\n']
    f.writelines(lines)
    f.close()