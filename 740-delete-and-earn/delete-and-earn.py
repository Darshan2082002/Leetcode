class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums=sorted(list(set(nums)))
        e1,e2=0,0
        for i in range(len(nums)):
            
            current_val=nums[i]*count[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                temp=e2
                e2=max(current_val+e1,e2)
                e1=temp
            else:
                temp=e2
                e2=current_val+e2
                e1=temp
        return e2