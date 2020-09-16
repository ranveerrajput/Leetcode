class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        aa=[]
        for i in range(len(a)-1):
            if(a[i]==a[i+1]):
                aa.append(a[i])
        return(aa)