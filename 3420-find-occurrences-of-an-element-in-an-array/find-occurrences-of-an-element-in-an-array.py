class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        mp=[]
        result=[]
        n=len(nums)
        m=len(queries)
        if n==0 or m==0:
            return -1
        for i, num in enumerate(nums):
            if num==x:
                mp.append(i)
        for q in queries:
            if q<=len(mp):
                result.append(mp[q-1])
            else:
                result.append(-1)
        return result
