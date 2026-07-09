class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        dp=[0]*l
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,l):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]