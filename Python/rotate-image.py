# coding: utf-8
# Time:  O(n^2)
# Space: O(1)
#
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?
#


# Time:  O(n^2)
# Space: O(1)
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        # anti-diagonal mirror
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        # horizontal mirror
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        return matrix


# Time:  O(n^2)
# Space: O(n^2)
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]


class Solution1(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        # 以对角线为中心，交换数据
        for i in xrange(length):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # 以竖中心线为中心，交换数据
        for i in xrange(length):
            for j in xrange(length / 2):
                matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]
        return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print matrix
    print Solution1().rotate(matrix)

