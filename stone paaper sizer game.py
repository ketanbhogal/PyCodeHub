import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='z':
            return False
    elif comp=='p':
        if you=='z':
            return True
        elif you=='s':
            return False
    elif comp=='z':
        if you=='s':
            return True
        elif you=='p':
            return False
print("comp Turn:stone(s) paper(p) or sizer(z)?")
radNo=random.randint(1,3)
if radNo==1:
    comp='s'
elif radNo==2:
    comp='p'
elif radNo==3:
    comp='z'
for i in range (1,50) : 
        you=input("your turn:stone(s) paper(p) or sizer(z)?")
        a=game(comp,you)

        print(f"computer choose:{comp}")
        print(f"you choose:{you}")

        if a==None:
                print("****MATCH IS TIE********")  
        elif a:
                print("******YOU ARE WIN THE MATCH******")
        else:
                print("****YOU LOOSE THE MATCH******")
