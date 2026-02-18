n = 4
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n-i):
        print(i+1, end = " ")
    print()