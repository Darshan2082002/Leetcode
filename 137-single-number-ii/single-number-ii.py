class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        one=0
        two=0
        for i in nums:
            one=(one^i)&~two
            two=(two^i)&~one
        return one 
          