import math_utils as m

print(m.divide(4,2))
def add( a ,  b):
    return a+b

def sub( a ,  b):
    return a-b
symobols = ["+","-"]
user = input("Enter add or sub + or - : ")

if user in symobols:
    num1 = int(input("Num1: \n"))
    num2 = int(input("Num2: \n"))
    if user == "+":
        print(add(num1,num2))
    if user == "-":
        print(sub(num1,num2))

else:
    print("Please enter a valid symbol")
