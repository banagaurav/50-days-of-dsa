# mountain array properties 
# values will be in increasing order before peak
# values will be in decresing order after peak
# peak will greater then previous and following value


arr = [0,3,8,9,5,2]

# starting and ending value can never be peak
start = 1 
end = len(arr) - 2

while(start<=end):
    mid = start + (end-start) // 2
    if arr[mid-1] < arr[mid] > arr[mid+1]:
        print(f"peek is {arr[mid]}")

    if arr[mid] < arr[mid+1]:
        start = mid + 1
    else:
        end = mid - 1 