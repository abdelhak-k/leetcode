class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        
        isAllowed= {}
        
        
        for char in allowed:
            isAllowed[char]=True
        
        count=0
        for word in words:
            Allowed= True
            for char in word:
                if char not in isAllowed.keys():
                    Allowed=False
                    break
            if Allowed:
                count+=1
               
        return count     