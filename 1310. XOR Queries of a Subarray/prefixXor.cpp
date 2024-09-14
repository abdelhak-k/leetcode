class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n= arr.size();
        int s= queries.size();
        vector<int> prefixXor(n+1);
        vector<int> answer(s);
        
        // things to make the solution more clear:
        // 0 Xor x = x
        // a Xor a = 0
        // -> a Xor a Xor b = b
        // prefixXor[i+1]= 0 Xor X0 Xor X1 Xor X2 Xor ... Xi 
        // XOR(i,j)= Xi ^..Xj= X0 ^ X1..Xi-1 ^ X0 ^ X1 ^..Xi-1 ^..Xj = prefixXor[i] ^ prefixXor[j+1]
        
        prefixXor[0]=0;
        
        for (int i=0;i<n;++i)
            prefixXor[i+1]= prefixXor[i]^arr[i];
        
        for(int i=0;i<s;++i)
            answer[i] = prefixXor[queries[i][0]] ^ prefixXor[queries[i][1]+1];
        
        return answer;
    }
};