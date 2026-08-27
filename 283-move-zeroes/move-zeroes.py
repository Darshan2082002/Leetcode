class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        arr=[]
        count=0
        for num in nums:
            if num!=0:
                arr.append(num)
            else:
                count+=1
        nums[:]=arr+[0]*count
