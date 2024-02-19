# def maximum(num1, num2,num3):
#     if(num1>num2):
#        if(num1>num3):
#            return num1
#        else:
#            return num3
#     else:
           
#             if(num2>num3):
#                     return num2
#             else:
#                     return num3
       
# m=maximum(5,30,60)
# print("the gretest value is "+str(m))
def maximum(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3
m=maximum(10,20,30)
print("THE GRETEST NUMBER IS THE::: ",str(m))