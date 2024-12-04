class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int n= str1.length();
        int m= str2.length();
        
        if(n<m)
            return false;
        
        int i=0;
        int j=n-1;
        
        int x=0;
        int y=m-1;
        
        while(i<=j && x<=y){
            if(str1[i]==str2[x] || int( (str1[i]+1)% 26) == int(str2[x])%26 ) ++x;
            
            if(str1[j]==str2[y] || int( (str1[j]+1)% 26) == int(str2[y])%26 ) --y;
            
            ++i;
            --j;
        }
        
        if(x>y)
            return true;
        
        return false;
        
        
    }
};