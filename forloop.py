fruit=["banana","mango","pineapple","grapes","chikku","orange","watermelon","leamon","custerdapple","guava"]
for item in fruit:
    print(item)
# this is simple print the number    
for i in range (5,8):
    print(i)
    
# print number step by step by between 2
for i in range (0,100,2):
    print(i)
else:
    print("this loop is end")
    
# else statement is only run after when for loop is successfully run
for i in range (0,10):
    if(i==5):
        break
    print(i)
    
else:
    print("this loop is end")
# else statement is not run beacuase loop is run successfully



# with the help of continue statement we skip the value
for i in range (0,10):
    if(i==5):
        continue
    print(i)
    
else:
    print("this loop is end")
    
# pass is null statement in python is instruct do nithing
for i in range (0,10):
    if(i==5):
        pass