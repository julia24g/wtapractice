class Solution:
    def lenSubArray(self, nums) -> int:
        s = 0
        maxsum = float('-inf')
        maxcount = 0
        count = 0
        
        for i in nums:
            s += i
            if s >= 0:
                count += 1
                if s > maxsum:
                    maxcount = count
                    maxsum = s
            else:
                count = 0
                s = 0
        
        if maxsum == float('-inf') and len(nums) > 0:
            return 1
        
        return maxcount

# Test Case 1
nums = [-2, -5, 1, 6, -2, 4, -10, 1]
test = Solution()
print(test.lenSubArray(nums))
# Answer: 4 - [1, 6, -2, 4] is the subarray

# Test Case 2
nums = [5,4,-13,7,8]
print(test.lenSubArray(nums))
# Answer: 2 - [7, 8] is the subarray

# Test Case 3
nums = [-1, -3, -5]
print(test.lenSubArray(nums))
# Answer: 1 - [-1] is the subarray