def is_reverse_signed_int(n):
    sign =1
    if n<0: 
         sign =  -1
    
    n= str(abs(n))[::-1]
    print(sign *int(n))
n = int(input("enter a num to be reverses with sign "))
is_reverse_signed_int(n)