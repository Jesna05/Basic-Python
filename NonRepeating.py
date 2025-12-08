lst = [4,5,5,3,5,6,7,4,3,6]
for i in set(lst): #repetition is stopped
    if lst.count(i) == 1:
        print(i)
