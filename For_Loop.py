# num = int(input("Enter an no to find tables \n"))
# for i in range(1,11):
#     print(f"{num}*{i} = ",i*num )

names = ["Mohit","Rajan"]
for i in names:
    for j in i:
        # print(j)
        if j.upper() in 'AEIOUaeiou':
            print(f"The character is vowel {j}")

for i in range(1,11,1):
     print(i)