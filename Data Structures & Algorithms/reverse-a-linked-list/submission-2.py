# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # [1,2,3]
        prev = None
        curr = head
        while curr != None:
            next = curr.next #save it to node 2 so you don't lose the loop 
            curr.next = prev #switch arrow so 1 points to null
            prev = curr #prev (0) becomes 1 which was curr
            curr = next #curr (1) becomes 2 which was next, and the sticky notes move to the right all the way
        return prev #at the end, it's prev on 3 and curr on nothing
        
        