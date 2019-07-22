# h03.py
a=int(input())
b=list(map(int,input().split()))
a1=0
c=[]
for i in range(0,a):
	if(b[i]==i):
		temp=b[i]
		a1=1
		c.append(temp)
		c=sorted(c)
print(*c)
if(a1==0):
	print(-1)
