class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        size= pow(2,n)-1
        s=[0] * size
        cur=1
        for i in range(n-1):
            s[cur]=1
            cur+=1
            tmp_cur= cur

            if cur>=k:
                return str(s[k-1])

            for j in reversed(range(tmp_cur-1)):
                if s[j]==1:
                    s[cur]=0
                else:
                    s[cur]=1
                cur+=1
            

        return str(s[k-1])
        
        