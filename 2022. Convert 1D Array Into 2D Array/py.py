class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        #m: number of rows
        #n: number of cols
        length= len(original)
        if (length != m*n):
            return []
        
        res= []
        
        for i in range(m):
            arr= []
            for j in range(i*n,n*(1+i)):
                arr.append(original[j])
            res.append(arr)
        
        return res
