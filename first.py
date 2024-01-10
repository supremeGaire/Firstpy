# print("Hello World!")

# num1 = 25
# num2 = 5
# sum = num1 + num2
# print("The sum is ",sum)

def take_input():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    return num1, num2

def add():
    num1, num2 = take_input()
    return (num2 + num1)

def sub():
    num1, num2 = take_input()
    return (num1 - num2)

def mul():
    num1, num2 = take_input()
    return (num1 * num2)

def div():
    num1, num2 = take_input()
    return (num1 / num2)

def menu():
    print("""
        Welcome to our Calculator:
        Please Choose one of the options below.
        1. Add Two numbers
        2. Subtract Two numbers
        3. Multiply Two numbers
        4. Divide Two numbers 
        5. Exit
""")

print("""
        Welcome to our Calculator:
        Please Choose one of the options below.
        1. Add Two numbers
        2. Subtract Two numbers
        3. Multiply Two numbers
        4. Divide Two numbers 
        5. Exit
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your result is : ", add())    

elif choice == 2:
    print("Your result is : ", sub())

elif choice == 3:
    print("Your result is : ", mul())

elif choice == 4:
    print("Your result is : ", div())

elif choice == 5:
    print("Bye bye")
    exit()

else:
    menu()




