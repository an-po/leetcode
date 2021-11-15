# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        def rec(node):
            if node.next is None:
                cur_number = 1
            else:
                cur_number = rec(node.next) + 1
            if cur_number == n + 1:
                node.next = node.next.next
            return cur_number
        cur_number = rec(head)
        if cur_number == n:
            return head.next
        else:
            return head


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
n = 1
head = s.removeNthFromEnd(head, n)

while head is not None:
    print(head.val)
    head = head.next