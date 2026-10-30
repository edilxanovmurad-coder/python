numbers = [4, 2, 7, 2, 4, 9, 2, 7, 5]
my_array = []
for i in numbers:
    if numbers.count(i) > 1 and my_array.count(i) == 0 :
        my_array.append(i)

print(my_array)