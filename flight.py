n=int(input())
p=int(input())
q=int(input())
r=int(input())
a=[]
c=1
for i in range(1,n):
    a.append(p*i)
for i in range(1,n):
    a.append(q*i)
for i in range(1,n):
    a.append(r*i)
a.sort()
print(a)

for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
        
print(c)