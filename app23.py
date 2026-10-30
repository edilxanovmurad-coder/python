a = [1, 4, 6, 8, 10, 4]
b = [2, 4, 8, 9, 10, 4]

my_array = []

for i in a:
    for i2 in b:
        if i == i2 and my_array.count(i) == 0:
            my_array.append(i2)

print(my_array)
