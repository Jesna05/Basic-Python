x = input("Enter a string:")       #PUT AN ADDITIONAL VARIABLE K then do k += i.upper()
for i in x:
    if i.islower():
        print(i.upper(),end="")
    else:
       print(i.lower(),end="")
