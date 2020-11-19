#coding:utf-8
#https://leetcode-cn.com/problems/number-of-segments-in-a-string/
#实现复杂了点，核心思想还是迭代，归并为子问题再去算子串的长度
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        print("++++++++++++++++ %s" % (s))

        if len(s) == 0:
            return 0

        if ' ' not in s:
            return 1

        if s[0] == ' ':
            return self.countSegments(s[1:])
        else:
            for index in range(len(s)):
                if s[index] == ' ':
                    return 1 + self.countSegments(s[index:])


solution = Solution()

#str = "Hello, my name is John"
str = ' 111 '
print(solution.countSegments(str))