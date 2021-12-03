# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def on_screen(self):
        def rec(obj):
            if obj is not None:
                print(obj.val)
                rec(obj.next)
        rec(self)


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        head = None
        next = None
        while True:
            min_node = None
            for i, node in enumerate(lists):
                if node is not None:
                    if min_node is None:
                        min_node = node
                        min_index = i
                    if node.val < min_node.val:
                        min_node = node
                        min_index = i
            if min_node is None:
                return head
            if head is None:
                head = min_node
                next = head
                lists[min_index] = lists[min_index].next
            else:
                next.next = min_node
                next = next.next
                lists[min_index] = lists[min_index].next



class Solution2:
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

lst = [0] * 3
lst[0] = ListNode(1)
lst[0].next = ListNode(4)
lst[0].next.next = ListNode(5)

lst[1] = ListNode(1)
lst[1].next = ListNode(3)
lst[1].next.next = ListNode(4)

lst[2] = ListNode(2)
lst[2].next = ListNode(6)

c = Solution()
ans = c.mergeKLists(lst)
ans.on_screen()

