# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         map = {}
#         for i, num in enumerate(nums):
#             if (target - num) in map:
#                 return [ map[target-num], i]
#             map[num] = i


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i, num in enumerate(nums):
            mapping[num] = i

        result = []
        for num in nums:
            tmp = target - num
            if tmp in mapping:
                result.append(mapping[num])
                result.append(mapping[tmp])
                break

        return result


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print s.twoSum(nums, target)
