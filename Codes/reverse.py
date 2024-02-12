#1 Using the Python language, have the function FirstReverse() and ReverseInt() takes the str and integer parameter respectively being passed and return the string and integer in reversed order.

def FirstReverse(r):
    return(r[::-1])

def ReverseInt(num):
    r=0
    while num!=0:
        digit=num%10
        r=r*10+digit
        num=num//10
    return r


s=input("Enter string: ")
n=int(input("Enter numbers: "))
print(FirstReverse(s))
print(ReverseInt(n))

