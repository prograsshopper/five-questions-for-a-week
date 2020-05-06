class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or not head or not head.next:
            return head
        
        first = prev = ListNode(0)
        first.next = head
        
        for _ in range(0, m-1):
            prev = prev.next
        current = prev.next
        
        rev_list = []
        for _ in range(0, n-m+1):
            rev_list.append(current.val)
            current = current.next
        
        rev_head = ListNode(0)
        rev_current = rev_head
        for _ in range(0, n-m+1):
            rev_current.next = ListNode(rev_list.pop())
            rev_current = rev_current.next
        
        rev_current.next = current
        prev.next = rev_head.next
        
        return first.next
