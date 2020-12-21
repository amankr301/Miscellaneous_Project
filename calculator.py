def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

num1 = float(input("Enter the first number: "))
operator = input("Choose the number + : Add, - : Subtraction, * : Multiplication, / : Division : ")
num2 = float(input("Enter the second number: "))



if operator == "+":
    #print("\n The First number is : ", num1,
    #      "\n The Second number is : ", num2,
    #      "\n The Sum of two numbers is : ", add(num1, num2))
    print(num1, "+", num2 , "=" , add(num1, num2))

elif operator == "-":
    #print("\nThe First number is : ", num1,
    #      "\nThe Second number is : ", num2,
    #      "\nThe Subs of two number is : ", sub(num1, num2))
    print(num1, "-", num2, "=", sub(num1, num2))

elif operator == "*":
    #print("\nThe First number is : ", num1,
    #      "\nThe Second number is : ", num2,
    #      "\nThe Multiplication of two number is : ",multiply(num1, num2))
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operator == "/":
    #print("\nThe First number is : ", num1,
    #      "\nThe Second number is : ", num2,
    #      "\nThe Division of the two number is : ", divide(num1, num2))
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("The number is invalid")