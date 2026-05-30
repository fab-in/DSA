num1=15
num2=25
i=1
while i<num1 and i<num2:
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print(gcd)