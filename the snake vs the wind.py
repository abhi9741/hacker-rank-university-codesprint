n = int(raw_input().strip()) #n cross n matrix
d = raw_input().strip() #direction
x, y = raw_input().strip().split(' ') #starsnt co-ordinates
x, y = [int(x), int(y)]
direction=["n","s","w","e"]

orgmat=[]
for i in range(0,n):
    rowlist=[]
    for j in range(0,n):
        rowlist.append(0)
    orgmat.append(rowlist)

orgmat[x][y]="1"

ds=[(1,0),(0,1),(0,-1),(-1,0)]
de=[(0,1),(1,0),(-1,0),(0,-1)]
dn=[(-1,0),(0,1),(0,-1),(1,0)]
dw=[(0,-1),(1,0),(-1,0),(0,1)]


if d=="n" :
     for pos in range(0,n*n): #position of the snake  , each iteration represents each second
        for s in dn:
            tx=x+s[0]
            ty=y+s[1]
            if  (0<=tx<n) and (0<=ty<n) and (orgmat[tx][ty]==0):
                x=tx
                y=ty
                p=str(pos+2)
                orgmat[tx][ty]=p
                break
if d=="e" :
     for pos in range(0,n*n): #position of the snake  , each iteration represents each second
        for s in de:

            tx=x+s[0]
            ty=y+s[1]

            if  (0<=tx<n) and (0<=ty<n) and (orgmat[tx][ty]==0):

                x=tx
                y=ty

                p=str(pos+2)
                orgmat[tx][ty]=p
                break

if d=="w" :
     for pos in range(0,n*n): #position of the snake  , each iteration represents each second
        for s in dw:
            tx=x+s[0]
            ty=y+s[1]
            if  (0<=tx<n) and (0<=ty<n) and (orgmat[tx][ty]==0):
                x=tx
                y=ty
                p=str(pos+2)
                orgmat[tx][ty]=p
                break

if d=="s" :
     for pos in range(0,n*n): #position of the snake  , each iteration represents each second
        for s in ds:
            tx=x+s[0]
            ty=y+s[1]
            if  (0<=tx<n) and (0<=ty<n) and (orgmat[tx][ty]==0):
                x=tx
                y=ty
                p=str(pos+2)
                orgmat[tx][ty]=p
                break
for i in range(0,n):
 l=orgmat[i]

 k=" ".join(l)
 print k
