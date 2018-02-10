import sys
nngrams=47
d=[]
for l in sys.stdin.readlines():
    try:
        k,v=l.split()[:2]
        d.append((k,int(v),int(v)*len(k)))
    except ValueError:
        print("ignoring %s" % (l,))

ds=sorted(filter(lambda _d: len(_d[0])>1,d),
        key= lambda _d:_d[2],reverse=True)
print(len(ds))
for i in range(min(nngrams,len(ds))):
    print("%s" % (ds[i][0],))
