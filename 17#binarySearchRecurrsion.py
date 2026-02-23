def binarySearch(arr, target, start, end):
    if start <= end:
        mid = start + (end - start) // 2
        
        if target > arr[mid]:  
            return binarySearch(arr, target, mid + 1, end)
        elif target < arr[mid]:  
            return binarySearch(arr, target, start, mid - 1)
        else:  # target == arr[mid]
            print(f"Target: {target} is at index: {mid}")
            return mid
    else:
        print(f"Target: {target} not found in the array")
        return -1

# Test
a = [1, 2, 5, 7, 9, 12, 22, 24]
target = 22
result = binarySearch(a, target, 0, len(a) - 1)