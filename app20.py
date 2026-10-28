numbers = [4, 9, 2, 9, 7, 5]
greatest = float("-inf")
secondGreatest = float("-inf")

for i in numbers:
    if i > greatest:
        secondGreatest = greatest
        greatest = i
    elif i < greatest and i > secondGreatest :
        secondGreatest = i

print(secondGreatest)