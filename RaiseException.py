
a = input("Enter any number ")

if a == "quit":
    print("yes")
elif int(a)<5 or int(a)>9:
    raise ValueError("Value should be between and 5 and 9")

print("Hey wahtsup")