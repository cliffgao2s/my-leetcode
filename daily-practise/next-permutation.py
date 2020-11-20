#https://leetcode-cn.com/problems/next-permutation/

# 必须 原地 修改，只允许使用额外常数空间

#问题转换为  从-1 开始 一个窗口内是否有 次大一级解，如果没有则扩大窗口范围,但是不符合 空间复杂度开销

#同样还是区间，找到区间内刚好大于 -N-1索引的数字并替换；然后再对 -N - TAIL的数据进行升序排列

#1 先从队尾开始，不断向左移动，找到过去N-1个里的最大值，如果最大值>当前INDEX，则记录下位置
#2 从找到INDEX位置开始回溯，找到> index的那个最小值，并且互换位置(因为前面的最大值替换过来不一定是最优解，比如 1， 9， 8，7   应该是7和1替换)
#3 INDEX-1的 窗口内进行升序排序，这样找到最小的次值
#4 如果原始队列没任何转换，则全部进行升序

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #从最后开始查找，找到即返回，如果-1没有，则从-2开始

        maxNumIndex = -1
        for index in range(1, len(nums) + 1):
            if nums[maxNumIndex] > nums[-index]:
                #找到可以替换的位置，再比较 之前窗口内是否有最小的大于 nums[index]的数据进行互换
                minGap = nums[maxNumIndex] - nums[-index]
                minGapIndex = maxNumIndex

                for indexInside in range(1, index):
                    if nums[-indexInside] - nums[-index] > 0 and nums[-indexInside] - nums[-index] < minGap:
                        minGap = nums[-indexInside] - nums[-index]
                        minGapIndex = -indexInside

                temp = nums[minGapIndex]
                nums[minGapIndex] = nums[-index]
                nums[-index] = temp

                #再对子序列进行升序排列，冒泡
                for index2 in range(len(nums) - index + 1, len(nums) - 1):
                    for index3 in range(index2 + 1, len(nums)):
                        if nums[index2] > nums[index3]:
                            temp1 = nums[index2]
                            nums[index2] = nums[index3]
                            nums[index3] = temp1

                return
            else:
                if nums[maxNumIndex] < nums[-index]:
                    maxNumIndex = -index
        
        #没有翻转，则反序
        for index in range((int)(len(nums)/2)):
            temp = nums[-index-1]
            nums[-index-1] = nums[index]
            nums[index] = temp
        
        return


solution = Solution()

#[1,3,2]
nums = [1,2,3]

#[1,2,3,4,5]
#nums = [5,4,3,2,1]

#[2,1,3]
#nums = [1,3,2]

#[4,2,0,3,0,2,2]
#nums = [4,2,0,2,3,2,0]

solution.nextPermutation(nums)
print(nums)