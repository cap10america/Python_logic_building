def is_fact(n):
    if n<0 : 
        raise ValueError("Negative input not allowed")
    if n==0 :
        return 1
    return n * is_fact(n-1)
n = int(input("enter a number to check the factorial of number" ))
print(is_fact(n))