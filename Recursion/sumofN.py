class Solution:
    def sumofN(self,N):
        if N==1:
            return 1
        return N+self.sumofN(N-1)
    
if __name__ == "__main__":
    N=5
    sol=Solution()
    print(sol.sumofN(N))