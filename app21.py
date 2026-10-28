user_input = input("please type a word: ")

chars = list(user_input)
result = ""
for i in range(len(chars)-1 , -1,-1):
    result += chars[i]
print(result)