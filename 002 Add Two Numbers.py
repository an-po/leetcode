# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L3 = ListNode(0)
        l3 = L3
        d = 0
        while True:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next

            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            val3 = (val1 + val2 + d) % 10
            d = (val1 + val2 + d) // 10
            l3.val += val3
            l3.next = ListNode(0)
            if l1 is None and l2 is None and d == 0:
                l3.next = None
                break
            l3 = l3.next
        return L3