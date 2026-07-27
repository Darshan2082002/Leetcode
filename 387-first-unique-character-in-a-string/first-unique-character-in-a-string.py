from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count frequency of each character
        count = Counter(s)
        
        # Step 2: Find the first character with a count of 1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
                
        return -1