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
        def merge2lists(lst1, lst2):
            if lst1 is None:
                return lst2
            if lst2 is None:
                return lst1
            if lst1.val < lst2.val:
                lst1.next = merge2lists(lst1.next, lst2)
                return lst1
            else:
                lst2.next = merge2lists(lst1, lst2.next)
                return lst2

        result = None
        for lst in lists:
            result = merge2lists(result, lst)

        return result


class Solution3:
    def mergeKLists(self, lists) -> ListNode:
        all_nodes = dict()
        for node in lists:
            while node is not None:
                all_nodes[node.val] = all_nodes.get(node.val, 0) + 1
                node = node.next

        head = None

        for val in range(-10000, 10000 + 1):
            if val in all_nodes:
                count = all_nodes[val]
                while count > 0:
                    if head is None:
                        head = ListNode(val)
                        node = head
                    else:
                        node.next = ListNode(val)
                        node = node.next
                    count -= 1
        return head


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
