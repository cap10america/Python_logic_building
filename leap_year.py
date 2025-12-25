def is_leap_year(n):
    return ( n% 4==0 and n%100 != 0) or( n%400 ==0 )
n = int ( input(" enter the year to find whether its leap year or not " ))

print(is_leap_year(n))