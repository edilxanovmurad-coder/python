while True:
    try:
        number = int(input("please  type a number : "))
        break
    except ValueError:
        print("please type a number")

x= 1
for i in range(number, 1, -1):
    x *= i

print(x)