#https://leetcode-cn.com/contest/weekly-contest-218/problems/concatenation-of-consecutive-binary-numbers/
#只要求得 最后长度在 len(modBinBase) 范围内的值即可，然后取异或

class Solution:
    modBinBase = '111011100110101100101000000111'
    
    def concatenatedBinary(self, n: int) -> int:
        sumStr = ""

        for index in range(n, 0 , -1):
            subStr = str(bin(index))
            subList = subStr.split("0b")
            sumStr = subList[1] + sumStr

            #计算和sumStr 在 modBinBase内的和值
            if len(sumStr) >= len(self.modBinBase):
                break
        
        print(sumStr)
        if len(sumStr) >= len(self.modBinBase):
            sumStr = sumStr[len(sumStr) - len(self.modBinBase) :]
        else:
            return int(sumStr,2)

        print(sumStr)
        
        #取异或
        temStr = ''
        for index in range(min(len(self.modBinBase), len(sumStr))):
            if sumStr[index] != self.modBinBase[index]:
                temStr += '1'
            else:
                temStr += '0'
        
        print(temStr)
        return int(temStr,2)



solution = Solution()
#27
#n = 3

#505379714
n = 12
print(solution.concatenatedBinary(n))

