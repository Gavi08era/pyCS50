class solution:
    def pattern3(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()


    def pattern4(self, N):
        #we have to fix i here
        for i in range(1, N+1):
            for j in range(1,i+1):
                print(i, end=" ")
            print()

    def pattern5(self, N):
        #Reverse triangle
        for i in range(N):
            print("* "*N)
            N=N-1

    def pattern25(self, N):
        for i in range(N):
            for j in range(N,i,-1):
                print("*", end=" ")
            print()

    def pattern6(self, N):
        for i in range(N):
            for j in range(N,i,-1):
                print(N-j+1, end=" ")
            print()    
    def pattern7(self, N):
        for i in range(N):
            for j in range(N-1-i):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end="")
            for j in range(N-1-i):
                print(" ", end="")
            print()   

    def pattern8(self, N):
        for i in range(N):
            for j in range(i):
                print(" ", end="")
            for j in range(2*N-2*i-1):
                print("*", end="")
            for j in range(i):
                print(" ", end="")
            print()        

    def pattern9(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print(" ", end="")            
            for j in range(2*i+1):
                print("*", end='')
            for j in range(N-i-1):
                print(" ", end="")
            print()
        for i in range(N):
            for j in range(i):
                print(" ", end="")
            for j in range(2*N-2*i-1):
                print("*", end="")
            for j in range(i):
                print(" ", end="")
            print()


if __name__=="__main__":
    sol=solution()
    N=5
    sol.pattern6(N)
