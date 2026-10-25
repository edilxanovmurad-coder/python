a = 20
b = 6


def my_function(x, y):
    for i in range(6):
        match i:
            case 1:
                print(x + y)
            case 2:
                print(x - y)
            case 3:
                print(x * y)
            case 4:
                print(x / y)
            case 5:
                print(x % y)



my_function(a, b)
