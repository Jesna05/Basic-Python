# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# x = int(input("Enter a number: "))
# y = fib(x) % 100
# print(y)


# x = int(input("Enter a number: "))
# a = x**2
# l = len(str(x))
# if a%(10**l)==x:
#     print("Automorphic")
# else:
#     print("Not automorphic")


# x = int(input("Enter a number: "))
# n = x
# sum = 0
# while x != 0:
#     sum=sum+((x%10)**3)
#     x = x//10
# if sum == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
#
# l = [2,4,12,7,5,1]
# for i in l:

l=["dood", "cac", "took", "malayalam", "Zooooooyza", "LOOOOOOOOOOOL"]
max=0
for i in l:
    if i.lower()[::-1]==i.lower():
        l = len(i)
        if l > max:
            max=l
print(max)




