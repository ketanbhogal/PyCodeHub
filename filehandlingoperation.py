# f=open("a.txt","r")
# data=f.read()
# data=f.read(10) #this is only read the 10 character
# data=f.readline()   #this is only read the one line character
# print(data)


# f=open("a.txt","w")
# f.write("my college name is anantrao pawar college of engineering and research pune")
# f.close

with open ("a.txt") as f:
    content=f.read()
content=content.replace("my","our")
with open("a.txt",'w') as f:
    f.write(content)   
