x = 30
s=0
for i in range(1,(x//2)+1):
    if x%i == 0:
        s += i
if s==x:
        print("perfect")
else:
    print("Not perfect")
