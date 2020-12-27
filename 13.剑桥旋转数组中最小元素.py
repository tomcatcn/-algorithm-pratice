"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

通过次数126,905提交次数256,898

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 解法一冒泡排序取最小


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return

        n = len(numbers)
        for i in range(n-1):
            for j in range(i+1, n):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers[0]

# 解法二：找规律
# 小于前一个元素的元素是最小的元素，如果没有找到就是第一个元素。（该数组最开始的0个元素搬到数组的末尾）


class Solution:
    def minArray(self, numbers) -> int:
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                return numbers[i+1]
        return numbers[0]
