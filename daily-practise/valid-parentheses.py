#https://leetcode-cn.com/problems/valid-parentheses/
#思路 迭代求子问题，计算每一个配对的子问题，任何1个子问题OK 则返回OK
class Solution(object):
    pairs = []
    pairs.append("[]")
    pairs.append("{}")
    pairs.append("()")

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print("+++++++ %s" % (s))

        if len(s) == 0:
            return True

        if len(s)%2 != 0:
            return False

        for index in range(len(s)-1):
            if s[0] + s[-index-1] in self.pairs:
                if self.isValid(s[1:len(s)-index-1]) and self.isValid(s[len(s)-index :] ):
                    return True
        return False




solution = Solution()

#true
input = "()[]{}"

#false
#input = "([)]"

#input = "[{()}]"

#true
#input = "{}[([])]{}"

print(solution.isValid(input))