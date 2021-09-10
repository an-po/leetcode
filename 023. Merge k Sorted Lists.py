class Solution:
    def mergeKLists(self, lists) -> ListNode:
        self.vals = list()
        for li in lists:
            while li:
                self.vals.append(li.val)
                li = li.next

        self.vals.sort()

        head = ListNode(0)
        point = head
        for val in self.vals:
            point.next = ListNode(val)
            point = point.next
        return head.next