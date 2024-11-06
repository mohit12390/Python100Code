# import random
# import string
#
# characters = random.choices(string.ascii_letters.lower()  , k=3)
# characters=  ''.join(characters)
#
# characters1 = random.choices(string.ascii_letters.lower()  , k=3)
# characters1=  ''.join(characters1)
# # print(characters)
#
# str = input("Enter an string to")
# coding = True
#
# if coding:
#     if len(str) > 3:
#         str = characters + str[1:] + str[0] + characters1
#         print(str)
# else:
#     pass

coding = input("1 for coding or 0 for decoding ")

coding = True if coding == "1" else False
print(coding)
