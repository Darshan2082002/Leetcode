class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1=="0" or num2=="0"):
            return "0"
        m,n=len(num1),len(num2)
        result=[0]*(m+n)
        for i in range(m):
            a=int(num1[i])
            for j in range(n):
                b=int(num2[j])
                result[i+j+1]+=a*b
        for i in range(m+n-1,0,-1):
             result[i - 1] += result[i] // 10
             result[i] %= 10
        i=0 if result[0] else 1
        return "".join(str(x) for x in result[i:])

               