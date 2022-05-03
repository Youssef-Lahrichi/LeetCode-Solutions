class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = ""
        number2 = ""
        while True:
            if l1.next == None:
                break
            else:
                number1 += str(l1.val)
                l1 = l1.next
                
        while True:
            if l2.next == None:
                break
            else:
                number2 += str(l2.val)
                l2 = l2.next
        number1 += str(l1.val)
        number2 += str(l2.val)  
        
        final = str(int(number1[::-1]) +int(number2[::-1]))[::-1]
        head = ListNode(int(final[0]))
        temp = head
        for i in range(1, len(final)):
            temp.next = ListNode(int(final[i]))
            temp = temp.next
        return head
