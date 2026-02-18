n = 4
for i in range(1,n+1):
    a = 1
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(a, end=" ")
        a+=1
    for j in range(i-1):
        print(i-1, end=  " ")
        i = i-1
    print()