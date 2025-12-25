def fib(n):
    a,b =0,1        #in  fibonacci series satrts with 0 , 1,1, 2, 3,5,8,13 .....
    fib =[]         # to store the elements in a sequence of list []
    for i in range (n):
        fib.append(a) #adding the a value to the end of the list fib[]  --> 0,1,1,2
        a,b =b,a+b      # replacing the b value to the a and valuse of a+b to the = b
    return fib
n = int (input())
print(fib(n))