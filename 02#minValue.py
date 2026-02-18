my_arr = [5,4,2,6,78,11]
minVal = my_arr[0]

for i in my_arr:
    if(i < minVal):
        minVal = my_arr[i]
    

print("lowest-value is: ", minVal)
    