# coding: utf-8
# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

# 思想： 其实是从右向左找到第一个数字不再递增的位置，然后从右边找到一个刚好大于当前位的数字即可
# https://www.bookstack.cn/read/wind-liang-eetcode/bbf257c543619182.md

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in xrange(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i
                
        if k == -1:
            num.reverse()
            return
        
        for i in xrange(k + 1, len(num)):
            if num[i] > num[k]:
                l = i
                
        num[k], num[l] = num[l], num[k]
        num[k + 1:] = num[:k:-1]


class Solution1(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return
        k = -1
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                k = i-1
                break
        if k < 0:
            for i in xrange(len(nums)/2):
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            return

        for i in xrange(len(nums)-1, k, -1):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break

        nums[k+1:] = nums[:k:-1]


if __name__ == "__main__":
    num = [4, 3, 2, 1]
    Solution1().nextPermutation(num)
    print num
