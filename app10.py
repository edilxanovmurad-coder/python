while True:
    try:
        number1 = int(input("number 1:"))
        number2 = int(input("number 2:"))
        break
    except ValueError:
        print("please enter a number")


operatorInvalid = True
while operatorInvalid:
    operator = input("operator :")
    if operator == "x" or operator == "+" or operator == "-" or operator == "/":
        operatorInvalid = False
    else:
        print("please enter a operator")
        operatorInvalid = True

match operator:
    case "x":
        print(number1 * number2)
    case "/":
            print(number1 / number2)
    case "+":
            print(number1 + number2)
    case "-":
            print(number1 - number2)