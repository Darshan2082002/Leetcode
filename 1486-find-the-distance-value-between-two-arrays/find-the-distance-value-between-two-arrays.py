class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Step 1: Sort the second array so we can perform binary search
        arr2.sort()
        count = 0
        
        for x in arr1:
            left = 0
            right = len(arr2) - 1
            is_valid = True
            
            # Step 2: Basic binary search loop
            while left <= right:
                mid = (left + right) // 2
                
                # If we find a number within distance d, this x is invalid
                if abs(arr2[mid] - x) <= d:
                    is_valid = False
                    break
                
                # If the middle element is strictly smaller than x (and outside distance d),
                # all elements to the left are even smaller. We must search the right half.
                elif arr2[mid] < x:
                    left = mid + 1
                    
                # If the middle element is strictly larger than x (and outside distance d),
                # all elements to the right are even larger. We must search the left half.
                else:
                    right = mid - 1
                    
            # If the binary search finishes without finding any close numbers, x is valid
            if is_valid:
                count += 1
                
        return count