#https://leetcode-cn.com/problems/roman-to-integer/

class Solution(object):
    numList = [1000, 500, 100, 50, 10, 5, 1]
    strList = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    def findIndex(self, s):
        for index in range(len(self.strList)):
            if s == self.strList[index]:
                return index
        return -1

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = 0
        jump = 0
        for index in range(len(s)):
            if jump == 1:
                jump = 0
            else:
                if (index + 1) < len(s) and self.findIndex(s[index]) > self.findIndex(s[index+1]) and self.findIndex(s[index]) % 2 ==0:
                    nums += self.numList[self.findIndex(s[index + 1])] - self.numList[self.findIndex(s[index])]
                    jump = 1
                else:
                    nums += self.numList[self.findIndex(s[index])]

        return nums


solution = Solution()

#3
#str = 'III'

#1994
str = 'MCMXCIV'

print(solution.romanToInt(str))