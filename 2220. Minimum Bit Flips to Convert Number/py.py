class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        
        # ^ is the bitwise operator (xor)
        # it will xor of the binary rep of start and goal as an integer

        count=0
        # now we need to count the number of ones in binary rep of res
        # that's beacuse the ones means that the binary digits in a certain place where not the same
        while (res!=0):
            # is the right binary digit 1 or 0
            if res%2==1:
                count+=1
            
            # right shift operator(remove the right binary digit)        
            res = res >> 1   
        
        return count
            
