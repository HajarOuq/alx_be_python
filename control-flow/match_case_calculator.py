num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Choose the operation (+, -, *, /):")
result = 0
match op :
    case "+":
        print("The result is",num1 + num2) 
    case "-":
        print("The result is",num1 - num2) 
    case "*":
        print("The result is",num1 * num2) 
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else :
            print("The result is",num1 / num2)