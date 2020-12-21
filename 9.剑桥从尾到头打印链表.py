"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

通过次数131,073提交次数174,024

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1


# class Solution:
#     def reversePrint(self, head: ListNode):
#         p = head
#         result = []

#         while not p.next is None:  # 遍历链表
#             result.append(p.val)
#             p = p.next
#         result.append(p.val)
#         # result = result[::-1]  # 添加最后一位值，切片会生成新的列表
#         result.reverse()
#         return result

# 解法2 递归
class Solution:
    def reversePrint(self, head: ListNode):

        # 终止条件 head 为假
        return self.reversePrint(head.next) + [head.val] if head else []


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    a.next = b
    b.next = c
    s = Solution()
    result = s.reversePrint(a)
    print(result)
