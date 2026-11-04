class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        from sortedcontainers import SortedList
        import math
        
        n = len(nums)
        # Array to store the cost of making each subarray of size x equal
        costs = [0] * (n - x + 1)
        
        left_half = SortedList()
        right_half = SortedList()
        left_sum = 0
        right_sum = 0
        
        for i, current_num in enumerate(nums):
            # Insert into the left half
            left_half.add(current_num)
            left_sum += current_num
            
            # Move largest from left to right to maintain sorted order
            largest_left = left_half.pop()
            left_sum -= largest_left
            right_half.add(largest_left)
            right_sum += largest_left
            
            # Maintain balance: left_half size must be equal to or one greater than right_half
            if len(right_half) > len(left_half):
                smallest_right = right_half.pop(0)
                right_sum -= smallest_right
                left_half.add(smallest_right)
                left_sum += smallest_right
                
            # If the current window has reached size x, calculate the cost
            if i >= x - 1:
                # Median is the largest element in the left half
                median = left_half[-1]
                
                # Cost calculation based on distance to the median
                cost = (median * len(left_half) - left_sum) + (right_sum - median * len(right_half))
                
                window_start = i - x + 1
                costs[window_start] = cost
                
                # Remove the element falling out of the sliding window
                element_to_remove = nums[window_start]
                if element_to_remove in right_half:
                    right_half.remove(element_to_remove)
                    right_sum -= element_to_remove
                else:
                    left_half.remove(element_to_remove)
                    left_sum -= element_to_remove

        # DP Step: Find min cost to pick k non-overlapping subarrays
        # dp[i][j] = min cost to pick j subarrays starting from index i or later
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(n - x, -1, -1):
            for j in range(1, k + 1):
                # Option 1: Skip index i entirely
                skip = dp[i + 1][j]
                
                # Option 2: Pick subarray starting at i, add the cost of picking j-1 subarrays from i+x onward
                pick = costs[i] + dp[i + x][j - 1]
                
                dp[i][j] = min(skip, pick)
                
        return dp[0][k]