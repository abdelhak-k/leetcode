class Solution:
    def findScore(self, nums: List[int]) -> int:

        n= len(nums)
        pair_nums = [0]* n
        
        
        for i in range(n):
            pair_nums[i] = (nums[i],i)
        
        pair_nums.sort()
        
        score=0
        
        for i in range(n):
            index= pair_nums[i][1]
            val= pair_nums[i][0]
            if nums[index] > 0:
                score += val
                nums[index] *= -1
                
                if index+1<n and nums[index+1]>0 :
                    nums[index+1] *= -1
                if index-1>=0 and nums[index-1]>0 :
                    nums[index-1] *= -1
            
        return score