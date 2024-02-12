#2 Using the Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18. 

def FirstFactorial(num):
    if num==1:
        return 0
    elif num==0:
        return 1
    elif num<0:
        return "You have typed negative number! Please type only positive numbers"
    else:
        x=1
        while num!=1:
            x=x*num
            num=num-1
        return x
n=int(input("Enter number to get factorial: "))
print(FirstFactorial(n))
