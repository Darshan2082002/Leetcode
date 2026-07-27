class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # right_sum is total_sum - left_sum - num
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1