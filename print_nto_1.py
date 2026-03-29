class Solution():
    def reverseCount(self, current):
        if current<1:
            return
        print(current, end=" ")
        self.reverseCount(current-1)


if __name__=="__main__":
    sol=Solution()
    n=10

    sol.reverseCount(n)
    print()