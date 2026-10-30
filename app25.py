word = "programming"
printed =[]
for i in word:
    if word.count(i) == 1:
        print(f"{i} : {word.count(i)}")
    elif word.count(i) > 1 and printed.count(i)  == 0:
        printed.append(i)
        print(f"{i} : {word.count(i)}")
