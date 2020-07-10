# coding: utf-8
# Time:  O(n)
# Space: O(n)
#
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#

# Manacher's Algorithm
# https://www.cnblogs.com/bitzhuwei/p/longest-palindromic-substring-part-ii.html
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T +=  ['#', c]
            T += ['#', '$']
            return T

        # 预处理后的字符串
        T = preProcess(s)
        # p[i] 表示以i为中心的回文长度
        P = [0] * len(T) 
        center, right = 0, 0
        for i in xrange(1, len(T) - 1):
            i_mirror = 2 * center - i
            # 当前i在center和right之间，可以利用回文的对称性
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0
            # i处的回文可能超出C的大回文范围了
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]       
        
        max_i = 0
        for i in xrange(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) / 2
        return s[start: start + P[max_i]]



class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def preProcess(s):
            if len(s) == 0:
                return ['^', '$']

            T = ['^']
            for i in s:
                T += ['#', i]
            T += ['#', '$']
            return T

        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in range(1, len(T)-1):
            mirror_i = center - (i - center)
            if right > i:
                P[i] = min(right-i, P[mirror_i])
            else:
                P[i] = 0

            while(T[i +1 + P[i]] == T[i-1 -P[i]]):
                P[i] +=1
            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i =0
        for i in range(1, len(T)-1):
            if P[i] > P[max_i]:
                max_i = i

        start = (max_i-1-P[max_i])/2
        print start
        return s[start:start+P[max_i]]


    
if __name__ == "__main__":
    print Solution1().longestPalindrome("abaaba")



