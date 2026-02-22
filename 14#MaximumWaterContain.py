## heigth list contains the heigth of the barrier
## for MaxWaterContain we will have to calculate the widht i.e distance between the index and height of the smallest barrier
height = [1,2,8,6,4,7,3,9,1,2]
n = len(height)
pl = 0
pr = n-1
maxWater = 0

while pl < pr:
    w = pr - pl # width
    h = min(height[pl],height[pr]) # height of the smaller barrier 

    area = w * h

    maxWater = max(maxWater , area)

    if height[pl] < height[pr]:
        pl += 1
    else:
        pr -= 1

print(f"Max Water Contain: {maxWater}")