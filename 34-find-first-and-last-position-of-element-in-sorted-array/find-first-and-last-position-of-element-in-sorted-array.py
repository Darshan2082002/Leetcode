class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # If we want the first occurrence, keep searching left
                        right = mid - 1
                    else:
                        # If we want the last occurrence, keep searching right
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound
        
        first = findBound(True)
        # If the target isn't found at all, return early
        if first == -1:
            return [-1, -1]
            
        last = findBound(False)
        return [first, last]