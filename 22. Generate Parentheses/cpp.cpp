class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        generate(0,0,res,n);
        return res;
    }
    void generate(int leftP,int rightP ,vector<string>& res,const int n,string cur=""){
        
        if(leftP==n && rightP==n){
            res.push_back(cur);
            return;
        }
        
        if(leftP<n)
            generate(leftP+1,rightP,res,n,cur+"(");
        
        if(leftP>rightP)
            generate(leftP,rightP+1,res,n,cur+")");
        
    }
};