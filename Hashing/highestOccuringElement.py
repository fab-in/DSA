arr=[10,5,10,15,10,5]

map={}
for i in arr:
    if i not in map:
        map[i]=1
    else:
        map[i]+=1

for key,value in map.items():
    if value==max(map.values()):
        print(key)