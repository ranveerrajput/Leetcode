class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=list(version1.split("."))
        b=list(version2.split("."))
        m=min(len(a),len(b))
        n=max(len(a),len(b))
        if(len(a)>=len(b)):
            for i in range(m):
                if(int(a[i])>int(b[i])):
                    return(1)
                elif(int(a[i])<int(b[i])):
                    return(-1)
                elif(int(a[i])==int(b[i])):
                    f=1
            if(f==1):
                ff=0
                if(len(a)>len(b)):
                    for k in range(m,n):
                        if(int(a[k])>0):
                            return(1)
                        else:
                            ff=1
                    if(f==1):
                        return(0)
                else:
                    return(0)
        else:
            for i in range(m):
                if(int(b[i])>int(a[i])):
                    return(-1)
                elif(int(b[i])<int(a[i])):
                    return(1)
                elif(int(b[i])==int(a[i])):
                    f=1
            if(f==1):
                ff=0
                if(len(b)>len(a)):
                    for k in range(m,n):
                        if(int(b[k])>0):
                            return(-1) 
                        else:
                            ff=1
                    if(f==1):
                        return(0)         
                else:
                    return(0)
       
                
                         
                         
