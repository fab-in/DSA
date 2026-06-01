class Solution:
    def printName(self,name,N):

        if N == 0:
            return
        print(name)
        self.printName(name,N-1)

if __name__ == "__main__":
    name="Fabin"
    count=5
    sol=Solution()
    sol.printName(name,count)