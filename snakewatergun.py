import random

def game(comp,you):
    if(comp==you):
        print("!!! match is tie !!!")
    elif(comp=='s'and you=='w'):
        print("$$$ comp is win $$$")
    elif(comp=='w'and you=='s'):
        print("$$$ You are win $$$")
    elif(comp=='s'and you=='g'):
         print("$$$ You are win $$$")
    elif(comp=='g'and you=='s'):
         print("$$$ comp is win $$$")
    elif(comp=='g'and you=='w'):
         print("$$$ You are win $$$")
    elif(comp=='w'and you=='g'):
         print("$$$ comp is win $$$")
           



print("Comp Turn: Snake(s),Water(w),Gun(g):: ")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
you=print(input("Your Turn: Snake(s),Water(w),Gun(g):: "))
game(comp,you)