#https://leetcode-cn.com/problems/minimum-incompatibility/
#分为K个大小相同子集，且子集内不能有相同数字，还要使子集MAX-MIN SUM值最小

from typing import List

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()

        if len(nums) % k != 0:
            return -1
        
        minGap  = 0
        #每个分组的长度
        gridLen = (int)(len(nums) / k)

        for index in range(k):
            gridTemp = []
            for item in nums:
                if item not in gridTemp and len(gridTemp) < gridLen:
                    gridTemp.append(item)
                    if len(gridTemp) == gridLen:
                        break
            
            if len(gridTemp) == gridLen:
                print(gridTemp)
                minGap += gridTemp[-1] - gridTemp[0]

                for item in gridTemp:
                    nums.remove(item)
            else:
                return -1

        return minGap


solution = Solution()

#6
nums = [6,3,8,1,3,1,2,2]
k = 4

print(solution.minimumIncompatibility(nums, k))

#贪心并不能得到最优解
'''class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()

        if len(nums) % k != 0:
            return -1
        
        minGap  = 0
        #每个分组的长度
        gridLen = (int)(len(nums) / k)

        for index in range(k):
            gridTemp = []
            for item in nums:
                if item not in gridTemp and len(gridTemp) < gridLen:
                    gridTemp.append(item)
                    if len(gridTemp) == gridLen:
                        break
            
            if len(gridTemp) == gridLen:
                print(gridTemp)
                minGap += gridTemp[-1] - gridTemp[0]

                for item in gridTemp:
                    nums.remove(item)
            else:
                return -1

        return minGap
'''