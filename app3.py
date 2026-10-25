x = int(input("number 1 : "))
y = int(input("number 2 : "))
z = int(input("number 3 : "))

my_array = [x, y, z]
largest = None

for i in my_array:
    if largest == None or i > largest :
        largest = i

print(largest)
