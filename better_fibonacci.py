def main():
    n=5
    if n==0:
        print(0)
    else:
        pre_last=0
        last=1
        print(f"{pre_last} {last} ", end="")
        for i in range(2, n+1):
            current=last+pre_last
            pre_last=last
            last=current
            print(current, end=" ")

if __name__=="__main__":
    main()