class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        
        int n = arr.size();
        vector<int> rank(n);
        
        unordered_map<int,vector<int>> index;
        
        for(int i=0;i<n;++i)
            index[arr[i]].push_back(i);
    
        sort(arr.begin(),arr.end());
        
        int i=0;
        int j=1;
    
        while(i<n){
            vector<int> subarr = index[arr[i]];            
            for(auto I: subarr){
                rank[I]=j;
                ++i;
            }
            ++j;
        }
        
        return rank;
        
        
    }
};