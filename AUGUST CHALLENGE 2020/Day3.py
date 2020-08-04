class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        #p = re.sub('[^0-9a-zA-Z]+', '*', s)
        p = filter(str.isalnum, s)
        p= "".join(p).lower()


        f=len(p)
        #print(f)
        #print(p)
        if(f>0):
            if(f%2==0):
                a=p[0:f//2]
                #print(a,"a")
                b=p[f//2:]
                b=b[::-1]
                #print(b,"b")
                if(a==b):
                    return(1)
                else:
                    return(0)
            
            else:
                a=p[0:(f//2)+1]
                #print(a,"a")
                b=p[f//2:]
                b=b[::-1]
                #print(b,"b")
                if(a==b):
                    return(1)
                else:
                    return(0)
        else:
            return(1)
            
                
            
        