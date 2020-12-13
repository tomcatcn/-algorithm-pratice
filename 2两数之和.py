'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def twoSum(self, nums, target: int):
        nums_dict = {}
        # 把列表转换成字典，值作为字典KEY, index作为字典值，这样就能去掉重复元素，且这个重复元素的索引是最大的哪一个
        for index, num in enumerate(nums):
            nums_dict[num] = index
        for i, num in enumerate(nums):
            # 取出J，如果 J存在，且 i 不等于 j ，因为不相等，说明了就不是一个同一个索引。
            j = nums_dict.get(target - num)
            if j is not None and i != j:
                return [i, j]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 5, 5, 11], 10))
