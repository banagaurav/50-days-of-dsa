a = [7,1,5,6,7]
length = len(a)

bestBuy = a[0]
maxProfit = 0

## we cannot buy and sell in same day

for i in range(length):
    if(a[i]>bestBuy):
        maxProfit = max(maxProfit, a[i]-bestBuy)
        print(f"{maxProfit} is the max-profit till day {i}")
    bestBuy = min(bestBuy,a[i])

print(maxProfit)