#1: Using the Python language, have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.

def PrimeTime(num):
    if num<=1:
        return False
    elif num<=3:
        return True
    elif num%2==0 or num%3==0:
        return False

