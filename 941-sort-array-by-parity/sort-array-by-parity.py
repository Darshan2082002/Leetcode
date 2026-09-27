class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        result = []
        result2 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                result.append(nums[i])
            else:
                result2.append(nums[i])
                
        combinee = result + result2
        return combinee