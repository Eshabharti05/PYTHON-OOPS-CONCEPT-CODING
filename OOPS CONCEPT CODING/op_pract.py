'''
num=192
res=str(num*1)+str(num*2)+str(num*3)
print(res)
for i in range(1,10):
    if str(i) not in res:
        print("not a fascinating no")
        break
else:
    print("fascinating no")
'''
n=int(input())
count=0
while n>0:
    if n%2==1:
        count+=1
    n//=2
if count%2==0:
    print("evil number")
else:
    print("odious number")
        
