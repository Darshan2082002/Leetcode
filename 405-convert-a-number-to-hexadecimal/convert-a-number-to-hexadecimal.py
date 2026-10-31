class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_char = "0123456789abcdef"
        result = []
        num = num & 0xFFFFFFFF
        
        while num > 0:
            remainder = num % 16
            result.append(hex_char[remainder])
            num //= 16
            
        return "".join(result[::-1])