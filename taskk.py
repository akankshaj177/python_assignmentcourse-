try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nResults:")
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers only.")
