"""def sum_num(n):
    if n<=0:
        return 0
    print ((n*(n+1))//2)
n = int (input())
sum_num(n)
"""
def sum_num(n):
    print(sum(range(1,n+1)))
n= int(input("enter the num to know the sum of valuse upto n"))
sum_num(n)