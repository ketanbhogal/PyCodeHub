# m1=int(input("enter the subject marks"))
# m2=int(input("enter the subject marks"))
# m3=int(input("enter the subject marks"))
# m4=int(input("enter the subject marks"))
# m5=int(input("enter the subject marks"))
# a=(m1+m2+m3+m4+m5)/5
# print(a)
# if(a<35):
#     print("**** THE RESULT OF STUDENT IS THE FAIL *****")
# else:
#     if(a>35 and a<50):
#         print("**** THE RESULT OF STUDENT IS THE PASS WITH C GRADE *****")
#     else:
#         if(a>50 and a<75):
#             print("THE RESULT OF STUDENT IS THE PASS WITH B GRADE *****")
#         else:
#             if(a>75 and a<=100):
#                 print("THE RESULT OF STUDENT IS THE PASS WITH A GRADE *****")
                
a=[]
sum=0
for i in range(0,5):
    a.append(int(input(f"enter marks of subject {i+1}: ",)))
for i in range(0,5):
    sum=sum+a[i]
per=sum/5
print("percentage of a student is :",per)