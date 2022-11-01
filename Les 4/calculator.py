def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation: \n1. Add\n2. subtract\n3. multiply\n4. divide")

while True:
    choice = input("Enter choice: ")
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        if choice == '1':
            outcome = add(num1, num2)
            print(num1, "+", num2, "=", outcome)
            if outcome == 69:
                print("haha nice")

        elif choice == '2':
            outcome = subtract(num1, num2)
            print(num1, "-", num2, "=", outcome)
            if outcome == 69:
                print("haha nice")

        elif choice == '3':
            outcome = multiply(num1, num2)
            print(num1, "x", num2, "=", outcome)
            if outcome == 69:
                print("haha nice")

        elif choice == '4':
            outcome = divide(num1, num2)
            print(num1, ":", num2, "=", outcome)
            if outcome == 69:
                print("haha nice")

        #Checks if user wants to do another calculation
        nextcalc = input("Do you want to do another calculation?: ")
        if nextcalc == "no":
            break
    
    else:
        print("invalid input")