# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product*(i+1)
#     return product

# print(factorial_iter(5))


def factorial_recursion(n):
    if n==0 or n==1:
        return 1

    return n*factorial_recursion(n-1)
f=factorial_recursion(5)
print(f)