#https://leetcode-cn.com/contest/weekly-contest-215/problems/determine-if-two-strings-are-close/
#几个条件才能相等   1 长度相同  2 含有字符种类相同，且子字符种类相同 3 2个字符串必须含有相同多的字符类型 比如A出现在WORD1， 那WORD2 也必须有A

class Solution(object):

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False

        dictA = {}
        dictB = {}

        for item in word1:
            if dictA.get(item) == None:
                dictA[item] = 1
            else:
                dictA[item] = dictA.get(item) + 1

        for item in word2:
            if dictB.get(item) == None:
                dictB[item] = 1
            else:
                dictB[item] = dictB.get(item) + 1

        ListA = []
        ListB = []

        for item in dictA:
            ListA.append(dictA.get(item))
        for item in dictB:
            ListB.append(dictB.get(item))

        ListA.sort()
        ListB.sort()

        if len(ListA) != len(ListB):
            return False

        for index in range(len(ListA)):
            if ListA[index] != ListB[index]:
                return False

        #判断2个字符串相同字符种类数量
        for item in dictA:
            if dictB.get(item) == None:
                return False

        return True



solution = Solution()

#T
#word1= "cabbba"
#word2 = "abbccc"


#F
#word1= "cabbba"
#word2 = "aabbss"

#F
word1= "abbzzca"
word2 = "babzzcz"

print(solution.closeStrings(word1, word2))