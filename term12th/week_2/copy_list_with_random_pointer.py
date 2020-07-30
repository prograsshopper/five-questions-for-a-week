"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new_head = temp = Node(0)
        dic = {}
        while head:
            if head not in dic:
                dic[head] = Node(head.val)
            temp.next = dic[head]
            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val)
                temp.next.random = dic[head.random]
            temp = temp.next
            head = head.next
        return new_head.next
