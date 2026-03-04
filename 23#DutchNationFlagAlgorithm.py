# Dutch National Flag Algorithm (DNF)
# this algorithm is applied on problems like sort arrays with 0s, 1s and 2s 
# this algorithm states:
# the array should be participated into four part low , mid , unsorted and high part 
# where , 0s => 0 to low - 1 , 1s => low to mid - 1 , 2s => high to n - 1 and unsorted array will be at mid to high - 1

a = [2,0,2,1,1,0,1,2,0,0]

n = len(a)
# first the whole array is unsorted so we can say mid is at ith position and high is in the last i.e n - 1 position and also low is at 0th position 
mid = 0
high = n - 1
low = 0  

while mid <= high :
    if a[mid] == 0:
        a[mid],a[low] = a[low] , a[mid]
        mid += 1
        low += 1
    
    elif a[mid] == 1:
        mid += 1
    
    else:
        a[mid],a[high] = a[high] , a[mid]
        high -= 1

print(a)
