num=153
amstrong=num
check=0
count=len(str(num))
while num>0:
	digit=num%10
	check+=digit**count
	num=num//10
if check==amstrong:
	print("Amstrong Number")
	