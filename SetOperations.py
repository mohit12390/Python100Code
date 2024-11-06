s1 = {1,2,3,6,4,5}
s2 = {6,4,5}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s2.difference(s1))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
s1.update(s2)
print(s1)

s3 = {8,9,19}
s1.update(s3)
print(s1)

s1.add(29)
print(s1)
try:
    s1.remove(28)
except KeyError:
    print("Element not present ")

s1.pop()
print(s1)

# s1.clear()
print(s1)
