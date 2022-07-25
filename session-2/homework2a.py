def subarray_sum(nums):
    sumSet = set()
    sum = 0
    
    for i in range(len(nums)):
        sum += nums[i]
        sumSet.add(sum)

    if(len(sumSet) < len(nums) or 0 in sumSet):
        return True

    return False

nums = [-1, -2, 3, 4, 5]
print(subarray_sum(nums))