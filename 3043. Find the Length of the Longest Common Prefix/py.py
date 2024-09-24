class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        # O(n+m)
        arr1str = [str(i) for i in arr1]
        arr2str = [str(i) for i in arr2]
        
        # we use a set since searching on a set takes O(1) on average
        prefix = set()
        
        # O(8*n) -> O(n)
        for s1 in arr1str:
            n = len(s1)
            for i in range(1, n+1):
                prefix.add(s1[0:i])
        
        res= 0
        # O(8*m) -> O(m)
        for s2 in arr2str:
            n= len(s2)
            for i in range(1,n+1):
                if s2[0:i] in prefix: # O(1) on average
                    res= max(res,i)
                    
        return res

                