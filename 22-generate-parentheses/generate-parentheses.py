class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       dp=[[] for _ in range(n+1)]
       dp[0]=[""]
       for i in range(1,n+1):
        for j in range(i):
            inside_list=dp[j]
            outside_list=dp[i-1-j]
            for inside in inside_list:
                for outside in outside_list:
                    dp[i].append("("+ inside +")" +outside)
       return dp[n]