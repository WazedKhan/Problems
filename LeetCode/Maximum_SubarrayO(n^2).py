# Amazon Coding Interview Question - Leetcode 53

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = nums[0]



for i in range(len(nums)):
    val = nums[i]
    if nums[i] >= max_sum:
        max_sum = nums[i]
    for j in range(i+1 ,len(nums)):
        val += nums[j]
        if val >= max_sum:
            max_sum = val

print(max_sum)