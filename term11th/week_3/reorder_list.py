class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Runtime: 120 ms, faster than 14.48% of Python3 online submissions for Reorder List.
        if not head or not head.next:
            return head
        from collections import deque
        val_deque = deque()
        node = head.next
        while node:
            val_deque.append(node.val)
            node = node.next
        temp_node = head
        count = 1
        while val_deque:
            if count % 2 == 0:
                temp_node.next = ListNode(val_deque.popleft())
            else:
                temp_node.next = ListNode(val_deque.pop())
            count += 1
            temp_node = temp_node.next
