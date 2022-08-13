class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeMultipleSortedLists(self, lists):
        
        k = len(lists)
        if lists is None or k ==0: return None
        
        interval = 1
        while interval < k:
            for x in range(0, k - interval, interval*2):
                lists[x] = self.mergeSortedLists(lists[x], lists[x+interval])
            interval = interval * 2  
        
        return lists[0]
        
    def mergeSortedLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = list1
        l2 = list2
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l2.val < l1.val:
            l2.next = self.mergeSortedLists(l2.next, l1)
            return l2
        else:
            l1.next = self.mergeSortedLists(l1.next, l2)
            return l1

# Test Case 1

## insert into l1
curr = l1 = ListNode(3)
l = [9, 11, 15]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

## insert into l2
curr = l2 = ListNode(1)
l = [2,3]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

## insert into l3
curr = l3 = ListNode(4)
l = [5, 7, 8, 9]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

lists = [l1, l2, l3]

obj = Solution()
l4 = obj.mergeMultipleSortedLists(lists)

## print l4 results
print("Test Case 1:")
res = []
curr = l4
while curr != None:
    res.append(curr.val)
    curr = curr.next
print(res)

#Test Case 2
## insert into l1
curr = l1 = ListNode(1)
l = [2]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

## insert into l2
curr = l2 = ListNode(6)

## insert into l3
curr = l3 = ListNode(1)
l = [1]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

## insert into l4
curr = l4 = ListNode(4)
l = [25]
for x in l:
    curr.next = ListNode(x)
    curr = curr.next

lists = [l1, l2, l3, l4]

obj = Solution()
l5 = obj.mergeMultipleSortedLists(lists)

## print l5 results
print("Test Case 2:")
res = []
curr = l5
while curr != None:
    res.append(curr.val)
    curr = curr.next
print(res)