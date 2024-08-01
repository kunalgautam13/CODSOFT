#CODSOFT PYTHON PROGRAMMING INTERNSHIP
                #TASK-2
def calculator():
    print("Simple Calculator")
    
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for the chosen operation
    operation = input("Enter the operation (1/2/3/4): ")
    
    # Perform the calculation based on the chosen operation
    if operation == "1":
        result = num1 + num2
        op_symbol = "+"
    elif operation == "2":
        result = num1 - num2
        op_symbol = "-"
    elif operation == "3":
        result = num1 * num2
        op_symbol = "*"
    elif operation == "4":
        if num2 != 0:
            result = num1 / num2
            op_symbol = "/"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return
    
    # Display the result
    print(f"The result of {num1} {op_symbol} {num2} is: {result}")

# Call the calculator function to run the program
calculator()