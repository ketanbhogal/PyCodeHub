def factorial_iter(n):
    product=1
    for i in range(n):
        product=product *(i+1)
        return product
    def factorial_ricursive(n):
        if n==1 or i==0:
            return 1
        return n*factorial_ricursive(n-1)
    
    f=factorial_ricursive(0)
    print(f)