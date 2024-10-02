class CustomStack {
private:
    vector<int> STACK;
    int cur;
    
public:
    CustomStack(int maxSize) {
        this->STACK.resize(maxSize,-1);
        this->cur = 0;
    }
    
    void push(int x) {
        if(cur < STACK.size())    
            STACK[cur++]=x;
    }
    
    int pop() {
        if( cur > 0)
            return STACK[--cur];
        else
            return -1;
    }
    
    void increment(int k, int val) {
        for(int i=0;i<k && i<cur; ++i)
            STACK[i]+=val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */