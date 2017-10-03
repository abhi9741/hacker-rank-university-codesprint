n=int(input())
m=int(input()) #no. of volcanoes

l=[]

for m in range(0,m):
    x, y, w = raw_input().strip().split(' ')
    x, y, w = [int(x), int(y), int(w)]
    l.append([x,y,w])
    # print l

locmat=[]
for i in range(0,n):
    rowmat=[]
    for i in range(0,n):
        rowmat.append(0)
    locmat.append(rowmat)

k=0
m =len(l)
while k<m:

    x=l[k][0]

    y=l[k][1]

    w=l[k][2]



    for i in range(0,n):
      for j in range (0,n):
        p=max(0,w-max(abs(x-i),abs(y-j)))
        locmat[i][j]=locmat[i][j]+p
    k=k+1
k=[]
for sublist in locmat:
    k.append(max(sublist))
kk=max(k)
print kk
