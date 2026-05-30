num=1221
palindorme=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==palindorme:
    print("Palindrome")