#https://leetcode-cn.com/contest/weekly-contest-218/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums.sort()

        opTimes = 0

        while len(nums) > 1:
            if nums[0] > (int)(k/2):
                break

            op1 = nums[0]
            op2 = nums[-1]

            if op1 + op2 < k:
                nums.pop(0)
            elif op1 + op2 == k:
                opTimes += 1
                nums.pop(0)
                nums.pop(-1)
            else:
                nums.pop(-1)
        return opTimes




#1
nums = [3,1,3,4,3]
k = 6


solution = Solution()

print(solution.maxOperations(nums, k))
