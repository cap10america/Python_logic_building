import time 

def binary_search(arr , target ):
    start=time.time()
    left =0 
    right = len(arr)-1
    while left<= right:
        mid = left + (right- left)//2 
        if arr[mid ]==target :
            return mid
        elif (arr[mid]<target):
            left = mid+1
        else :
            right = mid-1
    end=time.time()
    print(f"Time taken to execute the binary search is : {end-start} seconds")          
    return "not found/target is not in array " 
n = int(input("Enter the target value to search : "))
print(binary_search([1,5,9,87,98,101,201,300,401,501,8888,] ,n))
            

                
            
             
        
        