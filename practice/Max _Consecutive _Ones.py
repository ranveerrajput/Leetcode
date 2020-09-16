class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        c=0
        a=[]
        while(i<len(nums)):
            if(nums[i]==1):
                c=c+1
            else:
                a.append(c)
                c=0
            i=i+1
        if(c!=0):
            a.append(c)
        if(len(a)>0):
            return(max(a))
        else:
            return(0)
        
            
        