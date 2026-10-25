my_array = [12, 5, 28, 3, 17, 9]
largest = my_array[0]
Smallest = my_array[0]

for i in my_array:
    if i > largest:
        largest = i
    elif i < Smallest:
        Smallest = i

print(Smallest + largest, len(my_array))