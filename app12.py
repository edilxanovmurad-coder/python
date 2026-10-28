while True:
    try:
        number1 = int(input("number 1 : "))
        number2 = int(input("number 2 : "))
        break
    except ValueError:
        print("please type number")
    

if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
else:
    print("the numbers are equal")