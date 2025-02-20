from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(digits):
    dummy = ListNode()
    current = dummy
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy.next

l1 = create_linked_list([2, 4, 3]) 
l2 = create_linked_list([5, 6, 4])  

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")

solution = Solution()

result = solution.addTwoNumbers(l1, l2)

print_linked_list(result)