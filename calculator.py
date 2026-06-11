while True:
    print("\n----- CALCULATOR -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Percentage")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Calculator closed. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero.")

    elif choice == "5":
        if num2 != 0:
            print("Result =", num1 % num2)
        else:
            print("Cannot perform modulus with zero.")

    elif choice == "6":
        print("Result =", (num1 / 100) * num2)

    else:
        print("Invalid choice. Please try again.")