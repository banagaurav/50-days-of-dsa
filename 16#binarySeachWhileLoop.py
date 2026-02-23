a = [1,2,5,7,9,12,22,24]

target = 22
start = 0 
end = len(a) - 1 
found = False

while start <= end :
    # mid = (start + end)//2 
    # above calculation of mid in worst case can be start = max int value and also for end 
    # we cause overflow and can miscalculate the mid. So, 

    mid = start + ((end-start)//2)
    
    if target > a[mid]:
        start = mid + 1
    elif target < a[mid]:
        end = mid - 1
    else:  # target == a[mid]
        print(f"Target:{target} found at index: {mid}")
        found = True
        break

if not found:
    print("Target not found")

