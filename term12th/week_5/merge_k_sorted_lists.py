# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for elem in lists:
            while elem:
                nums.append(elem.val)
                elem = elem.next
        nums.sort()
        head = ListNode(0)
        current = head
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return head.next