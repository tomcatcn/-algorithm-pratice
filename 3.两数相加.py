'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l3是求和结果的节点，p用来遍历l3节点，l3和p指向头结点
        l3 = p = ListNode(None)
        # 初始化进位
        s = 0
        # 循环条件l1 or l2 or s
        while l1 or l2 or s:
            s = s + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # 连接新的节点，l1.val+l2.val 的结果位
            p = p.next  # 向下取一位
            s = s // 10  # 进位结果0或者1
            l1 = (l1.next if l1 else None)  # 如果l1为空,代表遍历到头了
            l2 = (l2.next if l2 else None)  # 如果l2为空,代表遍历到头了
        return l3.next  # 头节点是空节点，需要取下一位
