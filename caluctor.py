print("Mini Calculator")

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the second number here: "))

print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division")
choice = int(input("Enter a choice from 1 - 4: "))

if choice == 1:
    print("The addition of the given two numbers is", num1 + num2)
elif choice == 2:
    print("The subtraction of the given two numbers is", num1 - num2)
elif choice == 3:
    print("The multiplication of the given two numbers is", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("The division of the given two numbers is", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid input")


