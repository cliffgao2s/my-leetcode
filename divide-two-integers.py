#https://leetcode-cn.com/problems/divide-two-integers/
#不可用 乘法 除法  MOD
#不能直接用减法实现，考虑 被除数特别大，而除数又特别小，运算会超时；
#不用位移，采用二分法，不停用 除数的N次幂去裁剪区域 + 迭代
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        changeExp = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            changeExp = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
           result = dividend
        else:
            result = self.subCount(dividend, divisor)

        if changeExp:
            result = - result

        if result > 2**31 - 1 or result < -2**31:
            if changeExp:
                result = -2**31
            else:
                result = 2**31 - 1

        return  result

    def subCount(self, bc, cs):
        if bc < cs:
            return 0
        if bc == cs:
            return 1

        for index in range(1,32):
            if cs**index >= bc:
                return cs**(index-2) + self.subCount(bc-cs**(index-1), cs)

solution = Solution()
#divend = -10
#divsor = 3

divend = -2147483648
divsor = -1

print(solution.divide(divend, divsor))

