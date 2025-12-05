# x = int(input("Enter a year:"))
# if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

x = int(input())
if x % 4 ==0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")