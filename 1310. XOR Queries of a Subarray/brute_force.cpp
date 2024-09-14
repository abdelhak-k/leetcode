class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n= queries.size();
        vector<int> answer(n);
        
        for(int i=0;i<n;++i){
            int res=arr[queries[i][0]];
            for(int j=queries[i][0]+1;j<=queries[i][1];++j){
                res^=arr[j];
            }
            answer[i]=res;
        }
        return answer;
    }
};