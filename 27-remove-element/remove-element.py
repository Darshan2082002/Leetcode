class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left=0
        right=n-1
       
        while left<=right:
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1
        return left