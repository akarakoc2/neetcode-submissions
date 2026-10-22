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
        stock = {}
        dummy = Node(0)
        newNode = dummy
        curr = head

        while curr:
            if curr not in stock:
                newNode.next = Node(curr.val)
                stock[curr] = newNode.next
            else:
                newNode.next = stock[curr]

            if curr.random not in stock:
                if curr.random is not None:
                    newNode.next.random = Node(curr.random.val)
                    stock[curr.random] = newNode.next.random
                else:
                    newNode.next.random = None
            else:
                newNode.next.random = stock[curr.random]

            curr = curr.next
            newNode = newNode.next

        return dummy.next



        