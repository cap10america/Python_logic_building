# def two_sum(arr , target ):
#     temp =0
#     for  i in range(len(arr)):
#         if arr[i] != target - arr[temp]  :
#             temp = i
#             i +=1 # the dead code doestnt affect the loop 
#         else :
            
#             return  i , temp 
            
#         return "not found " ,i ,temp
    
# print(two_sum([1,2,3,4,5,6,7,8,9], 12))

"""this is working code for this only one occurences of the elements using hashmap data structure --> seen{}
    """
# def two_sum(arr, t):
#     seen={}
#     for i , val in enumerate(arr):
#          diff = t -val
#          if diff in seen :
#              return [seen[diff],i]
#          seen[val]=i
# print(two_sum([1,2,3,4,5,6,7,8,9], 12))      



def two_sum_list(arr ,t):
    list=[]
    seen ={}
    for i ,n in enumerate(arr):
        diff = t - n 
        if diff in seen:
             list.append([seen[diff],i])
        seen[n]=i
    return list
print(two_sum_list([1,2,3,4,5,6,7,8,9], 12))
        

        