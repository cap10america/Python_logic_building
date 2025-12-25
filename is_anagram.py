# def is_anagram(s1,s2):
#     count =0
    
#     if len(s1)==len(s2):
#         for i in s2:
#             if i in s1:
            
#                 count +=1
#         if count==len(s1):
#             print(f"the given strings {s1} ,{s2} are anagrams")
    
#     else:print("False")
# s1 ,s2 = map(str ,  input("enter the two strings to check the strings are anagrams or not S1:    , S2 :").lower().split())

# is_anagram(s1 , s2)


def are_anagrams( s1 , s2):
    return  sorted(s1)==sorted(s2)
s1 , s2 = map(str , input ("enter strings to check anagrams or not ").lower().split())
print(are_anagrams(s1,s2))
    