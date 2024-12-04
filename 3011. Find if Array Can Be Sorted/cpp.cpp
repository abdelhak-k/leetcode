class Solution {
public:
    int count1s(int num){
        if (num<2)
            return num;
        return num%2 + count1s(num/2);
    }
    bool canSortArray(vector<int>& nums) {
        int n = nums.size();

        for(int j=0;j<n;++j){
            int i=0;
            while(i<n-1-j){
                if(nums[i]>nums[i+1]){
                    if (count1s(nums[i])!=count1s(nums[i+1]))
                        return false;
                    else
                        swap(nums[i],nums[i+1]);
                }
                
                ++i;
            }
        }
        return true;
    }
};