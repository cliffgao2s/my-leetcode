#https://leetcode-cn.com/problems/integer-to-roman/

#对于罗马字母  注意 9 和 4 2个数字即可，我这里是写成numlist strlist 2个对应的数字和字母数组，正好对应奇数和偶数的下标，方便判断是否4 9
class Solution(object):
    numList = [1000, 500, 100, 50, 10, 5, 1]
    strList = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        print("+++++++++++++++ %d" % (num))

        #最低位数字后续逻辑处理越界麻烦，直接给出结果
        if num < 5:
            if num < 4:
                temp = ''
                for index in range(num):
                    temp += 'I'
                return temp
            else:
                return 'IV'

        for index in range(len(self.numList)):
            if num >= self.numList[index]:
                if index % 2 == 1:  #对于 500 50 5 要判断首位是否9或4特殊处理
                    if (int)(num / self.numList[index+1]) == 9:
                        return self.strList[index+1] + self.strList[index-1] + self.intToRoman((int)(num%self.numList[index + 1]))
                    else:
                        return self.strList[index] + self.intToRoman((int)(num%self.numList[index]))
                else:
                    if (int)(num / self.numList[index]) == 4:
                        return self.strList[index] + self.strList[index - 1] + self.intToRoman((int)(num % self.numList[index]))
                    else:
                        temp = ''
                        for i in range((int)(num/self.numList[index])):
                            temp += self.strList[index]
                        return temp + self.intToRoman((int)(num%self.numList[index]))



solution = Solution()

#MCMXCIV
#num = 1994

#IX
#num = 9

#LVIII
#num = 58

#XL
#num = 40

num=45

print(solution.intToRoman(num))