class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        cc=[]
        c=0
        SS=S[::-1]
        l=0
        r=0
        pre=0
        for i in range(len(S)):
            c=c+1
            l=i
            for j in range(len(S)-1,-1,-1):
                if(S[i]==S[j]):
                    r=j
                    if(r>pre):
                        pre=r
                    if(l==pre):
                        cc.append(c)
                        #print(cc)
                        c=0
                    break
        return(cc)
                    
                        
            
                