def is_prime(n):
    count =0
    if n<=1:
        return "its not a prime number"
    for i in range(2,n):
        if n % i ==0 :
            count +=1
    if count >=2 :
        print("this is not a prime number ")
    else :
        print("prime number")
n = int (input (" enter a number to check whether the number is prime or not "))
is_prime(n)