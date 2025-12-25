def longest_word_string(str):
    word = str.split(" ")
    return max(word, key=len)
str = input("enter a string to check longest word in a sentence / string ")
print(longest_word_string(str))