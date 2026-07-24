# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1, 2]

        fast = head
        slow = ListNode(0)
        dummy = slow
        slow.next = head

        # Move fast pointer up n spaces
        for i in range(n):
            if fast == None:
                break
            fast = fast.next

        # Progress both pointers until slow is one space before n
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
        