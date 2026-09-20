class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        results=0
        for i in nums:
            results^=i
        return results