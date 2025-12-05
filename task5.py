x = input()    #input().lower()
for i in x:
    if i.lower() not in "aeiou":
        print(i, end="")
print("hello"*5)
print("""Ravi is a good boy
He sings well""")
x = 5
y = "apple"
print(f"""Ravi is a good boy {x}
He sings well {y} """)