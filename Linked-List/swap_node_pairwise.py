# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def split(self,head,k):
        count=1
        curr = head
        while (curr and curr.next and count<k):
            curr = curr.next
            count+=1
        nextHead = curr.next
        curr.next = None
        return head, nextHead
    
    def reverse(self,head):
        prevHead  = None
        tail = head
        while head:
            currNext = head.next
            head.next = prevHead
            prevHead = head
            head = currNext
        print(prevHead)
        return prevHead,tail
            
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        curr = dummyNode
        while head:
            head1,head = self.split(head,2)
            #print(head1,head)
            revHead ,tail= self.reverse(head1)
            curr.next = revHead
            curr = tail
        return dummyNode.next


#SECOND METHOD
def pairWiseSwap(head):
    if not head:
        return head
    dummyNode = Node(-1)
    dummyNode.next = head
    curr = dummyNode
    while curr.next and curr.next.next:
        first = curr.next
        sec = curr.next.next
        first.next = sec.next
        sec.next = first
        curr.next = sec
        curr = curr.next.next
    return dummyNode.next
