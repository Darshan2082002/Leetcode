class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=1:
            return 0
        nums.sort()
        max=0
        for i in range(n-1):
            c=nums[i+1]-nums[i]
            if max<=c:
                max=c
        return max