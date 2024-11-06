import random
while True:
    comp =(random.randint(0,2))
    # print(comp)
    user = int(input("0 for Snake , 1 for water and 2 for Gun\n"))

    def check(comp,user):
        if comp == user:
            return 0
        elif (comp ==0 and user ==1):
            return -1
        elif (comp ==1 and user ==2):
            return -1
        elif (comp == 2 and user == 0):
            return -1

        return 1

    score = check(comp,user)

    print("comp choice", comp)
    print("User choice ", user )

    if score == 0:
        print("Draw")
    elif score == -1:
        print("You loose ")
        break
    else:
        print("you Win !!")