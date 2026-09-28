class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        res=[]
       
        def recurision(index,nums,res):
            if index==len(nums):
                res.append(nums[:])
                return
            for i in range(index,len(nums)):
                nums[index],nums[i]=nums[i],nums[index]
                recurision(index+1,nums,res)
                nums[index],nums[i]=nums[i],nums[index]
        recurision(0,nums,res)
        return res


