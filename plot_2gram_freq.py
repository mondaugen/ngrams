import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import itertools
import string

N_LETTERS=len(string.uppercase)
grams={}
tot=0.0
with open('2grams.txt','r') as f:
    for l in f.readlines():
        k,v=l.split()[:2]
        grams[k]=float(v)
        tot+=grams[k]

missing_keys={x+y for x, y in
        itertools.product(string.uppercase,string.uppercase)}-set(grams.keys())

for m in missing_keys:
    grams[m]=0.

probs=np.zeros((N_LETTERS,N_LETTERS))
start_letter=ord('A')
for i in range(N_LETTERS):
    for j in range(N_LETTERS):
        k=chr(start_letter+i)+chr(start_letter+j)
        probs[i,j]=np.log(grams[k]/tot)

fig,ax=plt.subplots()
ax.imshow(probs)
fig.canvas.draw()
ax.set_xticks(np.arange(0,N_LETTERS,1))
class MyFormatter(matplotlib.ticker.Formatter):
    def __call__(self,x,pos):
        return chr(start_letter+int(x))
    def __init__(self):
        pass
ax.xaxis.set_major_formatter(MyFormatter())
ax.set_yticks(np.arange(0,N_LETTERS,1))
ax.yaxis.set_major_formatter(MyFormatter())

#xtl=[item.get_text() for item in ax.get_xticklabels()]
#print xtl
#xtl=[chr(start_letter+int(item)) for item in xtl]
#ax.set_xticklabels(xtl)
#
#ytl=[item.get_text() for item in ax.get_yticklabels()]
#ytl=[chr(start_letter+int(item)) for item in ytl]
#ax.set_yticklabels(ytl)

plt.show()
