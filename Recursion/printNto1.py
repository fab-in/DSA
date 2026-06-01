class Solution:
    def printNum(self,N):

        if N==0:
            return
        print(N)
        self.printNum(N-1)

if __name__ == "__main__":
    N=5
    sol=Solution()
    sol.printNum(N)