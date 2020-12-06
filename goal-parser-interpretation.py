#https://leetcode-cn.com/contest/weekly-contest-218/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        resultStr:str = ""
        index = 0

        while index < len(command):
            if command[index] == '(':
                if command[index+1] == ')':
                    resultStr += "o"
                    index += 2
                    continue
                elif command[index + 1] == 'a':
                    resultStr += "al"
                    index += 4
                    continue
            elif command[index] == 'G':
                resultStr += 'G'
                index += 1
                continue

            index += 1
        
        return resultStr




solution = Solution()

command = "(al)G(al)()()G"

print(solution.interpret(command))