# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        begin = 0
        dict = {}
        if len(s) <= 1:
            return len(s)
        for i in range(len(s)):
            if dict.get(s[i]) != None:
                length = i - begin if i - begin > length else length
                begin = dict.get(s[i]) + 1 if dict.get(s[i]) + 1 > begin else begin
            dict[s[i]] = i
        length = max(length, i - begin + 1)
        return length