class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        mp={}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        result=[]
        for num,count in mp.items():
            if count ==1:
                result.append(num)
        return result
