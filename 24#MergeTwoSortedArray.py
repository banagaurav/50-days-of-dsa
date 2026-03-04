A = [1,2,3,0,0,0]
m = 3
B = [3,4,5] 
n = 3

i = m - 1
j = n - 1
indx = m + n - 1

while i >= 0 and j >= 0:
    if A[i] >= B[j]:
        A[indx], A[i] = A[i], A[indx]
        indx -= 1
        i -= 1
    else:
        A[indx], B[j] = B[j], A[indx]
        indx -= 1
        j -= 1

while j>=0:
    A[indx] = B[j]
    indx -= 1
    j -= 1

print(A)