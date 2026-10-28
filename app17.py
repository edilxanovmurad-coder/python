while True:
    try:
        number = int(input("please  type a number"))
        break
    except ValueError:
        print("please type a number")


numberStr =str(number)
number_array  = list(numberStr)
x= 0
for i in number_array:
    x += int(i)
print(x)