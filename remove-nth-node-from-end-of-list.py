#https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
#双指针，1个指向最后 1个指向-N位置

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        listNodePtr1 = head
        listNodePtr2 = head
        index = 1

        while True:
            if index > n:
                listNodePtr1 = listNodePtr1.next
                listNodePtr2 = listNodePtr2.next
            else:
                listNodePtr1 = listNodePtr1.next
            index += 1
            #已经到达尾部
            if listNodePtr1.next == None:
                listNodePtr2.next = listNodePtr2.next.next
                break
        return head


solution = Solution()

listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode1.next = listNode2
listNode3 = ListNode(3)
listNode2.next = listNode3
listNode4 = ListNode(4)
listNode3.next = listNode4
listNode5 = ListNode(5)
listNode4.next = listNode5

solution.removeNthFromEnd(listNode1, 3)

head = listNode1
while head != None:
    print(head.val)
    head = head.next