# set is created by the {}
# set is does not print  repeted value
a={1,2,3,5,6,9,8,7,4,5,6,2 }
print(type(a))
print(a)

a.add(44)
a.add(444)
a.add((4,5,6))
# a.add({4:5}) we are cannot add list and dictonary in sets because this is hashable

a.remove(6)
print(a)
b={1,2,3,14,52,36,54,21,21,4,5,6,87,98,99}
print(a.union(b))
print(a.intersection(b))

s={}
# this is not empty set syntax this is the empty dictonary syntax

s=set()
# this is empty set Syntax


