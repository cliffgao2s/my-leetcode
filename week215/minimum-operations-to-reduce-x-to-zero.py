#https://leetcode-cn.com/contest/weekly-contest-215/problems/minimum-operations-to-reduce-x-to-zero/
#https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/


#思路1  最直观的思路，不断迭代 从 最左 和 最右 计算子迭代是否能成功，但时间复杂度随着LIST变大，呈现指数扩张
#思路2  求最大的1个内部子串，使得 SUM内部 = SUM ALL - X，因为如果不存在这样的内层子串，那根本不存在这样的计算方法使得X=0;且要计算得到这个中间剩余部分LENG最长的结果，这样取0的LENG就是最短的
#问题转换为  求  sum = total - x  的最长连续子串
class Solution(object):

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        if sum(nums) == x:
            return len(nums)
        
        if x > sum(nums):
            return -1

        midVal = sum(nums) - x
        totalVal = 0

        indexL = 0
        indexR = 0

        maxMidLen = -1

        #先从左往右计算，直到找到第一个相等或者大于MIDVAL的，然后继续移动L下标，直到L下标和R下标的中指大于MIDVAL,循环往复，直到R挪到LIST底部
        #如果大于MIDVAL，缩减窗口左侧，然后每次再扩大窗口右侧，依次往复
        while indexL < len(nums):
            if indexR < len(nums):
                totalVal += nums[indexR]
                indexR += 1
            
            while totalVal > midVal and indexL < len(nums):
                totalVal -= nums[indexL]
                indexL += 1
            
            if totalVal == midVal:
                if maxMidLen == -1:
                    maxMidLen = indexR - indexL
                else:
                    if indexR - indexL > maxMidLen:
                        maxMidLen = indexR - indexL
            
            if indexR == len(nums):
                indexL += 1

            
            shortLen = -1
            if maxMidLen > 0:
                shortLen = len(nums) - maxMidLen

        return shortLen


solution = Solution()

#2
#nums = [1,1,4,2,3]
#num = 5

#-1
#nums = [5,6,7,8,9]
#num = 4

#-1
#nums = [1241,8769,9151,3211,2314,8007,3713,5835,2176,8227,5251,9229,904,1899,5513,7878,8663,3804,2685,3501,1204,9742,2578,8849,1120,4687,5902,9929,6769,8171,5150,1343,9619,3973,3273,6427,47,8701,2741,7402,1412,2223,8152,805,6726,9128,2794,7137,6725,4279,7200,5582,9583,7443,6573,7221,1423,4859,2608,3772,7437,2581,975,3893,9172,3,3113,2978,9300,6029,4958,229,4630,653,1421,5512,5392,7287,8643,4495,2640,8047,7268,3878,6010,8070,7560,8931,76,6502,5952,4871,5986,4935,3015,8263,7497,8153,384,1136]
#num = 894887480

#-1
#nums = [5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639]
#num = 565610

#5
#nums = [3,2,20,1,1,3]
#num = 10

#5
#nums = [1,5,10,3,2,4]
#num = 15

#1
#nums = [1,1,3,2,5]
#num = 5

#6
nums = [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
num = 31841

print(solution.minOperations(nums, num))