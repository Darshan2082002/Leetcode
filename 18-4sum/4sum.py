from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Don't forget to sort the array first!
        n = len(nums)
        array = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # left and right MUST be inside the 'j' loop
                left, right = j + 1, n - 1
                
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if summ == target:
                        # Append the actual 4 numbers, not the built-in sum function
                        array.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        # Skip duplicates for inner pointers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        right -= 1

        return array