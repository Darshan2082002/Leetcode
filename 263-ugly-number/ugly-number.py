class Solution:
    def isUgly(self, n: int) -> bool:
        a=[2,3,5]
        if n<1:
            return False 
        if n==1:
            return True 
        for prime in a:
            if n%prime==0:
                return self.isUgly(n//prime)
        return False 
        
