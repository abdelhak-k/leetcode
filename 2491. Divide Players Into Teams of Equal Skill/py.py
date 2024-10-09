class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        i = 0
        j = n-1
        
        lvl= skill[i]+skill[j]
        res=0
        
        while(i<j):
            if skill[i]+skill[j]==lvl:
                res+=skill[i]*skill[j]
            else:
                return -1
        
            i+=1
            j-=1
        
        return res