class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        MaxNumL=0
        MaxNumR=0
        water=0
        
        i=0
        j=n-1
        
        while(i<j):
            MinBorder= min(MaxNumL,MaxNumR)
            MaxNumL= max(MaxNumL,height[i])
            MaxNumR= max(MaxNumR, height[j])
            

            if(height[i]<height[j]):
                diff= MinBorder-height[i]
                if(diff>0):
                    water+=diff
                i+=1
                
            else:
                diff= MinBorder-height[j]
                if(diff>0):
                    water+=diff
                j-=1
            
                        
        return water
        
        
        
   