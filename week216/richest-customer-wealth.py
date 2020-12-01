#https://leetcode-cn.com/contest/weekly-contest-217/problems/richest-customer-wealth/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        maxNum = 0

        for item1 in accounts:
            temp = 0
            for item2 in item1:
                temp += item2
            
            if temp > maxNum:
                maxNum = temp

        return maxNum


solution = Solution()

#17
accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(solution.maximumWealth(accounts))