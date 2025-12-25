def non_repeating_char(str):
    from collections import Counter 
    freq= Counter(str)

    for c in str :
        if freq[c] ==1 :
            print(c)
            return None
str = input("enter a string to caluclate the first non repeating char from the string ")
non_repeating_char(str) 