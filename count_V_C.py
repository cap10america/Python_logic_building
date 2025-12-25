def count_vowels_consonants(str):
    vowels = set("aeiouAEIOU")
    v=c=0
    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                v +=1
            else :
                c +=1
    print(v,c)
str = input("enter a string to count the references of vowels and consonants")
count_vowels_consonants(str)
