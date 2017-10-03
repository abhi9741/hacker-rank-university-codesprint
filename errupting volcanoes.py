import sys

def createMatrix(rowCount, colCount):
     mat = []
     datalist = []
     i=0
     while i<(rowCount*rowCount): #for creating a list with n*n zeroes
        datalist.append(0)
        i=i+1
     for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(datalist[rowCount * i + j])
        mat.append(rowList)

     return mat

def calc(n,x,y,ww,matr): #for calculating the effect by each volcano in the given region

  i=1
  w=ww
  try:
       if matr[x][y]==0:
           matr[x][y]=w
  except IndexError:
    abhi=0
  w=w-1
  while i<=ww:

    #    print "i",i
    #    print "w",w

       k=0
       while k<=i:
             kk=0
             while kk<=i:
              try:
               if matr[x-k][y+kk]==0:
                matr[x-k][y+kk]=w
              except IndexError:
                abhi=0
              kk=kk+1
             k=k+1

       k=0
       while k<=i:
                kk=0
                while kk<=i:
                 try:
                  if matr[x][y+kk]==0:
                   matr[x][y+kk]=w
                 except IndexError:
                     abhi=0
                 kk=kk+1
                k=k+1

       k=0
       while k<=i:
              kk=0
              while kk<=i:
               try :
                if matr[x+k][y+kk]==0:
                 matr[x+k][y+kk]=w
               except IndexError:
                    abhi=0
               kk=kk+1
              k=k+1

       k=0
       while k<=i:
              kk=0
              while kk<=i:
                try:
                 if matr[x-k][y]==0:
                  matr[x-k][y]=w
                except IndexError:
                    abhi=0
                kk=kk+1
              k=k+1

       k=0
       while k<=i:
                kk=0
                while kk<=i:
                   try:
                    if matr[x+k][y]==0:
                     matr[x+k][y]=w
                   except IndexError:
                       abhi=0
                   kk=kk+1
                k=k+1

       k=0
       while k<=i:
                kk=0
                while kk<=i:
                 try:
                  if matr[x-k][y-kk]==0:
                   matr[x-k][y-kk]=w
                 except IndexError:
                     abhi=0
                 kk=kk+1
                k=k+1

       k=0
       while k<=i:
                kk=0
                while kk<=i:
                 try:
                  if matr[x][y-kk]==0:
                   matr[x][y-kk]=w
                 except IndexError:
                     abhi=0
                 kk=kk+1
                k=k+1

       k=0
       while k<=i:
                kk=0
                while kk<=i:
                 try:
                  if matr[x+k][y-kk]==0:
                   matr[x+k][y-kk]=w
                 except IndexError:
                     abhi=0
                 kk=kk+1
                k=k+1



       i=i+1

       if (w>0):
          w=w-1
    #    print matr
  return matr



if __name__ == "__main__":
 n = int(raw_input().strip())
 m = int(raw_input().strip())
 l=[]
 for a0 in xrange(m):
        x, y, w = raw_input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]

        l.append([x,y,w])
        # print l



orgmat = createMatrix(n,n)
# print (orgmat)

mm=0
bikki=0
while mm<m :

    matr1=createMatrix(n,n)
    x=l[bikki][0]
    y=l[bikki][1]
    z=l[bikki][2]
    # print z
    matr2=calc(n,x,y,z,matr1)
    r1=0
    c1=0
    while r1<n:
        c1=0
        while c1<n:
            orgmat[r1][c1]=orgmat[r1][c1]+matr2[r1][c1]
            c1=c1+1
        r1=r1+1
    # print orgmat
    mm=mm+1
    bikki=bikki+1
k=[]
for sublist in orgmat:
    k.append(max(sublist))
m=max(k)
print m
