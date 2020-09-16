class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        f=0
        str=list((str.split()))
        if((len(str)==len(pattern))):
            for i in range(1,len(pattern)):
                if(pattern[i]==pattern[i-1]):
                    if(str[i]==str[i-1]):
                        f=1
                    else:
                        f=0
                        break
                elif(pattern[i] in pattern[0:i]):
                    a=pattern.index(pattern[i],0,i)
                    if(str[i] in str[0:i]):
                        if(str[a]==str[i]):
                            f=1
                        else:
                            f=0
                            break
                    else:
                        f=0
                        break
                else:
                    if(pattern[i] not in pattern[0:i]):
                        if(str[i] not in str[0:i]):
                            f=1
                        else:
                            f=0
                            break
        else:
            f=0
        if(f==1 or len(pattern)==1):
            return(1)
        else:
            return(0)
                        
                
                
            
       
        
        