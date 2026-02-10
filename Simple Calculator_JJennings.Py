import math

print("Enter name:")
name = input()
print("Hello, " + name + "!")

print("Enter Operator (+ | - | * | / | ^ | sqrt):")
operator = input()
if operator == "sqrt":
    print("Enter number:")
    num1 = float(input())

    if num1 < 0:
        print("Error:Cannot take square root of a negative number.")
    else:
        result = math.sqrt(num1)
        print("The square root of " + str(num1) + " is " + str(result))
        

    
    
    










