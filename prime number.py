# :;;;;;;;;;;;;;;;;;;;;;PRIME NUMBER:;;;;;;;;;;;;;;;;;;
num=int (input("ENTER THE ANY NUMBER ::\n"))
prime =True
for i in range(2,num):
    if(i%num==0):
        prime=False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")
    
   