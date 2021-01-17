#https://leetcode-cn.com/contest/weekly-contest-216/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        total1 = ''
        total2 = ''

        for item in word1:
            total1 += item
        for item in word2:
            total2 += item
        
        if total1 != total2:
            return False

        return True



solution = Solution()

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]

print(solution.arrayStringsAreEqual(word1, word2))

