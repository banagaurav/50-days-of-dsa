myArr = [78,8845,23,6,21]

n = len(myArr)
for i in range(1,n):
    insert_index = i
    current_value = myArr.pop(i)
    for j in range(i-1, -1 ,-1):
        if(myArr[j]>current_value):
            insert_index = j
    myArr.insert(insert_index, current_value)
    print(myArr)