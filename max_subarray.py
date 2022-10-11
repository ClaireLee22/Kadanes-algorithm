class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localMax = nums[0]
        globalMax = nums[0]
        print("index:", 0,  "local max:", localMax, "global max:", globalMax)
        
        for i in range(1, len(nums)):
            currentNum = nums[i]
            localMax = max(localMax + currentNum, currentNum)
            globalMax = max(globalMax, localMax)
            print("index:", i, "local max:", localMax, "global max:", globalMax)
        
        return globalMax

if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print("the maximum subarray sum:", solution.maxSubArray(array))


"""
output:
('index:', 0, 'local max:', -2, 'global max:', -2)
('index:', 1, 'local max:', 1, 'global max:', 1)
('index:', 2, 'local max:', -2, 'global max:', 1)
('index:', 3, 'local max:', 4, 'global max:', 4)
('index:', 4, 'local max:', 3, 'global max:', 4)
('index:', 5, 'local max:', 5, 'global max:', 5)
('index:', 6, 'local max:', 6, 'global max:', 6)
('index:', 7, 'local max:', 1, 'global max:', 6)
('index:', 8, 'local max:', 5, 'global max:', 6)
('the maximum subarray sum:', 6)
"""