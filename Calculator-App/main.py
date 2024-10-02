def calculator():
    print("CALCULATOR----------------->>")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nSelect an operation:")
        print("1 for Addition (+)")
        print("2 for Subtraction (-)")
        print("3 for Multiplication (*)")
        print("4 for Division (/)")
        
        choice = int(input("\nEnter your choice (1/2/3/4): "))

        match choice:
            case 1:
                result = num1 + num2
                print(f"The result of {num1} + {num2} = {result}")
            case 2:
                result = num1 - num2
                print(f"The result of {num1} - {num2} = {result}")
            case 3:
                result = num1 * num2
                print(f"The result of {num1} * {num2} = {result}")
            case 4:
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("Invalid operation choice. Please select 1, 2, 3, or 4.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Call the calculator function
calculator()
