def gcd(x,y):
    while y !=0 :
        x = y
        y=x%y
    #return  abs(x)
    print(abs(x))
x = int(input("enter x value : "))
y = int(input("and y value : for gcd "))
gcd(x,y)