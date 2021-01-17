#https://leetcode-cn.com/contest/weekly-contest-216/problems/smallest-string-with-a-given-numeric-value/
#问题演化为 迭代到最后1个数字 在 1-26范围内; 还要使得使用 小字母的数量最大  ；需要把迭代的结果都列出来比较

#开销小的做法应该是  迭代， 每次都取从A开始 最小值，看有没有解；如果没有则扩充到B，以此类推

class Solution(object):

    listAlpha = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            if k >= 1 and k <= 26:
                return self.listAlpha[k]
            else:
                return ''

        for index in range(1, len(self.listAlpha)):
            strSub = self.getSmallestString(n-1, k-index)
            if strSub != '':
                return self.listAlpha[index] + strSub
                    

        return ''

solution = Solution()

#'aay'
#n = 3
#k = 27

#"aaszz"
n = 5
k = 73


#n = 24
#k = 552

print(solution.getSmallestString(n, k))