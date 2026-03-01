def isPossible(maxAllowedTime):
    painters = 1
    time = 0

    for i in range(N):
        if time + arr[i]<= maxAllowedTime:
            time += arr[i]
        else:
            painters += 1
            time = arr[i]

    return painters <= M

arr = [40,30,10,20]
N = len(arr)
M = 2

st = max(arr)
end = sum(arr)

ans = -1

while st <= end:
    mid = st + (end - st)//2

    if(isPossible(mid)):
        ans = mid
        end = mid - 1
    else:
        st = mid + 1

print(f"Minimum time to paint all boards: {ans}")

