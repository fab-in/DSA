class Solution:
    def factorial(self,N):
        if N==1:
            return 1
        return N*self.factorial(N-1)

if __name__ == "__main__":
    N=5
    sol=Solution()
    print(sol.factorial(N))