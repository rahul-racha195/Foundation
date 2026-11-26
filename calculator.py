print("=======CALCULATOR====")
number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice:")
if choice == "1":
    result = number1 + number2
    print("Addition of the two numbers is:", result)
elif choice == "2":
    result = number1 - number2
    print("Subtraction of the two numbers is:", result)
elif choice =="3" :
    result = number1 * number2 
    print("Multiplication of two numbers is:", result)
elif choice == "4":
    if number2 != 0:
        result = number1 / number2
        print("Division of two numbers is:", result)
    else:
        print("Error: Division by zero is not allowed.")    
else :
    print("Invalid choice. Please select a valid operation.")