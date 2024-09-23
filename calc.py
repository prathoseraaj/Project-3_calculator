print("Welcome to the Python Calculator!")
print("Choose an operation:")
print("1. Multiplication")
print("2. Division")

choice = input("Enter choice (1/2): ")

if choice not in ['1', '2']:
    print("Invalid input. Please select 1 or 2.")
else:
    # Get numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 * num2
        print(f"The result of multiplication: {num1} * {num2} = {result}")
    elif choice == '2':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division: {num1} / {num2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")
