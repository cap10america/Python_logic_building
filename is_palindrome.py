def is_palindrome(n):
    str1 =n
    str2 = str1[::-1]
    if str1==str2:
        print("true") 
n = input("enter a string to check a palindrome ")
is_palindrome(n)