for i in range(6):
    for j in range(6-i):
        print(" ",end="")
    for k in range((i*2)+1):
        print("*",end="")
    for l in range(6-i):
        print(" ",end="")
    print()
for i in range(5,-1,-1):
    for j in range(6-i):
        print(" ",end="")
    for k in range((i*2)+1):
        print("*",end="")
    for l in range(6-i):
        print(" ",end="")
    print()