#https://leetcode-cn.com/problems/remove-element/
#关键是O1的 额外空间消耗
from typing import List

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        total = 0
        #受限于空间，先将VAL全部替换到队尾
        for index in range(len(nums)):
            if nums[index] == val:
                #exchange,注意交换的下标不能超过当前正向查找的下标
                for indexRevert in range(1, len(nums) - index):
                    if nums[-indexRevert] != val:
                        nums[index] = nums[-indexRevert]
                        nums[-indexRevert] = val
                        break
        #从队尾开始POP数据并计数
        while True:
            if nums[-1] == val:
                total += 1
                nums.pop(-1)
            else:
                break

        return total

nums:List[int] = [3,2,2,3]
val:int =3

#nums  = [0,1,2,2,3,0,4,2]
#val = 2

solution = Solution()
print(solution.removeElement(nums, val))
print(nums)