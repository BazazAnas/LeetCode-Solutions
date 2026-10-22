# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        n = len(vals)
        return max(vals[i] + vals[n - 1 - i] for i in range(n // 2))
        