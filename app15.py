# my_array_even = []
# my_array_odd  = []
# x = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         my_array_even.append(i)
#     else:
#         my_array_odd.append(i)

# for i in my_array_even:
#     x+=i

# print(x)


x= 0
for i in range(0,101,2):
    x+= i

print(x)