class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       mp={}
       n=len(nums)
       for i in range(n):
        for j in range(i+1,n):
            c=nums[i]+nums[j]
            mp[c]=[i,j]
        if target in mp:
            return mp[target]
    
        