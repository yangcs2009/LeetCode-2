# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.
#


class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in lookup:
                stack.append(c)
            elif len(stack) == 0 or lookup[stack.pop()] != c:
                return False
        return len(stack) == 0


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
    
if __name__ == "__main__":
    print Solution1().isValid("()[]{}")
    print Solution1().isValid("()[{]}")