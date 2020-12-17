'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串长度为空，返回0
        if not s:
            return 0
        n = len(s)
        # 设置一个窗口，保存不重复字符串
        window = list()
        # 最大窗口长度，也就是不重复子串的长度
        max_lenth = 0
        # 当前窗口的长度
        cur_lenth = 0
        # 遍历字符串
        for i in range(n):
            val = s[i]
            # 如果字符串不在窗口内，则添加进去，并更新当前长度
            if not val in window:
                window.append(val)
                cur_lenth += 1
            # 在窗口内
            else:
                # 获取字符串在窗口的索引
                index = window.index(val)
                # 把窗口更新为不重复的字符串，从重复字符串的位置开始切片
                window = window[index + 1:]
                # 把字符串添加进窗口
                window.append(val)
                # 更新当前窗口长度
                cur_lenth = len(window)
            # 更新最大窗口长度
            if cur_lenth > max_lenth:
                max_lenth = cur_lenth

        return max_lenth


if __name__ == "__main__":
    s = Solution()
    result = s.lengthOfLongestSubstring("")
    print(result)
