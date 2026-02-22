# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

nums = [1,2,3,4]
n = len(nums)
# prefix = [1] * n
# suffix = [1] * n
suffix = 1
ans = [1] * n
for i in range(1,n):
    ans[i] = ans[i-1] * nums[i-1]
    # prefix[i] = prefix[i-1] * nums[i-1]

for i in range(n-2,-1,-1): #or for i in reversed(range(n))
    suffix *= nums[i+1]
    ans[i] = ans[i] * suffix
    # suffix[i] = suffix[i+1] * nums[i+1]

# for i in range(n):
#     ans[i] = prefix[i] * suffix[i]

print(ans)