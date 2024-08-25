class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, val: int) -> None:
        try:
            minm= self.getMin()
        except IndexError: # in the case where the stack is empty
            minm=val
        
        if(val<minm):
            self.arr.append( (val,val) )
        else:
            self.arr.append( (val,minm) ) 
    
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()