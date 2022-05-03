class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None: return None
        
        counter = 0
        
        pointer1 = head
        pointer2 = head
        
        for i in range(n):
            counter += 1
            pointer2 = pointer2.next
        
        while pointer2!= None:
            counter += 1
            prev = pointer1
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
    
        if counter == n and pointer1:
            return head.next
            
        prev.next = pointer1.next
        
        return head
