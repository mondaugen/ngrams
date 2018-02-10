import sys
import pickle
import random
nngrams=47
d={}
for l in sys.stdin.readlines():
    try:
        k,v=l.split()[:2]
        d[k]=int(v)
    except ValueError:
        print("ignoring %s" % (l,))

#with open("/tmp/hello","wb") as f:
#    pickle.dump(d,f)

# Iterate over ngrams from longest to shortest, subtracting out their inner
# mgrams from those of those size
#for k in sorted(d.keys(),key=len):
sskeys=random.sample(d.keys(),len(d.keys()))
prog=0
dlen=len(sskeys)
for k in sorted(sskeys,key=len,reverse=True):
    print('\033[0G%2.6f %%'%(float(prog)/dlen*100.0,),end='',flush=True)
    n=len(k)
    for m in range(1,n): # excludes n
        for q in range(n-m+1):
            k_=k[q:q+m]
            d[k_]-=d[k]
            #for l in filter(lambda z: k_ in z,sskeys):
            #    d[l] -= d[k]
    prog+=1
di = [(ke,d[ke]) for ke in sskeys]

ds=sorted(filter(lambda _d: len(_d[0])>1,di),
        key= lambda _d:_d[1],reverse=True)
print(len(ds))
for i in range(min(nngrams,len(ds))):
    print("%s %d" % ds[i])
with open("norm_ngrams","wb") as f:
    pickle.dump(ds,f)
