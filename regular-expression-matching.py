#coding:utf-8
#https://leetcode-cn.com/problems/regular-expression-matching/

#普通字符直接匹配，并且-1迭代下一次
#遇到 a* .* 字符，可以遍历所有结果，比如当前不匹配 直接往下迭代是否有一个正确匹配
#当遇到剩下字符里  单独 . 数量 超过  INPUT数量必不能匹配， 如果相等  则查看 x* 是否为剩余的RULE
#本题应该用动态规划完成，只要所有可行的结果迭代有一次成功即可！！！

class Solution(object):
    def isMatch(self, input, rule):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print("+++++++ %s %s" % (input, rule))

        if rule == "" and input == "":
            return True

        if (rule == "" and input != "")  :
            return False

        if input == "" and rule != "":
            if len(rule) %2 == 1:
                return False
            for index in range(len(rule)):
                if index % 2 == 1 and rule[index] != '*':
                    return False
            return True

        if rule[0] == input[0] or rule[0] == '.':
            #如果匹配，则看下一个是否为*,如果=*  则递归 匹配和不匹配2种结果
            if len(rule) > 1:
                if rule[1] == '*':
                    if self.isMatch(input[1:], rule) or self.isMatch(input, rule[2:]):
                        return True
                    else:
                        return False
                else:
                    return self.isMatch(input[1:], rule[1:])
            else:
                return self.isMatch(input[1:], rule[1:])
        else:
            #如果不匹配，查看RULE下一个是否为*,进行迭代或直接不匹配
            if len(rule) > 1 and rule[1] == '*':
                return self.isMatch(input, rule[2:])
            else:
                return False



solution = Solution()

#expect T
#teststr = "aaabc"
#matchstr = "a.*bc"

#expect T
teststr = "aab"
matchstr = "c*a*b"


#expect T
#teststr = "aa"
#matchstr = "a*"

#expect T
#teststr = "aaa"
#matchstr = "a*a"

#expect T
#teststr = "mississippi"
#matchstr = "mis*is*ip*."

#expect F
#teststr = "aaba"
#matchstr = "ab*a*c*a"

#expect F
#teststr = "bbbba"
#matchstr = ".*a*a"


#expect T
#teststr = "ab"
#matchstr = ".*..c*"


#expect F
#teststr = "a"
#matchstr = ".*..a*"

#expect T
#teststr = "ab"
#matchstr = ".*..c*"

#expect T
#teststr = "aasdfasdfasdfasdfas"
#matchstr = "aasdf.*asdf.*asdf.*asdf.*s"

#expect F
#teststr = ""
#matchstr = "."

#expect F
#teststr = "aa"
#matchstr = "a"

#expect F
#teststr = "ab"
#matchstr = ".*c"

#expect F
#teststr = "b"
#matchstr = "aaa."

print(solution.isMatch(teststr, matchstr))