class Solution {
public:
    #define ll long long
    int searchInsert(vector<int>& nums, int target) {
        ll l=0;
        ll r=nums.size()-1;
        ll mid;
        while(l<=r){
            mid=l+(r-l)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]>target) r=mid-1;
            else if(nums[mid]<target) l=mid+1;
        }
        if(nums[mid]<target) return mid+1;
        else return mid;
        
    }
};