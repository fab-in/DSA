for i in range(1,6):
    counter=1
    for j in range(1,i+1):
        if i%2==0:
            if counter==1:
                print(0,end="")
                counter=0
            elif counter==0:
                print(1,end="")
                counter=1
        else:
            if counter==1:
                print(1,end="")
                counter=0
            elif counter==0:
                print(0,end="")
                counter=1
    print()

