while True:
    try:
        number = int(input("please type a number : "))
        break
    except ValueError:
        print("please type a valid number")

my_array = []

for i1 in range(2, number):
    for i2 in range(2, i1):
        if i1 % i2 == 0:
            break
    else:
        my_array.append(i1)


print(my_array)
