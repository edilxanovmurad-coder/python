numbers = [3, 3, 12, 12, 8, 8, 5, 3,4,25,23,22,5,1,5,6,15,25,45]

greatest = float("-inf")
secondGreatest = float("-inf")

for i in numbers:
    if i > greatest:
        greatest =i
    elif i < greatest and i > secondGreatest and numbers.count(i) == 1 :
        secondGreatest = i

print(secondGreatest)
