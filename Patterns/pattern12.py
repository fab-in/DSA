for i in range(5):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,5-i):
        print(" ",end="")
    for l in range(i,0,-1):
        print(l,end="")
    print()


