class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        expected_sum=n*(n+1)/2
        unique_sum=sum(set(nums))
        duplicat_sum=sum(nums)-unique_sum
        missing=int(expected_sum-unique_sum)
        return [duplicat_sum,missing]

        