class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        def  rob_linear(houses:List[int])->int:
            rob1, rob2=0,0
            for n in houses:
                current=max(rob1,rob2+n)
                rob2=rob1
                rob1=current
            return rob1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))