def sub_str(str):
    # for i in range(len(str)):
    #     for j in  range (i+1 , len(str)+1):
    #         print(str[i:j])
    return [str[i:j] for i in range(len(str)) for j in range(i+1 ,len(str)+1)]

str = input("enter a string to check all the substrings from the list")
print(sub_str(str))