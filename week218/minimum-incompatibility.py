#https://leetcode-cn.com/problems/minimum-incompatibility/
#分为K个大小相同子集，且子集内不能有相同数字，还要使子集MAX-MIN SUM值最小

#DFS, 从最大值开始倒查，找到他的最优解，然后依次找剩下的； 如果剩下的满足条件，递归解决找到能满足条件的次优解

from typing import List

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        #排序
        nums.sort()
        
        #每个分组的长度
        gridLen = (int)(len(nums) / k)

        if len(nums) % k != 0:
            return -1
        
        countNum = 0
        countTimes = 0

        for item in nums:
            if item == countNum:
                countTimes += 1
                if countTimes > gridLen:
                    return -1
            else:
                countNum = item
                countTimes = 1 
        
        minGap  = 0

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