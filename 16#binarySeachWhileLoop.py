a = [1,2,5,7,9,12,22,24]

target = 22
start = 0 
end = len(a) - 1 
found = False

while start <= end :
    mid = (start + end)//2 
    if target > a[mid]:
        start = mid + 1
    elif target < a[mid]:
        end = mid - 1
    else:  # target == a[mid]
        print(f"Target found at index: {mid}")
        found = True
        break

if not found:
    print("Target not found")

