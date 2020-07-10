# coding: utf-8
# Time:  O(n * 4^n)
# Space: O(n)
#
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#

# Iterative Solution
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], [""]

        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result += [result[i % n] for i in xrange(n, m * n)]
            # print 'choices', choices, 'result', result

            for i in xrange(m * n):
                result[i] = choices[i / n] + result[i]
                # print 'result', result

        return result

# 假如是 “23” ，那么
#
# 第 1 次 外层for 循环结束后变为 ['', '', '']；
#
# 第 1 次 for 循环的第 1 次 内层for 循环分别加上 d e f，就变成 ['d', 'e', 'f']
#
# 第 2 次 外层for 循环结束后变为 ['d', 'e', 'f', 'd', 'e', 'f', 'd', 'e', 'f']；
#
# 第 2 次 for 循环的第 2 次 for 循环分别加上 a b c，就变成 ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']




# Time:  O(n * 4^n)
# Space: O(n)
# Recursive Solution
class Solution2:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecu(result, digits, lookup, "", 0)
        return result
    
    def letterCombinationsRecu(self, result, digits, lookup, cur, n):
        if n == len(digits):
            result.append(cur)
        else:
            for choice in lookup[int(digits[n])]:
                self.letterCombinationsRecu(result, digits, lookup, cur + choice, n + 1)



class Solution1:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []

        lookup, result = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], ['']
        for digit in reversed(digits):
            m, n = len(lookup[int(digit)]), len(result)
            result += [result[i%n] for i in xrange(n, m*n)]

            for i in xrange(m*n):
                result[i] = lookup[int(digit)][i/n] + result[i]

        return result



if __name__ == "__main__":
    print Solution1().letterCombinations("23")
