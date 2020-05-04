# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)  # go to the end recursively till head.next and contains new Head
        head.next.next = head               # reversing link from end node to  back node
        head.next = None                    # breaking link from front to back node
        return node                         # returning the last node every time as new head
        
        
