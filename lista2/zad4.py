def product_of(n, m):
    """Oblicza iloczyn dwóch podanych liczb m, n przy użyciu operatorów dodawania i odejmowania za pomocą rekurencji."""
    if n == 1:
        return m
    elif n == 0 or m == 0:
        return 0
    elif n > 1: 
        n -= 1   
        return m + product_of(n,m)
    elif n < 1:
        n += 1   
        return -(m + product_of(n,-m))


print(product_of(23,767),"=", 23*767)
print(product_of(56,21),"=",56*21)
print(product_of(4,9),"=", 4*9)
print(product_of(23,-10),"=", 23*(-10))
print(product_of(-7,44),"=", -7*44)
print(product_of(0,44),"=", 0*44)
print(product_of(-7,0),"=", -7*0)
print(product_of.__doc__)