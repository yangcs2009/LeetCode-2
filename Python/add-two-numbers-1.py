# coding=utf-8
# coding = utf-8
# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(-1)
        tmp = 0
        while l1 and l2:
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


a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(5)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)

s = Solution()
result = s.addTwoNumbers(a, b)
while result:
    print result.val
    result = result.next
