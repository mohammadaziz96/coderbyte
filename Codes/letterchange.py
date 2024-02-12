#4:  Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str):
    translation_table=str.maketrans("abcdefghijklmnopqrstuvwxyz", "bcdEfghIjklmnOpqrstUvwxyzA")
    transformed_str=str.translate(translation_table)
    return transformed_str
n=input("Enter your string: ")
print(LetterChanges(n))
