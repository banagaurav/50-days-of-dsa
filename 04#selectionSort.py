myArr = [45,96,7,5,12,65,85]

n = len(myArr)

for i in range(n-1):
    minIndex = i
    for j in range(i+1,n):
        if myArr[j] < myArr[minIndex]:
            minIndex = j
    myArr[i],myArr[minIndex] = myArr[minIndex],myArr[i]
    print(myArr)
