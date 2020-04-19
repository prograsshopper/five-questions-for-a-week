# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# first solution
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:       
#         if not l1 or not l2:
#             return l1 if not l2 else l2
#         num1 = 0
#         ten = 0
#         while l1:
#             num1 += (l1.val) * (10**ten)
#             l1 = l1.next
#             ten += 1
#         num2 = 0
#         ten = 0
#         while l2:
#             num2 += (l2.val) * (10**ten)
#             l2 = l2.next
#             ten += 1
#         result_list = [int(num) for num in str(num1 + num2)]
#         result_node = ListNode(result_list.pop())
#         current_node = result_node
#         while result_list:
#             current_node.next = ListNode(result_list.pop())
#             current_node = current_node.next
#         return result_node

# second  55.67%
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:       
        head = current_node = ListNode(0)
        remain = 0
        while l1 or l2 or remain:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current_val = val1 + val2 + remain
            current_node.next = ListNode(current_val%10)
            current_node = current_node.next
            remain = current_val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
