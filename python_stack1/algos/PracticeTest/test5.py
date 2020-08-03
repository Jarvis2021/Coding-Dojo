#Assignment: Find Characters

# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.




char = 'o'
word_list = ['hello','world','my','name','is','Anna']

def findwords(x):
    matching = [s for s in x if "o" in s]
    return matching

    # for i in x:
    #     if 'o' in i:
    #         print (i)





print(findwords(word_list))
