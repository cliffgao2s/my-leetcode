#https://leetcode-cn.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        index = 0
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        while True:
            header = ''
            for item in strs:
                if index >= len(item):
                    return  result
                elif header == '':
                    header = item[index]
                else:
                    if header != item[index]:
                        return result
            result += header
            index += 1

        return result


solution = Solution()

#'fl'
#strs = ["flower","flow","flight"]

#''
#strs = ["dog","racecar","car"]

#''
#strs = []

#""
strs = [""]

print(solution.longestCommonPrefix(strs))