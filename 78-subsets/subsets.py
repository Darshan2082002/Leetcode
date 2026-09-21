class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result,sol=[],[]
        n=len(nums)
        def backtracking(i):
            if i==n:
                result.append(sol[:])
                return 
            backtracking(i+1)

            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)
        return result 
