class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        f=0
        for i in range(1,(len(s)//2)+1):
            a=s[:i]
            p=(len(s)-len(a))
            p=p//len(a)
            #print(a+(a*p))
            if s==(a+(a*p)):
                f=1
                break
            else:
                f=0
        if f==1:
            return 1
        else:
            return 0
        