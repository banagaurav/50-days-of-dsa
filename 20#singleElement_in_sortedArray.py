# Single Element in Sorted Array

arr = [1,1,2,3,3,4,4,8,8]
# arr = [1]

start = 0
end = len(arr) - 1

if(len(arr) == 1):
    print(f"Single element is {arr[0]}")

while(start<=end and len(arr) != 1):
    mid = start + (end - start) // 2

    if ( mid == 0 and arr[0] != arr[1]):
        print(f"Single element is {arr[mid]}")
        break

    if ( mid == len(arr)-1  and arr[len(arr)-1] != arr[len(arr)-2]):
        print(f"Single element is {arr[mid]}")
        break

    if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
        print(f"Single element is {arr[mid]}")
        break

    # when an array has values of a number repeating twice(perfect duplicate) we can say that it will be of even size
    # perfect duplicates = even
    # duplicate + single = odd 

    if mid % 2 == 0: 
        if arr[mid] == arr[mid-1]:
            end = mid - 1
        else:
            start = mid + 1
    else: 
        if arr[mid] == arr[mid-1]:
            start = mid + 1
        else:
            end = mid - 1 
