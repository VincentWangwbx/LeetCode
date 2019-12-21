# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from timer import func_timer

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:'''
        penalty = 0
        if l1.val + l2.val < 10:
            head = ListNode(l1.val + l2.val)
        else:
            head = ListNode(l1.val + l2.val - 10)
            penalty = 1
        current = head
        l1 = l1.next
        l2 = l2.next
        while l1 != None or l2 != None or penalty == 1:
            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)
            value = l1.val + l2.val + penalty
            node = ListNode(value % 10)
            penalty = int((value - (value % 10))/10)
            current.next = node
            current = node
            l1 = l1.next
            l2 = l2.next
        return head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    l1 = ListNode(2)    #(2 -> 4 -> 3)
    b = ListNode(4)
    c = ListNode(3)
    l1.next = b
    b.next = c

    l2 = ListNode(5)    #(5 -> 6 -> 4)
    e = ListNode(6)
    f = ListNode(4)
    l2.next = e
    e.next = f

    solution = Solution()
    answer = solution.addTwoNumbers(l1,l2)

    while True:
        try:
            a = answer.val
        except:
            break
        else:
            print(a, end='')
            answer = answer.next