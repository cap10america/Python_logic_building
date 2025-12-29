def missing_num(arr , n):
    return n* (n+1 )//2 -sum(arr)
n = int(input("enter a number "))
user_input =input("enter a number in array ")
arr = [int(x) for x in user_input.split()]
print(missing_num(arr ,n))

