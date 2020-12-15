'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 双指针法
# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         a = 0
#         b = 1
#         lenth = len(nums)
#         nums.sort()
#         while b < lenth:
#             if nums[a] == nums[b]:
#                 b += 1
#                 return nums[a]
#             else:
#                 a += 1
#                 b += 1

# hash 法


# class Solution:
#     def findRepeatNumber(self, nums) -> int:
#         hash = {}
#         for num in nums:
#             print(num)
#             if not hash.get(num) is None: # 如果用if hash.get(num) 判断，会出现错误。
#                 print(num)
#                 return num
#             else:
#                 hash[num] = num

# 原地置换法 使用哈希表原理，一个索引对应多个值，如果索引不想等，值却一样，可以确定是重复了
class Solution:
    def findRepeatNumber(self, nums) -> int:
        for index, val in enumerate(nums):
            if index != val and nums[val] == val:
                return val
            else:
                nums[val], nums[index] = nums[index], nums[val]  # 交换变量，改变数组


if __name__ == "__main__":
    s = Solution()
    result = s.findRepeatNumber([0, 1, 0])
    print(result)
