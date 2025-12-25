from collections import Counter

def freq_count(str):
    print(Counter(str))


str = input("enter a string to check the frequency of a each character in a string ")
freq_count(str)