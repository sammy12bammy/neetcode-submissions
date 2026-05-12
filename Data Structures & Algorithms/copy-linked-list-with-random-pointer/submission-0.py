"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = collections.defaultdict(lambda: Node(0))
        temp[None] = None

        cur = head
        while cur:
            temp[cur].val = cur.val
            temp[cur].next = temp[cur.next]
            temp[cur].random = temp[cur.random]
            cur = cur.next
        return temp[head]