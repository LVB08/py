"""
合并两个有序链表
https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


if __name__ == '__main__':
    # l1 = [1,2,4], l2 = [1,3,4]
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    y = mergeTwoLists(l1, l2)
    while y is not None:
        print(y.val, end="\t")
        y = y.next
    print()


