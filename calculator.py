import math

def calculator():
    print("Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Sine")
    print("7.Cosine")
    print("8.Tangent")
    choice = input("Enter your choice from 1-8 : ")

    if choice in ['1','2','3','4','5']:
        num1 = float(input("Enter first number = "))
        num2 = float(input("Enter second number = "))

        if choice == '1':
            print(num1,"+",num2,"=",num1+num2)
        elif choice == '2':
            print(num1,"-",num2,"=",num1-num2)
        elif choice == '3':
            print(num1,"*",num2,"=",num1*num2)
        elif choice == '4':
            if num2 != 0:
                print(num1,"/",num2,"=",num1/num2)
            else:
                print("Error! Division by zero is not allowed.")
        elif choice == '5':
            print(num1,"^",num2,"=",num1**num2)

    elif choice in ['6','7','8']:
        num = float(input("Enter a number = "))
        if choice == '6':
            print("Sine of",num,"=",math.sin(math.radians(num)))
        elif choice == '7':
            print("Cosine of",num,"=",math.cos(math.radians(num)))
        elif choice == '8':
            print("Tangent of",num,"=",math.tan(math.radians(num)))
    else:
        print("Invalid choice!")
calculator()
