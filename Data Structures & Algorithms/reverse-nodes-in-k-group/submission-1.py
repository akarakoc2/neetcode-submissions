# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find the kth connection break
        list1 = head
        curr = list1

        # manage the edge case that there are at least k in the linked list
        for i in range(k - 1):
            if not curr:
                return head
            curr = curr.next
        if not curr:
            return head

        # save the rest of the list and snip the connection after the kth node
        list2 = curr.next
        curr.next = None

        # reverse the first k nodes
        list1_reversed = self.reverseList(list1)

        # recursively reverse the rest of the list and connect it to the new tail (list1)
        list1.next = self.reverseKGroup(list2, k)
        return list1_reversed


    # reversing any list 
    def reverseList(self, l):
        curr = l
        prev = None
        
        while curr:
            nextNode = curr.next
            curr.next = prev 
            prev = curr
            curr = nextNode
        return prev

            
        




        

