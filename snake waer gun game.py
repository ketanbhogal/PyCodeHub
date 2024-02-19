import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='s':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("comp Turn:snake(s) water(w) or gun(g)?")
radNo=random.randint(1,3)
if radNo==1:
    comp='s'
elif radNo==2:
    comp='w'
elif radNo==3:
    comp='g'
    
you=input("your turn:snake(s) water(w) or gun(g)?")
a=gamewin(comp,you)

print(f"computer choose:{comp}")
print(f"you choose:{you}")

if a==None:
    print("MATCH IS TIE")  
elif a:
    print("YOU ARE WIN THE MATCH")
else:
    print("YOU LOOSE THE MATCH")