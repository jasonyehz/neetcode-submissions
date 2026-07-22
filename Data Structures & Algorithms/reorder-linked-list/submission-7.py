# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        slowPrev = slow

        #finding the middle
        if head == None or head.next == None:
            return
        else:
            while fast and fast.next:
                slowPrev = slow
                slow = slow.next
                fast = fast.next.next

        prev = None
        current = slow #middle (first element of right side)

        #reversing the second half
        while current != None:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext

        # Making the last element of left half end with None
        slowPrev.next = None
        p1 = head
        p2 = prev

        # Alternating the nodes
        while p1 != None:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p1 = p1next

            if p1 == None:
                break
            p2.next = p1
            p2 = p2next




