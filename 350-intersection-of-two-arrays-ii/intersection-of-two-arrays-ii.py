
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mp={}
        for j in nums1:
            mp[j]=mp.get(j,0)+1
        result=[]
        for num in nums2:
            if mp.get(num,0)>0:
                result.append(num)
                mp[num]-=1
        return result