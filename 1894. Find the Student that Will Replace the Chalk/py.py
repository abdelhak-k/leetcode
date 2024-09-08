class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_ = 0
        
        for num in chalk:
            sum_+= num
            
        #now sum_ has the sum of all the numbers of chalk
        
        k%=sum_
        n=len(chalk)
        
        for i in range(n):
            if (chalk[i]>k):
                return i
            k-= chalk[i]