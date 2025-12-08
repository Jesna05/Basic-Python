# x =  [5,1,4,1,5]
# for i in set(x):
#     if x.count(i)>1:
#         print(i)

x = [1,2,3,2,4,3]
seen = set()
dup = set()
for x in x:
    if x in seen:
        dup.add(x)
    else:
        seen.add(x)
print(list(dup))
