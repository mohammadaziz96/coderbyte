#5: Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases, the parameter num will be any number from 1 to 1000. 

def SimpleAdding(num):
    count=0
    for i in range(1, num+1):
        count=count+i
    return count
n=int(input("Enter any number: "))
print(SimpleAdding(n))
