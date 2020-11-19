#https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    reflect_table = dict()
    reflect_table["2"] = ['a','b','c']
    reflect_table["3"] = ['d', 'e', 'f']
    reflect_table["4"] = ['g', 'h', 'i']
    reflect_table["5"] = ['j', 'k', 'l']
    reflect_table["6"] = ['m', 'n', 'o']
    reflect_table["7"] = ['p', 'q', 'r', 's']
    reflect_table["8"] = ['t', 'u', 'v']
    reflect_table["9"] = ['w', 'x', 'y', 'z']

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        if digits == '':
            return result

        for item1 in digits:
            tempList = []
            for item2 in self.reflect_table.get(item1):
                if len(result) > 0:
                    for item3 in result:
                        tempList.append(item3 + item2)
                else:
                    tempList.append(item2)

            result.clear()
            result = tempList


        return result



solution = Solution()

#["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
input = "23"




print(solution.letterCombinations(input))