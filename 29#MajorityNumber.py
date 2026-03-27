# a majority always lies there

nums = [1,2,2,1,2]

def voting(nums):
    ans = nums[0]
    freq = 0
    ans = 0
        
    for i in range(len(nums)):
        
        if freq == 0:
            ans = nums[i]
        
        if ans == nums[i]:
            freq += 1           
        else:
            freq -= 1
            
    return ans
     
print(voting(nums))