n = 4
for i in range(1, n+1):
    for j in range(n-i):
        print(" ",end=" ")
    print("*",end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    if(i>=2):
        for j in range(i-2):
            print(" ",end= " ")
        for j in range(1):
            print("*",end=" ")
    print()
for j in range(1,n):
    for i in range(j):
        print(" ",end=" ")
    for i in range(1):
        print("*",end=" ")
    for i in range(n-j-1):
        print(" ",end=" ")
    for i in range(n-j-2):
        print(" ",end=" ")
    if(j<n-1):
        print("*")
    print()
    
