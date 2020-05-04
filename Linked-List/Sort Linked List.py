
#METHOD 1   -> using  merge sort (O(n)) extra space

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:        # single element or NULL
            return head
        midNode = self.middle(head)
        rightHead = mid.next            #finding right list Head
        midNode.next = None                 #breaking link with second part
        left = self.sortList(head)
        right = self.sortList(rightHead)
        return self.merge(left,right)   # merge the two lists and return the head of sorted list
        
    def middle(self,head):              #find mid of linked list for splittiong
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,lHead,rHead):      #merge the two sorted lists into one
        dummyNode = ListNode(-1)
        curr = dummyNode
        while lHead != None and rHead!=None:
            if lHead.val <= rHead.val:
                curr.next = lHead
                lHead = lHead.next
            else:
                curr.next = rHead
                rHead = rHead.next
            curr = curr.next
        if lHead or rHead:
            curr.next = lHead or rHead
        return dummyNode.next



# METHOD 2  -> using bottom-up merge sort   O(n) space complexity , O(nlogn) time complxty


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        step = 1                     #starting splitting step set of 1
        length = self.getsize(head)
        dummy = ListNode(-1)         # universal head of the sorted list
        dummy.next = head
        left, right, tail = None,None,None
        while step < length:
            curr = dummy.next
            tail = dummy
            while curr:
                left  = curr
                right = self.split(curr,step)         #making split after 1 nodes (set of 1 then 2,4,8)
                curr = self.split(right,step)         # breaking link after 1(step) node in right
                tail = self.merge(left,right,tail)    #attaching sorted list start to tail and return new tail 
            step<<=1                   # change step to 2,4,8....
        return dummy.next
        
    def getsize(self,head):      #find length of list
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    #split the list after n nodes:
    def split(self,head,step):
        count=1
        while head and count<step:
            head = head.next
            count+=1
        if head == None:            #check if reached end of list
            return None
        rightHead = head.next
        head.next = None
        return rightHead

    #merge the right and left list and return tail
    def merge(self,head1,head2,head):
        curr = head
        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        curr.next = head1 if head1 else head2
        while curr.next:
            curr = curr.next
        return curr         # returing the tail of the sorted list




        
