# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:       
        rem = 0
        result_node = cur_node = ListNode(0)
        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cur_val = val1 + val2 + rem
            if cur_val >= 10:
                rem = 1
                cur_val %= 10
            else:
                rem = 0
            cur_node.next = ListNode(cur_val) 
            cur_node = cur_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result_node.next