# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        A = head
        B = A.next
        A.next = self.swapPairs(B.next)
        B.next = A
        return B



head = ListNode(4)
head = ListNode(3, head)
head = ListNode(2, head)
head = ListNode(1, head)

s = Solution()
head = s.swapPairs(head)
while head:
    print(head.val)
    head = head.next
