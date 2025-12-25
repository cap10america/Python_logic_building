def brk_cnt(n):
    il=[]
    for i in range(1,n+1):
        if (n%i == 0):
            il.append(i)
            break
        
    print(il)
        
n = int( input("enter a num to explain break and continue"))
brk_cnt(n)
# def brk_cnt(n):
#     il=[]
#     for i in range(1,n+1):
#         if (n%i == 0):
#             continue
#         il.append(i)
#     print(il)
        
# n = int( input("enter a num to explain break and continue"))
# brk_cnt(n)