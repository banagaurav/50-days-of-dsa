# in rotated sorted array has distintive values
arr = [3, 4, 5, 6, 7, 0, 1, 2]
start = 0
end = len(arr) - 1
tar = 1
found = False

while start <= end:
    mid = start + (end - start) // 2
    
    if arr[mid] == tar:
        print(f"Found {tar} at index: {mid}")
        found = True
        break
    
    if arr[start] <= arr[mid]:  # Left half is sorted
        if arr[start] <= tar <= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else:  # Right half is sorted
        if arr[mid] <= tar <= arr[end]:
            start = mid + 1
        else:
            end = mid - 1

if not found:
    print(f"{tar} not found in the array")

# this is not directly a binary but a modified one
