class Solution {
public:
    bool isPerfectSquare(int num) {
    int l=0;
    int r=num;
    long long mid;
        while(l<=r){
            mid=(l+r)/2;
            if(mid*mid==num) return 1;
            else if(mid*mid<num) l=mid+1;
            else r=mid-1;
        }
        return 0;
        
 
    }
};