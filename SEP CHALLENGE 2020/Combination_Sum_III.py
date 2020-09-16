from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        nn=list(range(1,10))
        arr=list(combinations(nn,k))
        for i in arr:
            if(sum(i)==n):
                ans.append(i)
        return(ans)
        
