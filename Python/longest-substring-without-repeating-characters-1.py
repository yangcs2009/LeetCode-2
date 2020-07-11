# coding: utf-8# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 边界检测
        if len(s) <= 1:
            return len(s)
        tmp_max = 0
        start = 0
        dic = {}
        for i, char in enumerate(s):
            if char in dic:
                tmp_max = max(tmp_max, i - start)
                # 防止 abba类型 start回退
                start = max(dic[char] + 1, start)
            dic[char] = i
        # i-start+1 是 abcd类型
        return max(tmp_max, i-start+1)


s = Solution()
string = 'abcabcbb'
# string = 'bbbbb'
#string = 'pwwkew'
string = 'abcadefa'
string = 'abba'
# string = ''

print s.lengthOfLongestSubstring(string)