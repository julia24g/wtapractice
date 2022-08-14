def cutrod(price, n):
    best = [0]*(n+1)
    for i in range(1, n + 1): # starts at 1 because we want to have access to 0 in val array to know what the sum of price by itself would be
        m = float('-inf')
        for j in range(i): # only goes up to current value of n we are testing
            m = max(m, price[j] + best[i-j-1]) # compares max value to that of value from price plus its opposite value in val
        best[i] = m

    return best[n]

# Test Case 1
price = [1, 3, 3, 9, 10, 17, 18, 18]
n = len(price)
print(cutrod(price, n))
# Answer: 3 + 17 = 20 - cut rod into peice of length 2 and length 6

# Test Case 2
price = [1, 2, 3, 5]
n = len(price)
print(cutrod(price, n))
# Answer: 5 - sell whole rod

# Test Case 3
price = []
n = len(price)
print(cutrod(price, n))



 

        
        
        
