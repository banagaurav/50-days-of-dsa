n= 4

for i in range(1,n+1):
    for j in range(n-i):
        print("_",end= " ")
    print("*",end=" ")
    if(i != 1 ):
        for j in range((i-1)+(i-2)):
            print("_",end =" ")
        print("*")
    print()
    
for i in range(n-1, 0, -1):
    # Print leading underscores
    for j in range(n - i):
        print("_", end=" ")
    
    # Print first star
    print("*", end=" ")
    
    # Print middle underscores (if any)
    if i > 1:
        for j in range(2 * i - 3):
            print("_", end=" ")
        # Print second star
        print("*", end="")
    
    # New line
    print()


# pyramid made kite happened

# n = 4
# for i in range(1,n+1):
#     a = 1
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(a, end=" ")
#         a+=1
#     for j in range(i-1):
#         print(i-1, end=  " ")
#         i = i-1
#     print()