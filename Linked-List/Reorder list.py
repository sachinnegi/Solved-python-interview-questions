'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid(self,head):
        slow,fast = head,head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self,head):
        prev = None
        while head:
            currNext = head.next
            head.next = prev
            prev = head
            head = currNext
        return prev
    def merge(self,headA,headB):
        
        dummy = ListNode(-1)
        curr = dummy
        while headA and headB:
            nextA = headA.next
            nextB = headB.next
            curr.next = headA
            curr = curr.next
            curr.next = headB
            curr =  curr.next
            headA = nextA
            headB = nextB
        if headA:
            curr.next = headA
        return dummy.next
        
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
            
        mid = self.mid(head)
        headB = mid.next
        mid.next = None
        headB = self.reverse(headB)
        head = self.merge(head,headB)
        
        
        
        
