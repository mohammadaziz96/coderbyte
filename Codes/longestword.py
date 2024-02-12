#3 Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

import string
def Longestword(sen):
    translator=str.maketrans("", "", string.punctuation)
    sen=sen.translate(translator)
    t=0
    for i in sen.split(" "):
        if len(i)>t:
            t=len(i)
    return t
n=input("Enter your String: ")
print(Longestword(n))
