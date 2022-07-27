def subarray_sum(nums):
    sumSet = set()
    sum = 0
    
    for i in range(len(nums)):
        sum += nums[i]
        sumSet.add(sum)

    if(len(sumSet) < len(nums) or 0 in sumSet):
        return True

    return False

#Test Case 1
nums = [-1, -2, 3, 4, 5]
print(subarray_sum(nums))

#Test Case 2
nums = [3, -7, 4, 3, -1]
print(subarray_sum(nums))

#Test Case 3
nums = [1, 2, 3, 4, 5]
print(subarray_sum(nums))

#Test Case 4
nums = [1, 2, 3, 0, 5]
print(subarray_sum(nums))