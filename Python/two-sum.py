# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = l3 = ListNode(-1)
    tmp = 0
    while l1 and l2:
        import pdb
        pdb.set_trace()
        value = (l1.val + l2.val + tmp) % 10
        tmp = (l1.val + l2.val + tmp) / 10
        l3.next = ListNode(value)
        l3 = l3.next
        l1 = l1.next
        l2 = l2.next
    while l1:
        value = (l1.val + tmp) % 10
        tmp = (l1.val + tmp) / 10
        l3.next = ListNode(value)
        l3 = l3.next
        l1 = l1.next
    while l2:
        value = (l2.val + tmp) % 10
        tmp = (l2.val + tmp) / 10
        l3.next = ListNode(value)
        l3 = l3.next
        l2 = l2.next
    if tmp:
        l3.next = ListNode(tmp)

    return head.next

l1 = ListNode(9)
l1.next = ListNode(9)
l2 = ListNode(1)

result = addTwoNumbers(l1, l2)

while result:
    print result.val
    result = result.next
