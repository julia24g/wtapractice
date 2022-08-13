class Solution:
    def removeP(self, s):      
        
        r1 = []
        bal = 0
        for x in s:
            if x == '(':
                bal += 1
            elif x == ')':
                bal -= 1
            if bal < 0:
                bal += 1
                continue
            r1.append(x) # add valid chars to list
        s1 = "".join(r1) # creating into a string
        
        r2 = []
        bal = 0
        s2 = s1[::-1] # finding the reverse
        for x in s2:
            if x == ')':
                bal += 1
            elif x == '(':
                bal -= 1
            if bal < 0:
                bal += 1
                continue
            r2.append(x) # add valid chars to list
        s2 = "".join(r2)
        return s2[::-1]

#Test Case 1
s = "((hey)(u)))"
obj = Solution()
print(obj.removeP(s))

#Test Case 2
s = "(((oops"
obj = Solution()
print(obj.removeP(s))