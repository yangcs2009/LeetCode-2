# coding: utf-8
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
import collections


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 主要思想是，遍历数组，用 0 减去当前的数，作为 sum ，然后再找两个数使得和为 sum
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            # 为了保证不加入重复的 list,因为是有序的，所以如果和前一个元素相同，只需要继续后移就可以
            if i == 0 or nums[i] != nums[i - 1]:
                # 两个指针,并且头指针从i + 1开始，防止加入重复的元素
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        # 元素相同要后移，防止加入重复的 list
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            # else会超时
            i += 1
        return result

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = collections.Counter(nums)
        nums_2 = [x[0] for x in d.items() if x[1] > 1]
        nums_new = sorted([x[0] for x in d.items()])
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_new):
            if j <= 0:
                numss2 = nums_new[i + 1:]
                for x, y in enumerate(numss2):
                    if 0 - j - y in [j, y] and 0 - j - y in nums_2:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
                    if 0 - j - y not in [j, y] and 0 - j - y in nums_new:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn

if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print result
