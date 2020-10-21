# coding=utf-8
# Time:  O(m * n)
# Space: O(m + n)
#
# The demons had captured the princess (P) and imprisoned her 
# in the bottom-right corner of a dungeon. T
# he dungeon consists of M x N rooms laid out in a 2D grid. 
# Our valiant knight (K) was initially positioned in the top-left room 
# and must fight his way through the dungeon to rescue the princess.
# 
# The knight has an initial health point represented by a positive integer. 
# If at any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons, 
# so the knight loses health (negative integers) upon entering these rooms; 
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
# 
# In order to reach the princess as quickly as possible, 
# the knight decides to move only rightward or downward in each step.
# 
# 
# Write a function to determine the knight's minimum initial health 
# so that he is able to rescue the princess.
# 
# For example, given the dungeon below, the initial health of 
# the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
# 
# Notes:
# 
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters 
# and the bottom-right room where the princess is imprisoned.
#


class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1

        for i in reversed(xrange(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
            for j in reversed(xrange(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j + 1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)

        return DP[0]


# Time:  O(m * n logk), where k is the possible maximum sum of loses 
# Space: O(m + n)
class Solution2:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        maximum_loses = 0
        for rooms in dungeon:
            for room in rooms:
                if room < 0:
                    maximum_loses += abs(room)

        return self.binarySearch(dungeon, maximum_loses)

    def binarySearch(self, dungeon, maximum_loses):
        start, end = 1, maximum_loses + 1
        result = 0
        while start < end:
            mid = start + (end - start) / 2
            if self.DP(dungeon, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def DP(self, dungeon, HP):
        remain_HP = [0 for _ in dungeon[0]]
        remain_HP[0] = HP + dungeon[0][0]
        for j in xrange(1, len(remain_HP)):
            if remain_HP[j - 1] > 0:
                remain_HP[j] = max(remain_HP[j - 1] + dungeon[0][j], 0)

        for i in xrange(1, len(dungeon)):
            if remain_HP[0] > 0:
                remain_HP[0] = max(remain_HP[0] + dungeon[i][0], 0)
            else:
                remain_HP[0] = 0

            for j in xrange(1, len(remain_HP)):
                remain = 0
                if remain_HP[j - 1] > 0:
                    remain = max(remain_HP[j - 1] + dungeon[i][j], remain)
                if remain_HP[j] > 0:
                    remain = max(remain_HP[j] + dungeon[i][j], remain)
                remain_HP[j] = remain

        return remain_HP[-1] > 0


# 这题一看就是典型的动态规划问题，关键的难点是找到状态转移方程。
# 由于房间的数字有负有正，从前往后推导，比较难，需要更多的信息。
# 考虑从后往前，dp[i][j]表示(i,j)到公主房间所需的最小健康点数。
# 先考虑最后一个房间，是负数-5， 那就意味着到达该房间的点数必须大于等于5+1,才能存活。
# 如果房间是正数，就意味这，只要能进入该房间就行。也就是最低点数1。
# 所以该房间的最小健康点数=max(1, -dungeon[][] + 1);
# 这样从一个格子到下一个格子的状态转移方程就出来了：
# dp[i][j] = max(1, -dungeon[i][j]+min(dp[i+1][j],dp[i][j+1])) //只能向下或向右走

class Solution1:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        # 为了更好的处理边界情况，我们的二维 dp 数组比原数组的行数列数均多1个，先都初始化为最大值，
        # 由于我们知道到达公主房间后，骑士火拼完的血量至少为1，那么此时公主房间的右边和下边房间里的数字我们就都设置为1，
        # 这样到达公主房间的生存血量就是1减去公主房间的数字和1相比较，取较大值，就没有问题了
        dp = [[float("inf") for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1

        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                tmp = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, tmp - dungeon[i][j])

        return dp[0][0]


if __name__ == "__main__":
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]

    print Solution1().calculateMinimumHP(dungeon)

    dungeon = [[-200]]
    print Solution1().calculateMinimumHP(dungeon)

    dungeon = [[0, -3]]
    print Solution1().calculateMinimumHP(dungeon)