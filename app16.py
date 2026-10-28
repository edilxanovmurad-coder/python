while True:
    try:
        number = int(input("please type a number : "))
        break
    except ValueError:
        print("please type a intager number")

numberStr =str(number)
print(len(numberStr))
