myArr = [45,96,7,5,12,1]

n = len(myArr)

for i in range(n-1):
    swapped = False
    for r in range(n-i-1):
        if myArr[r] > myArr[r+1]:
            myArr[r+1],myArr[r]=myArr[r],myArr[r+1]
            swapped = True
        print(myArr)
    if not swapped:
        break    