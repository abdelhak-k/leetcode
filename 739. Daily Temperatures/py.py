class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n=len(temperatures)
        res= [0]*n
        stack= []
        
        for i in reversed(range(n)):
            while len(stack)>0 and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if len(stack)>0 and temperatures[i] < stack[-1][0]:
                res[i]= stack[-1][1]- i  
                
            stack.append( [temperatures[i],i] )
            
        return res