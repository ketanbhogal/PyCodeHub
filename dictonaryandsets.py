# create dictonary by symbol {}
# dictonary is created as per key and value terms 1st term is key and 2nd is value 
mydict={
    "fast":"speed is fast",
    "slow":"speed is slow",
    "vision":"this is vision ", 
    "list":[1,2,3,4,5,6,7,8,9]
}
print(mydict['fast'])
print(mydict['list'])
print(list(mydict.keys())) 
print(list(mydict.values())) 


update={
    "lovish":"friend",
    "divya":"friend"
}
mydict.update(update)
print(mydict)

print(mydict.get['fast']) #use of the .get is this is return none either element is not present in dictonary
 