class Solution:
    def canFinish(self, numCourses: int, prerequisites):

        adj = {}
        indegrees = [0]*numCourses
        
        for e in prerequisites:
            i = e[0]
            o = e[1]
            indegrees[i]+=1 # find how many prereqs are required for the specific node
            
            if o not in adj: #prereq does not exist in dict yet
                adj[o] = []
            
            adj[o].append(i) #prereq does exist in dect
        
        q = [] # queue
        
        for i in range(numCourses):
            if indegrees[i]==0: #if no prereqs required, start graph search there
                q.append(i)
        
        while q:
            curr = q.pop(0) # look at "root"
            n = adj.get(curr) # get the next node
            if not n: # if there are no neighbours to root, continue
                continue
            for edge in n: # if there are neighbours
                indegrees[edge]-=1 # remove the edge
                
                if (indegrees[edge] ==0): # has it become a root?
                    q.append(edge)
                    
        for i in range(numCourses):
            if indegrees[i]!=0: # check if there are still nodes that require prereqs
                return False # means impossible
        return True # else, possible

# Test Case 1
nc = 3
prereqs = [[0, 1], [1, 2], [2, 0]]

sol = Solution()
print(sol.canFinish(nc, prereqs))

# Test Case 2
nc = 3
prereqs = [[0, 1], [2, 1]]

sol = Solution()
print(sol.canFinish(nc, prereqs))