class Solution:
    def printNum(self,start,N):

        if start >N:
            return
        print(start)
        self.printNum(start+1,N)

if __name__ == "__main__":
    N=5
    sol=Solution()
    sol.printNum(1,N)