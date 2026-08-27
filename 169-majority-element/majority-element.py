class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        mp={}
        thresold=n//2
        for num in nums:
            mp[num]=mp.get(num,0)+1
            if mp[num]>thresold:
                return num
        

