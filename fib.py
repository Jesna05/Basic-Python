#Method 1
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
x = int(input("Enter a number: "))
for i in range(x):
        print(fib(i))


#Method 2
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    else:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
        return memo[n]
n = int(input("Enter the value of n:"))
print(f"The {n}th fibonacci number is: {fib(n)}")
