x = int(input("number 1: "))
y = int(input("number 2: "))
z = int(input("number 3: "))

largest = float("-inf")

my_array = [x,y,z]
for i in my_array:
    if i > largest:
        largest = i

print(largest)