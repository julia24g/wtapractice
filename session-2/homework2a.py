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

#option 2

# def subarray_zero_sum(nums):

#     for x in range(1, len(nums)):
#         if ((nums[x] > 0 and nums[x-1] < 0) or (nums[x] < 0 and nums[x-1] > 0)):
#             nums[x] += nums[x-1]
#         if nums[x] == 0:
#             return True
#     return False
            
# nums = [-3, -3, 6, 1, 6]
# print(subarray_zero_sum(nums))