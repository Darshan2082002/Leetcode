class Solution:
    def addDigits(self, num: int) -> int:
        digits=list(map(int,str(num)))
        n=len(digits)
        total=0
        if n ==1:
            return num 
        for digit in digits:
            total+=digit
        return self.addDigits(total)