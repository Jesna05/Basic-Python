# for i in range(5):
#     for j in range(5):
#         print(i,end=" ")
#     print()

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i,6):
#         print(i,end=" ")
#     print()

# for i in range(1,6):                           5 5 5 5 5
#     for j in range(i,6):                       5 5 5 5
#         print("5",end=" ")                     5 5 5
#     print()                                    5 5
#                                                5

for i in range(0,5):                            #1
    for j in range(0,i+1):                      #3 3
        n=i                                     #5 5 5
        print((2*n+1),end=" ")                  #7 7 7 7
    print()                                     #9 9 9 9 9


