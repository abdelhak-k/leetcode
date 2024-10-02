class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:        
        nums= []
        
        for num in arr:
            r= num % k
            if r != 0 :
                nums.append(r)
            
        n = len(nums) 
        
        if n % 2 !=0:
            return False
        else:
            nums.sort()
        
        i = 0
        j = n-1
        
        while(i<j):
            if nums[i]+nums[j]!=k:
                return False
            i+=1
            j-=1
            
        return True
            