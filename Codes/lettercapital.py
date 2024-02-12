#6: Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 

def LetterCapitalize(str):
    return str.title()
n=input("Enter your string: ")
print(LetterCapitalize(n))
