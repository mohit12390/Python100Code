# with open("Kirti.txt","r") as file:
#     # print(file)
#     # switch to some line
#     file.seek(10)
#     print(file.tell())
#     print(file.read(10))

with open("Kirti.txt", "w") as file:
    file.write("Mohit Gangil")
    file.truncate(5)