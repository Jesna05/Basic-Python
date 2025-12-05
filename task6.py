# x = "elephant"
# print(x[0:3])
# print(x[3:6])
# print(x[3:])
# print(x[7:4:-1])
# print(x[::-1])
# print(x[::-2])
# y = 326
# r = 0
# while y != 0:
#     l = y%10
#     r = r*10 + l
#     y = y//10    #floor/integer division
# print(r)
y = 1001
x = y
r = 0
while y != 0:
    l = y%10
    r = r*10 + l
    y = y//10  #floor/integer division

if x == r:
    print("Palindrome")
else:
    print("Not palindrome")