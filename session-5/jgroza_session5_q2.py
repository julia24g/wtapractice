class Solution():
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum = 0
        count = 0
        maxcount = 0
        
        for i in nums:
            sum += i
            if sum > 0:
                count += 1
            else:
                maxcount = max(maxcount, count)
        
        if maxcount == 0:
            largest = -infinity
            for i in nums:
                if i > -infinity:
                    largest = i
            return largest
        else:
            return maxcount