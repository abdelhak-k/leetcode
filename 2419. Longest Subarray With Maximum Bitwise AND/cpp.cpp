class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        // distinct numbers -> always : 1
        // number AND x <= number in the case of: x <= number 
        // so we search for the max number in the array and the number of its occurnces
        // x AND x = x
        // subarray is a *** contiguous *** sequence 
        
        int max_num=0;
        int occ=0;
        int max_occ=0;
        
        for(int num:nums){
            if (num==max_num)
                ++occ;
            
            else if(num>max_num){
                max_num=num;
                occ=1;
                max_occ=0;
            }
            else if(num<max_num){
                max_occ=max(max_occ,occ);
                occ=0;
            }   
        }
        // in the case that the last part of the array has only the max number
        if (max_occ==0 )
            max_occ=occ;
        
        return max_occ;
    }
};