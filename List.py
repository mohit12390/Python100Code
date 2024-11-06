names = ["Rajesh","DInkar","Dhinu","Mohit","Mohit"]
# roll_number = [101,102,203,23,24,242,443]
# adding the element in list
names.append("Rajeev")
# insert element at some index
names.insert(2,"Kela")
# remove the element
names.remove("Dhinu")
# merge two list
# names.extend(roll_number)
# clear the list
# names.clear()
# remove the element from last
names.pop()
# check whether element does exist or not
print(names.__contains__("Rajan"))
# revese the list
names.reverse()
print(names)
# count the element
print(names.count("Mohit"))
# sort the list in asc /desc
names.sort(reverse=False)
print(names)

names2 = names.copy()
print(names2)

# names[1] = "Rupal"
# print(names[1:])

# for name in names:
#     print(f"The Name are : {name}")