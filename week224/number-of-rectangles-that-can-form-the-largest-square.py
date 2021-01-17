#https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        nums = {}
        result = 0
        maxRec = 0

        for item in rectangles:
            len1 = item[0]
            len2 = item[1]

            rec = min(len1, len2)

            if nums.get(rec) != None:
                nums[rec] = nums.get(rec) + 1
            else:
                nums[rec] = 1
        
        for item in nums:
            if item > maxRec:
                result = nums.get(item)
                maxRec = item
        
        return result



solution = Solution()
#3
#rectangles = [[5,8],[3,9],[5,12],[16,5]]

#3
#rectangles = [[2,3],[3,7],[4,3],[3,7]]

#1
rectangles = [[5,8],[3,9],[3,12]]

print(solution.countGoodRectangles(rectangles))