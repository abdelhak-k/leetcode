class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        n= len(heights)
        
        # a stack to keep track of the heights that can be extanded
        stack = []
        
        max_area=0
        
        # we add the first bar to the stack of heights that can be extanded
        stack.append( [0,heights[0]] )        
        
        for i in range(1,n):
            
            # case of: the next bar is smaller than the curr one -> can't be extanded
            
            if heights[i] < stack[-1][1]:
                last_bar_index= stack[-1][0]
                
                while len(stack)!=0 and heights[i] < stack[-1][1]:
                    # we store the index of the last bar
                    last_bar_index= stack[-1][0] 
                    
                    # then we calc the area extanded from that bar and store it iff it's greater 
                    max_area= max(max_area, stack[-1][1]*(i-last_bar_index))
                    
                    # then we pop that bar since we can't extand it forward anymore
                    stack.pop()
                    
        # now we store the curr bar with the index of tha last one since it can be extanded backward
                stack.append( [last_bar_index, heights[i]] )
            
            else: # heights[i] >= stack[-1][1]
                # we push it to the stack to keep track of it
                stack.append( [i, heights[i]] )
        
        #they made it to the end, we calc the extanded area genrated from n-index
        while len(stack)>0:
            max_area=max(max_area, (n-stack[-1][0])*stack[-1][1] )
            stack.pop()
            
        return max_area
        