def multiplication(a,mul):
    for i in range(0,len(a)):
        mul=mul*a[i]
    return mul    

mul=1
n=int(input("HOW MANY NUMBER DO YOU MULTIPLY:"))
a=[]
for i in range(n):
    a.append(int(input(f"ENTER NUMBER {i+1}: ")))

print("MULTIPLICATION OF LIST IS THE  ",multiplication(a,mul))
        