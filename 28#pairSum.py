def bruteForce(nums,target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if (nums[i]+nums[j] == target):
                return [i,j]

def optimizedOption(nums, target):
    i = 0 
    j = len(nums) - 1
    
    while(i<j):
        ans = nums[i] + nums[j]

        if ans < target:
            i += 1
        elif ans > target:
            j -= 1
        else:
            return [i,j] 
     
# sorted array is given
nums = [2,4,11,15]

target = 13

print(optimizedOption(nums,target))

