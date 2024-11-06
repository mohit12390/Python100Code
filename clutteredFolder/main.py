import os

files = os.listdir("E:/Python_Hindi/pythonProject/clutteredFolder")

i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"E:/Python_Hindi/pythonProject/clutteredFolder/{file}", f"E:/Python_Hindi/pythonProject/clutteredFolder/FIle{i}.png")
        i += 1