for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    for l in range(5-i-1):
        print(" ",end="")
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    for l in range(5-i):
        print(" ",end="")
    print()