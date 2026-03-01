arr = []
n = len(arr)
m = 2

def isValid(arr, n , m , maxAllowedPages):
    students = 1 , pages = 0

    for i in range(n):
        if arr[i] > maxAllowedPages:
            return False
        
        if pages + arr[i] <= maxAllowedPages:
            pages += arr[i]
        else:
            students + 1 
            pages = arr[i]

    return False if students > m else True

def allocateBooks(arr,n,m):
    if m > n:
        return -1
    
    sum = 0

    for i  in range(n):
        sum += arr[i]

    ans = -1 
    st = 0
    end = sum

    while(st <= end):
        mid = st + (end - st)/2

        if isValid(arr,n,m,mid):
            ans = mid
            end = mid - 1
        else:
            st = mid + 1

    return ans