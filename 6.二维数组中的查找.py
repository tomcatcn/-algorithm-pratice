'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解法1 遍历法


# class Solution:
#     def findNumberIn2DArray(self, matrix, target: int) -> bool:
#         if not matrix:
#             return False
#         n = len(matrix)
#         s = len(matrix[0])
#         for i in range(n):
#             for j in range(s):
#                 if target == matrix[i][j]:
#                     return True
#         return False

# 解法2 找规律 左下角开始找，比目标大向右找，比目标小，向上找


class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        # 数组为空直接返回结果
        if not matrix:
            return False
        # 左下角开始遍历
        row, clo = len(matrix) - 1, 0
        while row >= 0 and not clo == len(matrix[0]):
            # 比目标大，向上找
            if matrix[row][clo] > target:
                row -= 1
            # 比目标小，向右找
            elif matrix[row][clo] < target:
                clo += 1
            elif matrix[row][clo] == target:
                return True
        return False


if __name__ == "__main__":
    matrix = [
        [-5]
    ]
    s = Solution()
    result = s.findNumberIn2DArray(matrix, -5)
    print(result)
