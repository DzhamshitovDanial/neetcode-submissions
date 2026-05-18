# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        left=head
        right=head
        while right is not None and right.next is not None:
            right=right.next.next
            left=left.next
            if left==right:
                return True
        return False