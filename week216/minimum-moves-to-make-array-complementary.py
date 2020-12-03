#https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/

'''
在1+a处，操作次数减少一次；
在a+b处，操作次数减少一次；
在a+b+1处，操作次数增加一次；
在b+limit+1处，操作次数增加一次。
'''

class Solution:
    def minMoves(self, nums: [int], limit: int) -> int:
        resultList = []
        minMoves = 0

        #构造1个limit*2的数组,假设每个TARGET数据上  对折的数字 平均移动1步即可
        for index in range(limit * 2 + 2):
            resultList.append((int)(len(nums)/2))
        
        for index in range((int)(len(nums)/2)):
            add1 = min(nums[index], nums[-index - 1])
            minus1 = nums[index] + nums[-index - 1]
            add2 = max(nums[index], nums[-index - 1]) + limit + 1

            resultList[minus1] -= 1
            resultList[add1] += 1
            resultList[add2] += 1

        print(resultList)

        #要注意访问下标，因为SUM的最小值是2
        minMoves = resultList[2]
        for index in range(3, 2*limit + 1):
            if minMoves > resultList[index]:
                minMoves = resultList[index]

        return minMoves
        
solution = Solution()


#1
nums = [1,2,4,3]
limit = 4

#2
#nums = [1,2,2,1]
#limit = 2

#0
#nums = [1,2,1,2]
#limit = 2


#4
#nums = [20744,7642,19090,9992,2457,16848,3458,15721]
#limit = 22891

print(solution.minMoves(nums, limit))