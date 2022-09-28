class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        N=str(n)
        for i in N:
            s+=int(i)
            p*=int(i)
        return p-s
    
        
    
            
        