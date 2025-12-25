def sum_digits(n):
     sum=0 
     for i in str(n):
         sum +=int(i)
     print(sum)
     
n = int( input ("enter a digit sum the digit"))
sum_digits(n)