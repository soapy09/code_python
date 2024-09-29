print("Welcome to our calculator app1")

num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: "))

choice = input("Choose either: add, subtract, multiply or divide: ")

if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "multiply":
    print (num1 * num2)
elif choice == "divide":
    print (num1 / num2)