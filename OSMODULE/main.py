import os

#get current working directry
# cwd = os.getcwd()
# print("Current working directory:", cwd)
#
# def current_path():
#     print("Current working directory before")
#     print(os.getcwd())
#     print()
# current_path()
# change the directory
# os.chdir('../')
# current_path()
#
# list the directory
# print(os.listdir(current_path()))

os.write("")



# remove the file
# file = 'hello'
# location = "E:\Python_Hindi\pythonProject\OSMODULE"
# path = os.path.join(location, file)
# os.remove(path)

#read the file and handle if not eist
# try:
#     filename = 'hello'
#     f = open(filename, 'r')
#     text = f.read()
#     print(text)
#     f.close()
# except IOError:
#   print('Problem reading: ' + filename)

# create directory and internal dir and file
# if os.path.exists("data"):
#     print("Dir data exist")
# else:
#     os.mkdir("data")
#
# for i in range(1,20):
#     if os.path.exists(f"data/Day{i+1}"):
#         print("cant created directory")
#     else:
#         os.mkdir(f"data/Day{i+1}")
#         file = open(f"data/Day{i+1}/hello{i+1}.txt","w")
#         file.write("kya baat hain ")

# check the size of directory
size = os.path.getsize("data")
print("Size of the file is", size, " bytes.")


# if os.path.exists("data"):
#     os.rmdir("data")
