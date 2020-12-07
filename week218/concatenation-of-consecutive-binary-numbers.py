#https://leetcode-cn.com/contest/weekly-contest-218/problems/concatenation-of-consecutive-binary-numbers/
#只要求得 最后长度在 len(modBinBase) 范围内的值即可，然后取异或

class Solution:
    modBinBase = '111011100110101100101000000111'
    
    def concatenatedBinary(self, n: int) -> int:

        ss=""
        for i in range(n+1):
            ss+=(bin(i)[2:])

        print(ss)
        return int(ss,2) % 1000000007



solution = Solution()
#27
#n = 3

#505379714
n = 12
print(solution.concatenatedBinary(n))

