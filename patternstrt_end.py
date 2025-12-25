import re 
def pattern_strt_end(str):
    prefix ="hello"
    suffix = "world"
    p=re.escape(prefix)
    s = re.escape(suffix)
    # pattern = r"^hello.*world$"
    pattern = (rf"^{prefix}.*{suffix}$" )
    # pattern = re.search(r"prefix+[\w.-]+suffix", str)
    # if pattern is str:
    if re.search(pattern , str) :
        
        print("matched")
        return True
    

    return False 

       
str = input("enter a strng to check whether it start with given pattern or not ")
print(pattern_strt_end(str))