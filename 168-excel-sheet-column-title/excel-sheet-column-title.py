class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Convert a column number to Excel column title.
      
        Args:
            columnNumber: A positive integer representing the column number
          
        Returns:
            A string representing the corresponding Excel column title
          
        Example:
            1 -> "A", 26 -> "Z", 27 -> "AA", 28 -> "AB"
        """
        result = []
      
        # Convert number to base-26 representation with letters A-Z
        while columnNumber > 0:
            # Subtract 1 to handle 1-indexed to 0-indexed conversion
            # (Excel columns start at 1, but we need 0-25 for modulo operation)
            columnNumber -= 1
          
            # Get the current digit (0-25) and convert to corresponding letter
            current_digit = columnNumber % 26
            current_letter = chr(ord('A') + current_digit)
            result.append(current_letter)
          
            # Move to the next position (divide by 26)
            columnNumber //= 26
      
        # Reverse the result since we built it from least to most significant digit
        return ''.join(result[::-1])
