def percentage(marks):
    return(sum(marks)/400)*100

marks1=[90,88,85,92]
percentage1=percentage(marks1)

print(percentage1)

# strenger is work as a default parameter
def greet(name="strenger"):
    print("good day "+name)

greet("ketan")
greet()
    