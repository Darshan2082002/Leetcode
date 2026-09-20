class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:].zfill(32)
        return int(a[::-1],2)