class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        
        long long sum=0;
        priority_queue<long long> pq;
        int n= gifts.size();
        
        for(auto gift: gifts)
            pq.push(gift);
        
        int i=0;
        
        while(i<k){
            
            pq.push( sqrt( pq.top() ) );
            pq.pop();
            ++i;
        }
        
        while(!pq.empty()){
            sum+= pq.top();
            pq.pop();
        }
        
        
        return sum;
        
        
    }
};