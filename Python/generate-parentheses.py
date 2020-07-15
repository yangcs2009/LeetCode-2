# coding: utf-8
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

# 思考方式是采用DFS
# 如果左括号还能括就不断的画左括号,直到左括号的数量等于n
# 接下来考虑右括号,因为对于一对括号,右括号不能出现在左括号前,所以当右括号数量小于左括号时,加上右括号
# 当左右括号数量都等于n时,得到解


class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result
    
    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)

if __name__ == "__main__":
    print Solution().generateParenthesis(3)