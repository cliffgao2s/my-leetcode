#https://leetcode-cn.com/problems/tuple-with-same-product/

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        nums.sort()

        dot = {}

        #22计算乘积,然后查看每一种乘积结果，计算C排列组合，每个组合对应8个可能结果
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                dotResult = nums[index1] * nums[index2]

                tmp = []
                tmp.append(index1)
                tmp.append(index2)

                if dot.get(dotResult) != None:
                    resultList = dot.get(dotResult)
                    resultList.append(tmp)
                    dot[dotResult] = resultList
                
                else:
                    resultList = []
                    resultList.append(tmp)
                    dot[dotResult] = resultList

        #print(dot)

        for item in dot:
            listResult = dot.get(item)

            total = 0
            for index in range(len(listResult) - 1):
                total += len(listResult) - index - 1
        
            result += total * 8

        return result


solution = Solution()

#16
#nums = [1,2,4,5,10]

#40
#nums = [2,3,4,6,8,12]

#48
#nums = [20,10,6,24,15,5,4,30]

#293728
#nums = [69,252,95,725,112,345,390,221,405,27,58,100,392,156,147,377,32,288,350,17,230,609,29,357,66,728,140,462,190,621,51,7,475,105,255,81,391,120,690,250,308,261,68,464,28,540,116,18,192,16,468,189,532,60,56,420,207,425,630,126,40,432,2,153,84,272,870,210,552,200,228,161,285,648,322,320,132,87,459,70,336,64,184,44,338,15,196,90,117,20,14,45,266,270,374,204,133,416,165,99,780,102,551,195,34,506,182,160,513,48,114,175,72,560,494,364,22,299,225,180,460,171,104,580,476,598,4,437,150,152,76,340,650,50,145,672,522,378,75,396,12,325,375,406,21,1,170,702,10,306,348,304,224,575,418,342,696,368,24,500,483,231,203,78,399,253,26,644,174,19,54,9,486,128,567,57,720,450,8,297,162,52,96,125,588,35,456,240,30,440,260,130,594,525,91,840,154,25,330,264]

print(solution.tupleSameProduct(nums))


'''
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        nums.sort()

        for index in range(len(nums)):
            if len(nums) - index < 4:
                break
            for index1 in range(len(nums) - 1, - 1, -1):
                for index2 in range(index + 1, index1):
                    for index3 in range(index1 - 1, -1, -1):
                        if index3 <= index2:
                            break
                        if nums[index] * nums[index1] == nums[index2] * nums[index3]:
                            result += 8

        
        return result


'''