class Solution():
    def __init__(self):
        self.memo = {}
    
    def rod(self, n, prices[]):
        if n <= 0:
            return -1

        # Base Case
        if n == 1:
            return prices[0]
        
        # See if we've already calculated this
        if n in self.memo:
            return self.memo[n]

        
        
        
